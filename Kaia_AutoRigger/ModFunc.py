import maya.cmds as mc

def _getPosListFromVerts(verts):
    posList = []
    for vert in verts:
        pos = mc.xform(vert, q=True, ws=True, t=True) #get position from the verts
        posList.append(pos)
    return posList

def _createBindsOnCrv(names,posList,curv,grpName):
    try:mc.select(grpName)
    except: mc.group(em=True, n=grpName)
    posDicList = []
    
    for pos in posList:
        nearNode = mc.createNode('nearestPointOnCurve') #create nearestPointOnCurve node
        #connect position to the nearestPointOnCurve node
        mc.connectAttr( curv+'.worldSpace', nearNode+'.inputCurve' )
        mc.setAttr( nearNode+'.inPosition', pos[0], pos[1], pos[2], type='double3' )
        mc.getAttr( nearNode+'.parameter' )#get parameter attribute
        
        mc.select(cl=True)
        jnt = mc.joint(rad=.1)#create joint
        mc.connectAttr( nearNode+'.position', jnt+'.t' )#feed in position attribute to the translation of the jnt
        param = mc.getAttr(nearNode+'.parameter') #get parameter
        mc.delete(nearNode) #delete nearestPointOnCurve node
        pointNode = mc.createNode('pointOnCurveInfo') #create pointOnCurve node

        mc.connectAttr(curv+'.worldSpace', pointNode+'.inputCurve') #connect attributes
        mc.setAttr(pointNode+'.parameter', param)
        mc.connectAttr(pointNode+'.position', jnt+'.t')
        
        mc.parent(jnt,grpName)
        
        posDicList.append( {'jnt':jnt,'param':param} ) #return list of mini dictionaries
    posDicList.sort(key=lambda t: t['param']) #sort the list with parameter
    
    for i,name in zip(posDicList,names):
        jnt=i['jnt']
        mc.reorder( jnt, back=True )#reorder in hierarchy
        mc.rename(jnt,name)


def _createCtlGrp(targList, nameList, grp, ori=True, shape='circle', size=1, opm=False, mid=False):
    if type(targList)!=list: targList = [targList]
    if type(nameList)!=list: nameList = [nameList]
    
    if type(grp)!=list:
        try:mc.select(grp)
        except: mc.group(em=True, n=grp)
    
    for i,targ in enumerate(targList):
        ctl = _customNURBScircle(shape, size, nameList[i])
        nul = mc.group(ctl, n = ctl+'_nul')
        if ori==True: orientGrp = mc.group(ctl, n=ctl+'_orient')
        
        if opm==True:
            mc.connectAttr(targ+'.xformMatrix',nul+'.offsetParentMatrix')
        else:
            const1 = mc.parentConstraint(targ, nul, mo=False)
            mc.delete(const1)
        if mid==True: mc.move(0,nul,x=True,ws=True)
        
        if type(grp)!=list:mc.parent(nul,grp)
        else:mc.parent(nul,grp[i])
        

def _createAutoGrp(child,parent,name=None):
    if name==None: name=child+'_auto'
    auto=mc.group(em=True,n=name)
    mc.parent(auto,parent,r=True)
    mc.parent(child,auto)

def _handleToggle(ctl):
    shape=_getCrvShape(ctl)
    mc.addAttr(ctl, sn='handle', k=True, dv=1, at='bool')
    mc.connectAttr(ctl+'.handle',ctl+'.displayHandle')
    rev1=mc.createNode('reverse')
    mc.connectAttr(ctl+'.handle',rev1+'.inputX')
    mc.connectAttr(rev1+'.outputX',shape+'.visibility')

def _scaleOrient(ctlList,s=(-1,1,1)):
    for i in ctlList:
        if '_l_' in i:
            mc.scale(s[0],s[1],s[2],i+'_orient')
            
    

def _offsetCtls(ctlList, r=(0,0,0), s=(1,1,1), t=(0,0,0)):
    if type(ctlList)!=list: ctlList = [ctlList]
    for ctl in ctlList:
        CVs = _getCVs(ctl)
        mc.rotate(r[0],r[1],r[2], CVs, r=True)
        mc.scale(s[0],s[1],s[2], CVs, r=True)
        mc.move(t[0],t[1],t[2], CVs, r=True)
        
    
def _normalizeCtls(ctls,val=(1,1,1)):
    val = list(val)
    for i in ctls:
        _offsetCtls(i, s=(1/val[0], 1/val[1], 1/val[2]))
        mc.scale(val[0], val[1], val[2], i+'_orient',r=True)

def _bindSkin(jnts,geos,maxi=4):
    if type(geos)!=list: geos = [geos]
    mc.select(jnts,geos)
    for geo in geos:
        try:mc.skinCluster(tsb=True,mi=maxi,sm=0,n=geo+'_skinCluster')#name the skinCluster based on geo!
        except: print('###'+ geo +' is already skinned ###')

def _connectTransform(driver,driven):
    mc.connectAttr(driver+'.t',driven+'.t')
    mc.connectAttr(driver+'.r',driven+'.r')
    #mc.connectAttr(driver+'.s',driven+'.s')

def _parentConstIterate(parents,childs):
    for parent,child in zip(parents,childs):
        const1 = mc.parentConstraint(parent,child,mo=True)
        mc.setAttr(const1+'.interpType', 2) #shortest

def _parentIterate(parents,childs):
    for parent,child in zip(parents,childs):
        mc.parent(child,parent)

def _aimConstIterate(locs,targ,upObj=None):
    for loc in locs:
        if upObj == None:
            mc.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] )
        else:
            mc.aimConstraint(targ, loc, aimVector=[0,0,-1], upVector=[0,1,0], worldUpType='objectrotation', worldUpVector=[0,1,0] , worldUpObject=upObj )

def _localScaleLoc(loc,num):
    locShape = mc.listRelatives(loc)[0]
    mc.setAttr(locShape+'.localScale',num,num,num)
    
def _overrideColor(crvList, color=(1,1,0)):
    if type(crvList)!=list: crvList = [crvList]
    for crv in crvList:
        try:
            shape = mc.listRelatives(crv, shapes=True)[0]
            rgb = ('R','G','B')
            
            mc.setAttr(shape + '.overrideEnabled',1)
            mc.setAttr(shape + '.overrideRGBColors',1)
            
            for channel, col in zip(rgb, color):
                mc.setAttr(shape + '.overrideColor%s' %channel, col)
        except:print('ERROR: _overrideColor:',crv,'is not curve')
        
def _getCrvShape(crv):
    return mc.listRelatives(crv, type = 'nurbsCurve')[0]

def _getCVs(crv):
    return mc.ls(crv + '.cv[*]', fl=1)
    
def _customNURBScircle(shape, size, name):
    if shape=='circle':
        ctl = mc.circle(n=name, r=size, d=1)[0] #degree=1(linear)
    elif shape== 'semiCircle':
        ctl = mc.circle(n=name, r=size, d=1)[0]
        mc.move(0,ctl+'.cv[3:5]',y=True,a=True)
        mc.move(-.5*size,ctl+'.cv[*]',y=True,r=True)
    elif shape=='square':
        ctl = mc.circle(n=name, r=size, sections=4, d=1)[0]
        mc.rotate(0,0,45,ctl+'.cv[*]')
    elif shape=='triangle':
        ctl = mc.circle(n=name, r=size, sections=3, d=1)[0]
        mc.move(0,-.25*size,0,ctl+'.cv[*]',r=True)
    elif shape=='arch':
        ctl = mc.circle(n=name, r=size, sections=6, d=0)[0]
        mc.move(0,2*size,0,ctl+'.cv[4]',r=True)
        mc.move(0,-.3*size,0,ctl+'.cv[*]',r=True)
    elif shape== 'pentagon':
        ctl = mc.circle(n=name, r=size, sections=5, d=1)[0]
    else:
        print('wrong shape name')
    mc.delete(ctl, constructionHistory=True)
    return ctl


def _mirrorObj(name,right):
    left = mc.duplicate(right, n=name)[0]
    mc.scale(-1,1,1,left)
    mc.makeIdentity(left, apply=True)
    mc.delete(left, constructionHistory=True)

def _mirrorIterate(rightList):
    leftList = []
    for right in rightList:
        left = mc.duplicate(right)[0]
        left = mc.rename(left,right.replace('_r_','_l_'))
        mc.scale(-1,1,1,left)
        mc.makeIdentity(left, apply=True)
        mc.delete(left, constructionHistory=True)
        leftList.append(left)
    return leftList

def _mirrorPosX(posList):
    mirList = []
    for pos in posList:
        x,y,z = pos
        mirList.append((-x,y,z))
    return mirList

###nose func


###---------test execute--------------------------------------
if __name__ == "__main__":
    pass
