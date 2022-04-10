import maya.cmds as cmds

def _getPosListFromVerts(verts):
    posList = []
    for vert in verts:
        pos = cmds.xform(vert, q=True, ws=True, t=True) #get position from the verts
        posList.append(pos)
    return posList

def _createLocsOnCurve(curv,posList,grpName,newGrp=True):
    locDicList = []
    if newGrp==True:
        grp = cmds.group(em=True, n=grpName)
    else:
        grp = grpName
        
    for pos in posList:
        nearNode = cmds.createNode('nearestPointOnCurve') #create nearestPointOnCurve node
        #connect position to the nearestPointOnCurve node
        cmds.connectAttr( curv+'.worldSpace', nearNode+'.inputCurve' )
        cmds.setAttr( nearNode+'.inPosition', pos[0], pos[1], pos[2], type='double3' )

        cmds.getAttr( nearNode+'.parameter' )#get parameter attribute

        loc = cmds.spaceLocator()[0]#create space locator
        _localScaleLoc(loc,.2)
        cmds.connectAttr( nearNode+'.position', loc+'.t' )#feed in position attribute to the translation of the loc
        
        #get parameter
        param = cmds.getAttr(nearNode+'.parameter')
    
        #delete nearestPointOnCurve node
        cmds.delete(nearNode)

        #create pointOnCurve node
        pointNode = cmds.createNode('pointOnCurveInfo')

        #connect attributes
        cmds.connectAttr(curv+'.worldSpace', pointNode+'.inputCurve')
        cmds.setAttr(pointNode+'.parameter', param)
        cmds.connectAttr(pointNode+'.position', loc+'.t')
        
        cmds.parent(loc,grp)
        
        locDicList.append( {'loc':loc,'param':param} ) #return list of mini dictionaries
    locDicList.sort(key=lambda t: t['param']) #sort the list with parameter
    locList = [d['loc'] for d in locDicList]
    
    for loc in locList:
        cmds.reorder( loc, back=True )#reorder in hierarchy
        
    return locList
    
        
def _aimConstLocs(locs,targ,upObj=None):
    #Create aim constraint on list of locators
    for loc in locs:
        if upObj == None:
            cmds.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] )
        else:
            cmds.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] , worldUpObject=upObj )

def _createJntsOnLocs(locs,parJnt): #parJnt means parent joint
    jntList = []
    for loc in locs:
        cmds.select(cl=True)
        jntName = loc.replace('_loc', '_bind')
        jnt = cmds.joint( n=jntName, rad=.1 )
        const = cmds.parentConstraint(loc, jnt, mo=False)[0]
        '''
        #fuck I don know I'm sorry!?>>???
        cmds.delete(const)
        cmds.makeIdentity(loc) ###why this is here??? XXX
        cmds.makeIdentity(jnt)  ###why orient not applyed??? XXX
        cmds.parentConstraint(loc, jnt, mo=False)
        '''
        cmds.parent(jnt,parJnt)
    return jntList


def _createJntsOnCVs(curv,grpName):
    jntList = []
    grp = cmds.group(em=True, n=grpName)
    
    curvShape = _getCrvShape(curv)
    cvs = _getCVs(curv)

    counter = 0
    for cv in cvs:
        cmds.select(cl=True)
        poc1 = cmds.createNode('pointOnCurveInfo')
        cmds.connectAttr(curvShape+'.worldSpace[0]', poc1+'.inputCurve', f=True)
        param = counter
        cmds.setAttr(poc1 + '.parameter', param)

        jnt= cmds.joint(rad=.3)
        cmds.connectAttr(poc1+'.position', jnt+'.t')
        
        cmds.parent(jnt,grp)
        jntList.append(jnt)
        counter += 1
    return jntList



def _createBindmeshesOnJnts(jnts,grpName):
    bindmeshList = []
    grp = cmds.group(em=True,n=grpName)
    
    for jnt in jnts:
        pos=cmds.xform(jnt,q=True,ws=True,t=True)
        name = jnt.replace('_driver','_bindmesh')
        
        bindmesh = cmds.polyPlane(w=.3,h=.3,sw=1,sh=1,n=name)[0]
        cmds.move(pos[0],pos[1],pos[2],bindmesh)
        cmds.makeIdentity(bindmesh, apply=True) #freeze transformation. If I don't do this, follicles won't attach
        
        cmds.skinCluster(jnt,bindmesh,n='bindMesh_skinCluster',tsb=True)#tsb means toSelectedBones
        
        cmds.parent(bindmesh,grp)
        bindmeshList.append(bindmesh)
    return bindmeshList
    
def _createClsOnBindmeshes(bindmeshes,grpName):
    clsList = []
    grp = cmds.group(em=True, n=grpName)
    for bindmesh in bindmeshes:
        cmds.select(cl=True) #clear selection for safety
        name=bindmesh.replace('bindmesh','cls')
        
        clus = cmds.cluster(bindmesh)
        clsTrans = clus[1]
        clsTrans = cmds.rename(clsTrans, name)
        
        cmds.parent(clsTrans,grp)
        clsList.append(clsTrans)
    return clsList
    
def _createFolsOnBindmeshes(bindmeshes,grpName):
    folList = []
    grp = cmds.group(em=True, n=grpName)
    for bindmesh in bindmeshes:
        name = bindmesh.replace('bindmesh','fol')
        folShape = cmds.createNode('follicle', n=name+'_shape' )
        folTrans = cmds.listRelatives(folShape, p=1)[0]
        folTrans = cmds.rename(folTrans, name)
        bmShape = cmds.listRelatives(bindmesh, type = 'mesh')[0]

        cmds.connectAttr(bmShape+'.worldMesh', folShape+'.inputMesh')
        cmds.connectAttr(folShape+'.outTranslate', folTrans+'.t')
        cmds.connectAttr(folShape+'.outRotate', folTrans+'.r')
        cmds.setAttr(folShape+'.parameterU', .5)
        cmds.setAttr(folShape+'.parameterV', .5)
        
        cmds.parent(folTrans, grp)
        folList.append(folTrans)
    return folList

def _createCtrlGrp(drivenList, nameList, grpName, shape='circle'):
    #Create lip controllers on given drivers.
    #Nurv curves, orient group, nul group
    #lower lip controllers has scale -1 on orient groups
   
    ctlDicList = []
    bigGrp = cmds.group(em=True, n=grpName)
    counter = 0
    for driven in drivenList:
        name = nameList[counter]
        ctl = _customNURBScircle(shape,name)
        
        nulGrp = cmds.group(ctl, n = ctl+'_nul')
        orientGrp = cmds.group(ctl, n=ctl+'_orient')
        offsetGrp = cmds.group(ctl, n=ctl+'_offset')
        cmds.parentConstraint(driven, nulGrp, mo=False)
        
        cmds.parent(nulGrp,bigGrp)
        ctlDicList.append( {'nul':nulGrp,'ori':orientGrp, 'off':offsetGrp,'ctl':ctl} ) #return list of mini dictionaries
        
        counter += 1
    return ctlDicList

def _moveOffset(ctlDicList, offset=(0,0,0)):
    for i in ctlDicList:
        cmds.move(offset[0],offset[1],offset[2], i['off'], r=True)
    
    
def _parentConstIterate(parents,childs):
    for parent,child in zip(parents,childs):
        cmds.parentConstraint(parent,child,mo=True)
    
def _localScaleLoc(loc,num):
    locShape = cmds.listRelatives(loc)[0]
    cmds.setAttr(locShape+'.localScale',num,num,num)
    
def _overrideColor(Crvlist, color=(1,1,0)):
    for crv in Crvlist:
        shape = cmds.listRelatives(crv, shapes=True)[0]
        rgb = ('R','G','B')
        
        cmds.setAttr(shape + '.overrideEnabled',1)
        cmds.setAttr(shape + '.overrideRGBColors',1)
        
        for channel, col in zip(rgb, color):
            cmds.setAttr(shape + '.overrideColor%s' %channel, col)

def _getCrvShape(crv):
    return cmds.listRelatives(crv, type = 'nurbsCurve')[0]

def _getCVs(crv):
    return cmds.ls(crv + '.cv[*]', fl=1)
    
def _customNURBScircle(shape,name):
    if shape=='circle':
        ctl = cmds.circle(n=name, normal=(0,1,0), r=.3, d=1)[0] #degree=1(linear)
    elif shape=='square':
        ctl = cmds.circle(n=name, normal=(0,1,0), r=.5, sections=4, d=1)[0]
    elif shape=='triangle':
        ctl = cmds.circle(n=name, normal=(0,1,0), r=.5, sections=3, d=1)[0]
        CVs = _getCVs(ctl)
        cmds.rotate(0,30,0,CVs)
    
    cmds.delete(ctl, constructionHistory=True)
    return ctl

def _getTransformData(inList, t=False, r=False, ws=False, os=False):
    outData = []
    for i in inList:
        dic = {'name':i}
        if t==True:
            pos = cmds.xform(i, q=True, ws=ws, os=os, t=True)
            dic['pos']=pos
        
        if r==True:
            rot = cmds.getAttr(i+'.r')[0]
            dic['rot']=rot
            
        outData.append(dic)
    return tuple(outData)

def _applyTransformData(inData, ws=False, os=False):
    for i in inData:
        if 'pos' in i:
            pos = i['pos']
            cmds.move(pos[0],pos[1],pos[2],i['name'], ws=ws, os=os)
        
        if 'rot' in i: 
            rot = i['rot']
            cmds.rotate(rot[0],rot[1],rot[2],i['name'])
        
        if 'scl' in i:
            scl = i['scl']
            cmds.scale(scl[0],scl[1],scl[2],i['name'])
            
def _mirrorObj(right):

    left = cmds.duplicate(right)[0]
    left = cmds.rename(left,right.replace('_r_','_l_'))
    cmds.scale(-1,1,1,left)
    cmds.makeIdentity(left, apply=True)
    cmds.delete(left, constructionHistory=True)

    return left

def _mirrorIterate(rightList):
    leftList = []
    for right in rightList:
        left = cmds.duplicate(right)[0]
        left = cmds.rename(left,right.replace('_r_','_l_'))
        cmds.scale(-1,1,1,left)
        cmds.makeIdentity(left, apply=True)
        cmds.delete(left, constructionHistory=True)
        leftList.append(left)
    return leftList

def _mirrorPosX(posList):
    mirList = []
    for pos in posList:
        x,y,z = pos
        mirList.append((-x,y,z))
    return mirList
###---------test execute--------------------------------------
