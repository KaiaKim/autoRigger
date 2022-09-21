### utility functions
import maya.cmds as mc
import importlib

from Kaia_AutoRigger.modules import getset
importlib.reload(getset)
###-------------------------------------------------------------------------------------------

def getPosListFromVerts(verts):
    posList = []
    for vert in verts:
        pos = mc.xform(vert, q=True, ws=True, t=True)
        posList.append(pos)
    return posList

def createBindsOnCrv(names, posList, curv, grpName):
    if not mc.ls(grpName): mc.group(em=True, n=grpName)
    
    posDicList = []
    for pos in posList:
        nearNode = mc.createNode('nearestPointOnCurve')
        mc.connectAttr(curv+'.worldSpace', nearNode+'.inputCurve')
        mc.setAttr(nearNode+'.inPosition', pos[0], pos[1], pos[2], type='double3')
        mc.getAttr(nearNode+'.parameter')
        
        mc.select(cl=True)
        jnt = mc.joint(rad=.1)
        mc.connectAttr( nearNode+'.position', jnt+'.t')
        param = mc.getAttr(nearNode+'.parameter')
        mc.delete(nearNode)
        pointNode = mc.createNode('pointOnCurveInfo')

        mc.connectAttr(curv+'.worldSpace', pointNode+'.inputCurve')
        mc.setAttr(pointNode+'.parameter', param)
        mc.connectAttr(pointNode+'.position', jnt+'.t')
        
        mc.parent(jnt,grpName)
        
        posDicList.append({'jnt':jnt,'param':param}) #return list of mini dictionaries
    posDicList.sort(key=lambda t: t['param']) #sort the list with parameter
    
    for i, name in zip(posDicList, names):
        jnt = i['jnt']
        mc.reorder(jnt, back=True) #reorder in hierarchy
        mc.rename(jnt, name)


def createCtlGrp(targs, names, grps, ori=True, shape='circle', size=1, opm=False, mid=False):
    if isinstance(targs,str): targs = [targs]
    if isinstance(names,str): names = [names]
    

    for i, targ in enumerate(targs):
        ctl = customNURBScircle(shape, size, names[i])
        nul = mc.group(ctl, n=ctl+'_nul')
        
        if ori == True:
            orientGrp = mc.group(ctl, n=ctl+'_orient')
        
        if opm == True:
            mc.connectAttr(targ+'.xformMatrix', nul+'.offsetParentMatrix')
        else:
            const1 = mc.parentConstraint(targ, nul, mo=False)
            mc.delete(const1)
            
        if mid == True:
            mc.move(0, nul, x=True, ws=True)
        
        if isinstance(grps,str):
            if not mc.ls(grps):
                mc.group(em=True, n=grps)
            mc.parent(nul, grps)
        elif isinstance(grps,list):
            mc.parent(nul, grps[i])
        elif grps == None:
            pass
        

def createAutoGrp(child, parent, name=None):
    if name == None: name = child+'_auto'
    auto = mc.group(em=True, n=name)
    mc.parent(auto, parent, r=True)
    mc.parent(child, auto)

def handleToggle(ctl):
    shape=getset.getCrvShape(ctl)
    mc.addAttr(ctl, sn='handle', k=True, dv=1, at='bool')
    mc.connectAttr(ctl+'.handle', ctl+'.displayHandle')
    rev1=mc.createNode('reverse')
    mc.connectAttr(ctl+'.handle', rev1+'.inputX')
    mc.connectAttr(rev1+'.outputX', shape+'.visibility')

def scaleOrient(ctls, s=(-1, 1, 1)):
    for ctl in ctls:
        if '_l_' in ctl:
            mc.scale(s[0], s[1], s[2], ctl+'_orient')    
    

def offsetCtls(ctls, r=(0,0,0), s=(1,1,1), t=(0,0,0), reverseZ=False):
    if isinstance(ctls,str): ctls = [ctls]
    
    for ctl in ctls:
        CVs = getset.getCVs(ctl)
        
        mc.rotate(r[0], r[1], r[2], CVs, r=True)
        mc.scale(s[0], s[1], s[2], CVs, r=True)
        if reverseZ == True and '_l_' in ctl:
            mc.move(t[0], t[1], -t[2], CVs, r=True)
        else:
            mc.move(t[0], t[1], t[2], CVs, r=True)
        
    
def normalizeCtls(ctls, val=(1,1,1)):
    val = list(val)
    for i in ctls:
        offsetCtls(i, s=(1/val[0], 1/val[1], 1/val[2]))
        mc.scale(val[0], val[1], val[2], i+'_orient', r=True)

def bindSkin(jnts, geos, mi=4):
    if isinstance(geos,str): geos = [geos]
    for geo in geos:
        if checkSkinned(geo): continue #skinned
        mc.select(jnts,geo)
        mc.skinCluster(tsb=True, mi=mi, sm=0, n=geo+'_skinClst')#check if works
        
def checkSkinned(obj):
        shape = mc.listRelatives(obj,c=True,s=True)[0]
        skinClst = mc.listConnections(shape, t='skinCluster', d=False)

        if skinClst != None:
            print('%s is already skinned'%obj)
            return True    
        else:
            return False


def connectTransform(driver, driven, reverseZ=False):
    mc.connectAttr(driver+'.tx', driven+'.tx')
    mc.connectAttr(driver+'.ty', driven+'.ty')  
    mc.connectAttr(driver+'.rx', driven+'.rx')
    mc.connectAttr(driver+'.rz', driven+'.rz')   
    if reverseZ == True and '_l_' in driver:
        mult1 = mc.createNode('multDoubleLinear')
        mc.connectAttr(driver+'.tz', mult1+'.input1')
        mc.setAttr(mult1+'.input2', -1)
        mc.connectAttr(mult1+'.output', driven+'.tz')
        mult2 = mc.createNode('multDoubleLinear')
        mc.connectAttr(driver+'.ry', mult2+'.input1')
        mc.setAttr(mult2+'.input2', -1)
        mc.connectAttr(mult2+'.output', driven+'.ry')
    else:
        mc.connectAttr(driver+'.ry', driven+'.ry')
        mc.connectAttr(driver+'.tz', driven+'.tz')


def matchTransformIterate(parents, childs):
    if isinstance(parents,str): parents = [parents]
    if isinstance(childs,str): childs = [childs]
    
    constList = []
    for parent, child in zip(parents, childs):
        if mc.ls(parent) != [] and mc.ls(child) != []:
            const1 = mc.parentConstraint(parent, child, mo=False)[0]
            constList.append(const1)
    mc.delete(constList)
    
def parentConstIterate(parents, childs):
    for parent, child in zip(parents, childs):
        const1 = mc.parentConstraint(parent, child, mo=True)[0]
        mc.setAttr(const1+'.interpType', 2) #shortest

def parentConstAlterInv(parent, child, alter):
        const1 = mc.parentConstraint(parent, child, mo=True)[0]
        mc.setAttr(const1+'.interpType', 2) #shortest
        mc.disconnectAttr(child+'.parentInverseMatrix', const1+'.constraintParentInverseMatrix')
        mc.connectAttr(alter+'.parentInverseMatrix', const1+'.constraintParentInverseMatrix')

def parentIterate(parents, childs):
    for parent, child in zip(parents, childs):
        mc.parent(child, parent)

def aimConstIterate(locs, targ, upObj=None,MO=False):
    for loc in locs:
        if upObj == None:
            mc.aimConstraint(
                targ, loc, aimVector=[0,0,-1], upVector=[0,1,0],
                worldUpType='objectrotation', worldUpVector=[0,1,0],
                mo=MO
                )
        else:
            mc.aimConstraint(
                targ, loc, aimVector=[0,0,-1], upVector=[0,1,0],
                worldUpType='objectrotation', worldUpVector=[0,1,0],
                worldUpObject=upObj,mo=MO
                )

def localScaleLoc(loc,num):
    locShape = mc.listRelatives(loc)[0]
    mc.setAttr(locShape+'.localScale', num, num, num)
    
def overrideColor(crvs, color=(1,1,0)):
    if isinstance(crvs,str): crvs = [crvs]
    for crv in crvs:
        if mc.ls(crv) != []:
            try:
                rgb = ('R','G','B')
                mc.setAttr(crv + '.overrideEnabled', 1)
                mc.setAttr(crv + '.overrideRGBColors', 1)
                for channel, col in zip(rgb, color):
                    mc.setAttr(crv + '.overrideColor%s' %channel, col)
            except:
                mc.warning('ERROR: overrideColor failed: '+ crv) ##use raise instead
        

    
def customNURBScircle(shape, size, name):
    if shape =='circle':
        ctl = mc.circle(n=name, r=size, d=1)[0] #degree=1(linear)
    elif shape == 'semiCircle':
        ctl = mc.circle(n=name, r=size, d=1)[0]
        mc.move(0,ctl+'.cv[3:5]', y=True, a=True)
        mc.move(-.5*size,ctl+'.cv[*]', y=True, r=True)
    elif shape =='square':
        ctl = mc.circle(n=name, r=size, sections=4, d=1)[0]
        mc.rotate(0,0,45,ctl+'.cv[*]')
    elif shape =='triangle':
        ctl = mc.circle(n=name, r=size, sections=3, d=1)[0]
        mc.move(0,-.25*size,0,ctl+'.cv[*]', r=True)
    elif shape =='arch':
        ctl = mc.circle(n=name, r=size, sections=6, d=0)[0]
        mc.move(0,2*size,0,ctl+'.cv[4]', r=True)
        mc.move(0,-.3*size,0,ctl+'.cv[*]', r=True)
    elif shape == 'pentagon':
        ctl = mc.circle(n=name, r=size, sections=5, d=1)[0]
    else:
        print('wrong shape name')
    mc.delete(ctl, constructionHistory=True)
    return ctl






###---------test execute--------------------------------------
if __name__ == "__main__":
    targs = cmds.ls(sl=True)
    names = [d+'_ctl' for d in targs]
    par = 'hair_ctl_Grp'
    
    for name, targ in zip(names,targs):
        createCtlGrp(
            targ, name, par, ori=False,
            shape='circle', size=3,
            opm=False, mid=False
            )
        offsetCtls(name, r=(0,90,0))
        mc.setAttr(name + '.overrideEnabled', 1)
        mc.setAttr(name + '.overrideColor', 21)
        mc.parentConstraint(name, targ, mo=False)
        par = name
