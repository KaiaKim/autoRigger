import maya.cmds as cmds

def _createLocsOnCurve(curv,verts,grpName):
    locPosList = []
    grp = cmds.group(em=True, n=grpName)
    for vert in verts:
        pos = cmds.xform(vert, q=True, ws=True, t=True ) #get position from the verts

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
        
        locPosList.append( {'loc':loc,'xpos':pos[0]} ) #return list of mini dictionaries
    locPosList.sort(key=lambda t: t['xpos']) #sort the list with x pos value
    return locPosList
        
def _aimConstLocs(locs,targ,upObj):
    #Create aim constraint on list of locators
    for loc in locs:
        cmds.aimConstraint(targ, loc,  aimVector = [0, 0, -1] , upVector = [0, 1, 0], worldUpType = 'objectrotation', worldUpVector = [0, 1, 0] , worldUpObject = upObj )

def _createJntsOnLocs(locs,parJnt): #parJnt means parent joint
    jntList = []
    for loc in locs:
        cmds.select(cl=True)
        jntName = loc.replace('_loc', '_bind')
        jnt = cmds.joint( n=jntName, rad=.1 )
        cmds.parentConstraint(loc, jnt, maintainOffset=False)
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

def _createClsOn2Curv(upCurv,loCurv,grpName):
    #can use this for lip_upper_curve & lip_lower_curve, or eye_upper_curve & eye_lower_curve
    clsList = []
    grp = cmds.group(em=True, n=grpName)
    
    upCurvShape = _getCrvShape(upCurv)
    upCVs = _getCVs(upCurv)
    loCurvShape = _getCrvShape(loCurv)
    loCVs = _getCVs(loCurv)
    leftCorner = [upCVs.pop(0) , loCVs.pop(0)]
    rightCorner = [upCVs.pop(-1) , loCVs.pop(-1)]
    
    leftCornerCls = cmds.cluster(leftCorner)[1] #[1] gets trans node
    cmds.parent(leftCornerCls,grp)
    clsList.append(leftCornerCls)
    
    for cv in upCVs:
        clus = cmds.cluster(cv)[1]
        cmds.parent(clus,grp)
        clsList.append(clus)
        
    rightCornerCls = cmds.cluster(rightCorner)[1]
    cmds.parent(rightCornerCls,grp)
    clsList.append(rightCornerCls)
    
    loCVs.reverse()
    for cv in loCVs:
        clus = cmds.cluster(cv)[1]
        cmds.parent(clus,grp)
        clsList.append(clus)

    return clsList

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
    for i in range(len(childs)):
        cmds.parentConstraint(parents[i],childs[i],mo=True)
    
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

    return ctl

def _getTransformData(inList):
    outData = []
    for i in inList:
        pos = cmds.getAttr(i+'.t')[0]
        rot = cmds.getAttr(i+'.r')[0]
        
        dic = {'name':i, 'pos':pos, 'rot':rot}
        outData.append(dic)
    return tuple(outData)

def _applyTransformData(inData):
    for i in inData:
        pos = i['pos']
        rot = i['rot']

        cmds.move(pos[0],pos[1],pos[2],i['name'], os=True)
        cmds.rotate(rot[0],rot[1],rot[2],i['name'], os=True)

###---------test execute--------------------------------------
