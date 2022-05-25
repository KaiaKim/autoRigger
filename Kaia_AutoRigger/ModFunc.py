import maya.cmds as cmds

def _getPosListFromVerts(verts):
    posList = []
    for vert in verts:
        pos = cmds.xform(vert, q=True, ws=True, t=True) #get position from the verts
        posList.append(pos)
    return posList

def _createLocsOnCurve(names,posList,curv,grpName,newGrp=True):
    ###no create locator when there's already one
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
    
    for i,name in zip(locDicList,names):
        loc=i['loc']
        cmds.reorder( loc, back=True )#reorder in hierarchy
        cmds.rename(loc,name)

    
        
def _aimConstLocs(locs,targ,upObj=None):
    #Create aim constraint on list of locators
    for loc in locs:
        if upObj == None:
            cmds.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] )
        else:
            cmds.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] , worldUpObject=upObj )

def _createJntsOnLocs(locs,names,parent): #parent should be a joint
    for loc,name in zip(locs,names):
        cmds.select(cl=True)
        jnt = cmds.joint( n=name, rad=.1 )
        const = cmds.parentConstraint(loc, jnt, mo=False)[0]
        cmds.parent(jnt,parent)


def _createJntsOnCVs(names,curv,grpName,newGrp=True):
    jntList = []
    if newGrp==True:
        grp = cmds.group(em=True, n=grpName)
    elif newGrp==False:
        grp = grpName
    
    curvShape = _getCrvShape(curv)
    cvs = _getCVs(curv)

    for num,cv in enumerate(cvs):
        cmds.select(cl=True)
        poc1 = cmds.createNode('pointOnCurveInfo')
        cmds.connectAttr(curvShape+'.worldSpace[0]', poc1+'.inputCurve', f=True)
        param = num 
        cmds.setAttr(poc1 + '.parameter', param)

        jnt= cmds.joint(rad=.3)
        cmds.connectAttr(poc1+'.position', jnt+'.t')
        
        cmds.parent(jnt,grp)
        jntList.append(jnt)

    jntList = jntList[-1:] + jntList[:-1] #param 0 attachs to cv[1] for somehow, so I shifted last element to first position in list.
    for name,jnt in zip(names,jntList):
        cmds.rename(jnt,name)
        




def _createBindmeshesOnJnts(names,jnts,grpName):
    grp = cmds.group(em=True,n=grpName)
    for jnt,name in zip(jnts,names):
        pos=cmds.xform(jnt,q=True,ws=True,t=True)
        
        bindmesh = cmds.polyPlane(w=.3,h=.3,sw=1,sh=1,n=name)[0]
        cmds.move(pos[0],pos[1],pos[2],bindmesh)
        cmds.makeIdentity(bindmesh, apply=True) #freeze transformation. If I don't do this, follicles won't attach
        
        cmds.skinCluster(jnt,bindmesh,n='bindMesh_skinCluster',tsb=True)#tsb means toSelectedBones
        
        cmds.parent(bindmesh,grp)

    
def _createClsOnBindmeshes(names,bindmeshes,grpName):
    grp = cmds.group(em=True, n=grpName)
    for bindmesh,name in zip(bindmeshes,names):
        cmds.select(cl=True) #clear selection for safety
        clus = cmds.cluster(bindmesh)
        clsTrans = clus[1]
        clsTrans = cmds.rename(clsTrans, name)
        cmds.parent(clsTrans,grp)
        
    
def _createFolsOnBindmeshes(names,bindmeshes,grpName):
    grp = cmds.group(em=True, n=grpName)
    for bindmesh,name in zip(bindmeshes,names):
        folShape = cmds.createNode('follicle', n=name+'_shape' )
        folTrans = cmds.listRelatives(folShape, p=1)[0]
        folTrans = cmds.rename(folTrans, name)
        bmShape = cmds.listRelatives(bindmesh, type='mesh')[0]

        cmds.connectAttr(bmShape+'.worldMesh', folShape+'.inputMesh')
        cmds.connectAttr(folShape+'.outTranslate', folTrans+'.t')
        cmds.connectAttr(folShape+'.outRotate', folTrans+'.r')
        cmds.setAttr(folShape+'.parameterU', .5)
        cmds.setAttr(folShape+'.parameterV', .5)
        
        cmds.parent(folTrans, grp)


def _createCtlGrp(targList, nameList, grpName, newGrp=True, ori=True, shape='circle', size=1, const=True, mid=False):
    #Nurv curves, orient group, offset group, nul group

    
    if newGrp==True: bigGrp = cmds.group(em=True, n=grpName)
    else: bigGrp = grpName
    
    for name,targ in zip(nameList,targList):
        ctl = _customNURBScircle(shape, size, name)
        
        nulGrp = cmds.group(ctl, n = ctl+'_nul')
        if ori==True: orientGrp = cmds.group(ctl, n=ctl+'_orient')
        
        constNode = cmds.parentConstraint(targ, nulGrp, mo=False)
        if const==False: cmds.delete(constNode)
        if mid==True: cmds.move(0,nulGrp,x=True,ws=True)
        
        cmds.parent(nulGrp,bigGrp)

def _90dOrient(ctlList):
    for i in ctlList:
        cmds.rotate(90,0,0,i+'_orient')

def _scaleOrient(ctlList):
    for i in ctlList:
        scaleVal = [1,1,1]
        if '_lower_' in i:
            scaleVal[1] = -1 #Y value is -1 
        if '_l_' in i:
            scaleVal[0] = -1 #X value is -1
        
        cmds.scale(scaleVal[0],scaleVal[1],scaleVal[2],i+'_orient')

def _offsetCtls(ctlList, r=(0,0,0), s=(1,1,1), t=(0,0,0)):
    for ctl in ctlList:
        CVs = _getCVs(ctl)
        cmds.rotate(r[0],r[1],r[2], CVs, r=True)
        cmds.scale(s[0],s[1],s[2], CVs, r=True)
        cmds.move(t[0],t[1],t[2], CVs, r=True)
        
    
def _normalizeCtls(ctls,val=(1,1,1)):
    val = list(val)
    for i in ctls:
        cmds.scale(1/val[0], 1/val[1], 1/val[2],i)
        cmds.scale(val[0], val[1], val[2], i+'_orient',r=True)


def _parentConstIterate(parents,childs):
    for parent,child in zip(parents,childs):
        cmds.parentConstraint(parent,child,mo=True)

def _parentIterate(parents,childs):
    for parent,child in zip(parents,childs):
        cmds.parent(child,parent)

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
    
def _customNURBScircle(shape, size, name):
    if shape=='circle':
        ctl = cmds.circle(n=name, r=size, d=1)[0] #degree=1(linear)
    elif shape== 'semiCircle':
        ctl = cmds.circle(n=name, r=size, d=1)[0]
        cmds.move(0,ctl+'.cv[3:5]',y=True,a=True)
        cmds.move(-.5*size,ctl+'.cv[*]',y=True,r=True)
    elif shape=='square':
        ctl = cmds.circle(n=name, r=size, sections=4, d=1)[0]
    elif shape=='triangle':
        ctl = cmds.circle(n=name, r=size, sections=3, d=1)[0]
        cmds.move(0,-.25*size,0,ctl+'.cv[*]',r=True)
    elif shape=='arch':
        ctl = cmds.circle(n=name, r=size, sections=6, d=0)[0]
        cmds.move(0,2*size,0,ctl+'.cv[4]',r=True)
        cmds.move(0,-.3*size,0,ctl+'.cv[*]',r=True)
    elif shape== 'pentagon':
        ctl = cmds.circle(n=name, r=size, sections=5, d=1)[0]
    else:
        print('wrong shape name')
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
            
def _mirrorObj(name,right):
    left = cmds.duplicate(right, n=name)[0]
    cmds.scale(-1,1,1,left)
    cmds.makeIdentity(left, apply=True)
    cmds.delete(left, constructionHistory=True)

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


