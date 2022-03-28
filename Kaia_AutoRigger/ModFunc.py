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
    
    print('upCVs:',upCVs)
    for cv in upCVs:
        clus = cmds.cluster(cv)[1]
        cmds.parent(clus,grp)
        clsList.append(clus)
        
    rightCornerCls = cmds.cluster(rightCorner)[1]
    cmds.parent(rightCornerCls,grp)
    clsList.append(rightCornerCls)
    
    loCVs.reverse()
    print('loCVs:',loCVs)
    for cv in loCVs:
        clus = cmds.cluster(cv)[1]
        cmds.parent(clus,grp)
        clsList.append(clus)
        
    print('clsList:',clsList)
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

def _createCtrlGrp(fols, grpName, offset=(0,0,0)):
    #Create lip controllers on the follicles.
    #We need both micro controllers, and macro controllers. So we're gonna call this function twice with different attr.
    #Nurv curves, ctl group, orient group, nul group
    #lower lip controllers has scale -1 on orient groups
    #I have to figure out how to figure out the offset value
    ctlList = []
    bigGrp = cmds.group(em=True, n=grpName)
    for fol in fols:
        name = fol.replace('fol','ctl')

        ctl = cmds.circle(n=name, normal=(0,1,0), r=.3, d=1)[0] #degree=1(linear)
        nulGrp = cmds.group(ctl, n = ctl+'_nul')
        cmds.parentConstraint(fol, nulGrp, mo=False)
        orientGrp = cmds.group(ctl, n=ctl+'_orient')
        cmds.move(offset[0],offset[1],offset[2], orientGrp, r=True)
        
        scaleVal = [1,1,1]
        if '_lower_' in name:
            scaleVal[2] = -1 #Z value is -1 
        if '_l_' in name:
            scaleVal[0] = -1 #X value is -1
        
        cmds.scale(scaleVal[0],scaleVal[1],scaleVal[2],orientGrp)
        
        cmds.parent(nulGrp,bigGrp)
        ctlList.append(ctl)
    return ctlList
    
def _parentConstIterate(parents,childs):
    for i in range(len(childs)):
        cmds.parentConstraint(parents[i],childs[i],mo=True)
    
def _localScaleLoc(loc,num):
    locShape = cmds.listRelatives(loc)[0]
    cmds.setAttr(locShape+'.localScale',num,num,num)
    
def _overrideColor(dag, color=(1,1,0)):
    shape = cmds.listRelatives(dag, shapes=True)[0]
    rgb = ('R','G','B')
    
    cmds.setAttr(shape + '.overrideEnabled',1)
    cmds.setAttr(shape + '.overrideRGBColors',1)
    
    for channel, color in zip(rgb, color):
        cmds.setAttr(shape + '.overrideColor%s' %channel, color)

def _getCrvShape(crv):
    return cmds.listRelatives(crv, type = 'nurbsCurve')[0]

def _getCVs(crv):
    return cmds.ls(crv + '.cv[*]', fl=1)
    
###---------test execute--------------------------------------
