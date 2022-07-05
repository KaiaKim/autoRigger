import maya.cmds as cmds

def _getPosListFromVerts(verts):
    posList = []
    for vert in verts:
        pos = cmds.xform(vert, q=True, ws=True, t=True) #get position from the verts
        posList.append(pos)
    return posList

def _createBindsOnCrv(names,posList,curv,grpName):
    try:cmds.select(grpName)
    except: cmds.group(em=True, n=grpName)
    posDicList = []
    
    for pos in posList:
        nearNode = cmds.createNode('nearestPointOnCurve') #create nearestPointOnCurve node
        #connect position to the nearestPointOnCurve node
        cmds.connectAttr( curv+'.worldSpace', nearNode+'.inputCurve' )
        cmds.setAttr( nearNode+'.inPosition', pos[0], pos[1], pos[2], type='double3' )
        cmds.getAttr( nearNode+'.parameter' )#get parameter attribute
        
        cmds.select(cl=True)
        jnt = cmds.joint(rad=.1)#create joint
        cmds.connectAttr( nearNode+'.position', jnt+'.t' )#feed in position attribute to the translation of the jnt
        param = cmds.getAttr(nearNode+'.parameter') #get parameter
        cmds.delete(nearNode) #delete nearestPointOnCurve node
        pointNode = cmds.createNode('pointOnCurveInfo') #create pointOnCurve node

        cmds.connectAttr(curv+'.worldSpace', pointNode+'.inputCurve') #connect attributes
        cmds.setAttr(pointNode+'.parameter', param)
        cmds.connectAttr(pointNode+'.position', jnt+'.t')
        
        cmds.parent(jnt,grpName)
        
        posDicList.append( {'jnt':jnt,'param':param} ) #return list of mini dictionaries
    posDicList.sort(key=lambda t: t['param']) #sort the list with parameter
    
    for i,name in zip(posDicList,names):
        jnt=i['jnt']
        cmds.reorder( jnt, back=True )#reorder in hierarchy
        cmds.rename(jnt,name)


def _createCtlGrp(targList, nameList, grpName, ori=True, shape='circle', size=1, mid=False, opm=False):
    if type(targList)!=list: targList = [targList]
    if type(nameList)!=list: nameList = [nameList]
    
    try:cmds.select(grpName)
    except: cmds.group(em=True, n=grpName)
    
    for name,targ in zip(nameList,targList):
        ctl = _customNURBScircle(shape, size, name)
        nul = cmds.group(ctl, n = ctl+'_nul')
        if ori==True: orientGrp = cmds.group(ctl, n=ctl+'_orient')
        
        if opm==True:
            cmds.connectAttr(targ+'.xformMatrix',nul+'.offsetParentMatrix')
        else:
            const1 = cmds.parentConstraint(targ, nul, mo=False)
            cmds.delete(const1)
            
        if mid==True: cmds.move(0,nul,x=True,ws=True)
        
        cmds.parent(nul,grpName)

def _90dOrient(ctlList):
    for i in ctlList:
        cmds.rotate(90,0,0,i+'_orient')

def _scaleOrient(ctlList):
    for i in ctlList:
        scaleVal = [1,1,1]

        if '_l_' in i:
            scaleVal = (-1,1,1) #X value is -1
        if 'mouth_corner_l_ctl' in i:
            scaleVal = (1,1,-1)
        
        cmds.scale(scaleVal[0],scaleVal[1],scaleVal[2],i+'_orient')

def _offsetCtls(ctlList, r=(0,0,0), s=(1,1,1), t=(0,0,0)):
    if type(ctlList)!=list: ctlList = [ctlList]
    for ctl in ctlList:
        CVs = _getCVs(ctl)
        cmds.rotate(r[0],r[1],r[2], CVs, r=True)
        cmds.scale(s[0],s[1],s[2], CVs, r=True)
        cmds.move(t[0],t[1],t[2], CVs, r=True)
        
    
def _normalizeCtls(ctls,val=(1,1,1)):
    val = list(val)
    for i in ctls:
        _offsetCtls(i, s=(1/val[0], 1/val[1], 1/val[2]))
        cmds.scale(val[0], val[1], val[2], i+'_orient',r=True)

def _skinCrv(jnts,crv):
    cmds.select(jnts,crv)
    cmds.skinCluster(maximumInfluences=1)

def _connectTransform(driver,driven):
    cmds.connectAttr(driver+'.t',driven+'.t')
    cmds.connectAttr(driver+'.r',driven+'.r')
    #cmds.connectAttr(driver+'.s',driven+'.s')

def _parentConstIterate(parents,childs):
    for parent,child in zip(parents,childs):
        cmds.parentConstraint(parent,child,mo=True)

def _parentIterate(parents,childs):
    for parent,child in zip(parents,childs):
        cmds.parent(child,parent)

def _aimConstIterate(locs,targ,upObj=None):
    for loc in locs:
        if upObj == None:
            cmds.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] )
        else:
            cmds.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] , worldUpObject=upObj )

def _localScaleLoc(loc,num):
    locShape = cmds.listRelatives(loc)[0]
    cmds.setAttr(locShape+'.localScale',num,num,num)
    
def _overrideColor(crvList, color=(1,1,0)):
    if type(crvList)!=list: crvList = [crvList]
    for crv in crvList:
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

### where to put?
def _createCheekDrv(drvs,targs,parent):
    for drv,targ in zip(drvs,targs):
        cmds.group(em=True,w=True,n=drv)
        cmds.connectAttr(targ+'.worldMatrix',drv+'.offsetParentMatrix')
        cmds.disconnectAttr(targ+'.worldMatrix',drv+'.offsetParentMatrix')
        
        cmds.parent(drv,parent)
        cmds.makeIdentity(drv,apply=True, t=1)
        
        cmds.pointConstraint(targ,drv,mo=False)


def _createCheekAuto(ctls,cornerCtls,val):
    for ctl,cornerCtl in zip(ctls,cornerCtls):
        name = ctl + '_auto'
        cmds.group(ctl,n=name)
        mult = cmds.createNode('multiplyDivide')
        cmds.connectAttr(cornerCtl+'.t',mult+'.input1')
        cmds.setAttr(mult+'.input2',val[0],val[1],val[2],type='double3')
        cmds.connectAttr(mult+'.output',name+'.t')
    #create node 'multiplyDivide'
    #connect attr ctl translate > input1
    #connect attr output > nul translate
    #customize set attr input2 #initial value = .75
###---------test execute--------------------------------------


