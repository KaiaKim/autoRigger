import maya.cmds as mc
import importlib

from . import util
from . import getset
importlib.reload(util)
importlib.reload(getset)

def createMouthCrv(name, upperCrv, lowerCrv):
    upperCVs = getset.getCVs(upperCrv)
    lowerCVs = getset.getCVs(lowerCrv)
    lowerCVs.reverse() #reverse list order so that it comes back to the start, as a circle
    cvList = upperCVs + lowerCVs

    sectionCount = 11
    mouthCrv = mc.circle(n=name, s=sectionCount, d=1)[0] #create a new curve #cv 0~11
    mc.delete(mouthCrv,constructionHistory=True)

    counter = 0
    for i in range(12): #We're going to iterate through mouth curv(CVs)
        pos = mc.xform(cvList[counter], q=True, t=True, ws=True) #get world position from the CV
        if counter == 6: #there's two cvs overlapping on the corner. 6 is the right corner CV.
            counter += 1 #We skip the overlapping cv by adding 1 to the counter
               
        mouthCV = mouthCrv + '.cv[%d]'%i #get mouth CV
        mc.move(pos[0], pos[1], pos[2], mouthCV) #snap mouth CV to the position

        counter += 1

def createBindmeshes(names, targs, grpName):
    grp = mc.group(em=True, n=grpName)
    for targ,name in zip(targs, names):
        pos=mc.xform(targ, q=True, ws=True, t=True)
        bindmesh = mc.polyPlane(w=.3, h=.3, sw=1, sh=1, n=name)[0]
        mc.move(pos[0],pos[1],pos[2], bindmesh)
        mc.makeIdentity(bindmesh, apply=True) #freeze transformation
        mc.delete(bindmesh, constructionHistory=True)
        
        mc.parent(bindmesh,grp)

def skinBindmeshes(bms, jnts):
    for jnt, bm in zip(jnts, bms):
        mc.skinCluster(jnt, bm, n='bindMesh_skinClst', tsb=True)

def createUvPin(names, bindmeshes):
    for bm,name in zip(bindmeshes, names):
        pin1=mc.createNode('uvPin')
        pin1=mc.rename(pin1, name)
        mc.setAttr(pin1+'.coordinate[0].coordinateU', 0.5)
        mc.setAttr(pin1+'.coordinate[0].coordinateV', 0.5)
        mc.setAttr(pin1+'.normalAxis', 1) #Y
        mc.setAttr(pin1+'.tangentAxis', 0) #X
        mc.connectAttr(bm+'Shape.worldMesh[0]', pin1+'.deformedGeometry')
        mc.connectAttr(bm+'ShapeOrig.outMesh', pin1+'.originalGeometry')    


def createMouthDrivers(names, curv, grpName):
    mc.group(em=True, n=grpName)
    curvShape = getset.getCrvShape(curv)
    cvs = getset.getCVs(curv)

    for num,cv in enumerate(cvs):
        mc.select(cl=True)
        poc1 = mc.createNode('pointOnCurveInfo')
        mc.connectAttr(curvShape+'.worldSpace[0]', poc1+'.inputCurve', f=True)
        mc.setAttr(poc1+'.turnOnPercentage', 1)
        mc.setAttr(poc1+'.parameter', num/11)
        jnt= mc.joint(rad=.5, n=names[num])
        mc.connectAttr(poc1+'.position', jnt+'.t')
        mc.parent(jnt, grpName)

def lipDrivers(names, pins, ctls, grpName):
    mc.group(em=True, n=grpName)

    for name,pin,ctl in zip(names,pins,ctls):  
        mc.select(cl=True)
        jnt = mc.joint(n=name, rad=.3)
        nul = mc.group(jnt, n=name+'_nul')
        mc.connectAttr(ctl+'_orient.r', nul+'.r')
        mc.connectAttr(pin+'.outputMatrix[0]', nul+'.offsetParentMatrix')
        mc.connectAttr(pin+'.outputMatrix[0]', ctl+'_nul'+'.offsetParentMatrix', force=True)
        util.connectTransform(ctl, jnt)
        mc.parent(nul, grpName)

###   
def createClsGrp(name, targ, bindmeshes, grpName, weights=[]):
    try:mc.select(grpName)
    except: mc.group(em=True, n=grpName)
    
    clus = mc.cluster(bindmeshes)[1]
    clus = mc.rename(clus, name)
    mc.connectAttr(targ+'.worldInverseMatrix', clus+'.offsetParentMatrix')
    mc.disconnectAttr(targ+'.worldInverseMatrix', clus+'.offsetParentMatrix')
    
    nul = mc.group(em=True, n=name+'_nul')
    mc.connectAttr(targ+'.worldMatrix', nul+'.offsetParentMatrix')
    mc.disconnectAttr(targ+'.worldMatrix', nul+'.offsetParentMatrix')
    
    mc.parent(clus, nul, r=True)
    mc.parent(nul ,grpName)
    
    if weights != []:
        for bm,val in zip(bindmeshes,weights):
            mc.select(bm+'.vtx[*]')
            mc.percent( name+'Cluster', v=val ) #set percents on the selected items to each value

        
def createBsCrv(guides, names, grpName):
    if not mc.ls(grpName): mc.group(em=True, n=grpName)

    for guide, name in zip(guides, names):
        upperCrv, lowerCrv = guide
        createMouthCrv(name, upperCrv, lowerCrv)
        mc.parent(name, grpName)

def createBsNode(name, orig, targList):
    bs = mc.blendShape(orig, n=name, o='local')[0] #o is origin
    for num,targ in enumerate(targList):
        mc.blendShape(bs, e=True, t=(orig, num, targ, 1.0))

def setBsCvWeight(bs):
    for i in range(8):
        for j in range(12):
            val=1
            if j in [3,9]: #middle vertex
                val=.5
            elif j in [0,1,2,10,11]: #left side vertex
                if 4<=i: #left side target
                    val=0
            elif j in [4,5,6,7,8]: #right side vertex
                if i<4: #right side target
                    val=0
            mc.setAttr(bs+'.inputTarget[0].inputTargetGroup[%d].targetWeights[%d]'%(i,j), val)
            
            
def symmetricMouthCrv(crvList):
    outList = []
    for crv in crvList:
        CVs = getset.getCVs(crv)
        posList = getset.getTransform(CVs, t=True, r=False, os=True)
        for num,i in enumerate(posList):
            if num<len(CVs)/4:
                x,y,z = i['pos']
                posList[len(CVs)//2-num]['pos'] = (-x,y,z)
            elif len(CVs)*3/4 < num:
                x,y,z = i['pos']
                posList[len(CVs)*3//2-num]['pos'] = (-x,y,z)
        outList += posList
    return outList

def connectBs(ctl, blendCrvs, bs):
    #rBlendCrvs = 
    #[ wideR smallR smileR frownR ]
    #[ 0     1     2      3      4 ]

    clp = mc.createNode('clamp')
    mc.setAttr(clp+'.maxR', 10)
    mc.setAttr(clp+'.minG', -10)
    mc.connectAttr(ctl+'.tx', clp+'.inputR')
    mc.connectAttr(ctl+'.tx', clp+'.inputG')
    mc.connectAttr(clp+'.outputR', bs+'.'+blendCrvs[1])
    
    mul = mc.createNode('multDoubleLinear')
    mc.setAttr(mul+'.input2', -1)
    mc.connectAttr(clp+'.outputG', mul+'.input1')
    mc.connectAttr(mul+'.output', bs+'.'+blendCrvs[0])
    ###
    rng = mc.createNode('setRange')
    mc.setAttr(rng+'.minX', 10)
    mc.setAttr(rng+'.oldMinX', -10)
    mc.setAttr(rng+'.maxY', 10)
    mc.setAttr(rng+'.oldMaxY', 10)
    mc.connectAttr(ctl+'.ty', rng+'.valueX')
    mc.connectAttr(ctl+'.ty', rng+'.valueY')
    mc.connectAttr(rng+'.outValueX', bs+'.'+blendCrvs[3])
    mc.connectAttr(rng+'.outValueY', bs+'.'+blendCrvs[2])
        
    
def matchCrvRtoL(posList):
    #actually, mouth_curve_r_wide & mouth_curve_l_wide are identical.
    #It doesn't mirror, it snaps CV positions
    rPosList = [d for d in posList if '_r_' in d['name']]
    lPosList = [d for d in posList if '_l_' in d['name']]
    for r,l in zip(rPosList, lPosList):
        l['pos'] = r['pos']
    outList = rPosList + lPosList
    return outList

def connectBigClus(C1, P1, P2):
    mm1 = mc.createNode('multMatrix')
    mc.connectAttr(P1+'.matrix', mm1+'.matrixIn[0]')
    mc.connectAttr(P2+'.matrix', mm1+'.matrixIn[1]')
    dm1 = mc.createNode('decomposeMatrix')
    mc.connectAttr(mm1+'.matrixSum', dm1+'.inputMatrix')
    mc.connectAttr(dm1+'.outputTranslate', C1+'.t')
    mc.connectAttr(dm1+'.outputRotate', C1+'.r')

def cornerCtls(ctl, clus, P1, P2):
    auto = ctl+'_auto'
    bm1 = mc.createNode('blendMatrix')
    mc.connectAttr(P2+'.matrix', bm1+'.target[0].targetMatrix')
    mc.connectAttr(P1+'.matrix', bm1+'.inputMatrix')
    mc.setAttr(bm1+'.target[0].weight', .5)
    dm1 = mc.createNode('decomposeMatrix')
    mc.connectAttr(bm1+'.outputMatrix', dm1+'.inputMatrix')
    mc.connectAttr(dm1+'.outputRotate', auto+'.r') #connect ctl auto
    mc.connectAttr(dm1+'.outputRotate', clus+'_nul'+'.r') #connect clus nul
    
    #add corner pin attr
    mc.addAttr(ctl, sn='cornerPin', k=True, dv=0, min=-1, max=1)
    #set range node
    ran1 = mc.createNode('setRange')
    #cornerPin >> valueX
    mc.connectAttr(ctl+'.cornerPin', ran1+'.valueX')
    # minX 0 maxX 1, oldMinX -1 oldMaxX 1
    mc.setAttr(ran1+'.minX', 0)
    mc.setAttr(ran1+'.maxX', 1)
    mc.setAttr(ran1+'.oldMinX', -1)
    mc.setAttr(ran1+'.oldMaxX', 1)
    #outValueX >> face_Lower_bindW0
    mc.connectAttr(ran1+'.outValueX', bm1+'.target[0].weight')




