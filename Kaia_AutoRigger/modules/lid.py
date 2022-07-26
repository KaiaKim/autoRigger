import maya.cmds as mc
import importlib

from . import util
importlib.reload(util)

###-----------------------------------------------------FUNCTION---------------------------------------------------
def _createDrivCrv(name,orig):
        mc.duplicate(orig,n=name)
        mc.rebuildCurve(name,d=1,kcp=True)

def _createBlinkDrivers(names,curv,grpName):
    try:mc.select(grpName)
    except: mc.group(em=True, n=grpName)
    curvShape = util.getCrvShape(curv)
    cvs = util.getCVs(curv)

    for num,cv in enumerate(cvs):
        poc1 = mc.createNode('pointOnCurveInfo')
        mc.connectAttr(curvShape+'.worldSpace[0]', poc1+'.inputCurve', f=True)
        mc.setAttr(poc1+'.turnOnPercentage',1)
        mc.setAttr(poc1 + '.parameter', num/4)
        loc= mc.spaceLocator(n=names[num])[0]
        util.localScaleLoc(loc,.3)
        mc.connectAttr(poc1+'.position', loc+'.t')
        mc.parent(loc,grpName)


def _createlidDrivers(names,locs,ctls,grpName):
    try:mc.select(grpName)
    except: mc.group(em=True, n=grpName)
    
    for name,loc,ctl in zip(names,locs,ctls): #0,1,2,3,4
        mc.select(cl=True)
        jnt= mc.joint(rad=.3,n=name)
        mc.connectAttr(loc+'.xformMatrix',jnt+'.offsetParentMatrix')
        util.connectTransform (ctl,jnt)
        
        mc.parent(jnt,grpName)




def _createBsCrv(crvs,names,grpName):
    grp = mc.group(em=True,n=grpName)
    
    for name in names:
        if 'upper' in name:
            orig = crvs[0]
        elif 'lower' in name:
            orig = crvs[1]
        
        if ('upper' in name and'neutral' in name) or ('lower' in name and'closed' in name): #lower_closed = upper_neut = upper_orig
            orig = crvs[0]
        if ('lower' in name and'neutral' in name) or ('upper' in name and 'closed' in name): #upper_closed = lower_neut = lower_ orig
            orig = crvs[1]

        dup = mc.duplicate(orig,n=name)
        mc.parent(dup, grp)



def _createBsNode(nodes,crvs,targList):
    for node in nodes:
        if 'upper' in node: x=0
        elif 'lower' in node: x=1
        orig=crvs[x]
        mc.blendShape(orig, n=node, o='local')
        if '_open' in node:
            mc.blendShape(node, e=True, t=(orig, 1, targList[0+4*x], 1.0))
            mc.setAttr(node+'.'+targList[0+4*x],1)
        elif '_closed' in node:
            #print('_closedTarget:',targList[3+4*x])
            mc.blendShape(node, e=True, t=(orig, 1, targList[3+4*x], 1.0))
            mc.blendShape(node, e=True, ib=True, t=(orig, 1, targList[1+4*x], 0.333))
            mc.blendShape(node, e=True, ib=True, t=(orig, 1, targList[2+4*x], 0.666))
            
            
def _connectBs(blinkCtls, blendCrvs, bsNodes):
        #upper closed
    #set driven key node1
    sdk1 = mc.setDrivenKeyframe( bsNodes[1]+'.'+blendCrvs[3], cd=blinkCtls[0]+'.rx' )
    sdk1 = bsNodes[1]+'_'+blendCrvs[3]
        #lower closed
    #reverse node
    rev = mc.createNode('reverse')
    #addDoubleLinear node
    addDou = mc.createNode('addDoubleLinear')
    #clamp node
    clmp = mc.createNode('clamp')
    
    #set driven key node2
    sdk2 = mc.setDrivenKeyframe(clmp+'.inputR', cd=blinkCtls[1]+'.rx')
    sdk2 = clmp+'_'+'inputR'
    
    #driven1 output >> reverse inputX
    mc.connectAttr(sdk1+'.output',rev+'.inputX')
    #reverse outputX >> addDoubleLinear input1
    mc.connectAttr(rev+'.outputX',addDou+'.input1')
    #addDoubleLinear input2, 0.333
    mc.setAttr(addDou+'.input2',0.333)
    #addDoubleLinear output >> clamp maxR
    mc.connectAttr(addDou+'.output',clmp+'.maxR')
    #clamp outputR >> blend weight lower_lid_l_closed_curve
    mc.connectAttr( clmp+'.outputR', bsNodes[3]+'.'+ blendCrvs[7] )
    
    ###
    mc.keyframe(sdk1,index=(0,0),a=True,fc=-20,vc=0)
    mc.setKeyframe(sdk1,i=True,f=0)
    mc.setKeyframe(sdk1,i=True,f=40)
    mc.keyframe(sdk1,index=(1,1),a=True,vc=1/3)
    mc.keyframe(sdk1,index=(2,2),a=True,vc=1)

    mc.keyTangent(sdk1,index=(0,2),itt="spline",ott="spline")

    mc.setAttr(sdk1+'.preInfinity',1)
    mc.setAttr(sdk1+'.postInfinity',1)
    
    ###
    mc.keyframe(sdk2,index=(0,0),a=True,fc=-20,vc=0)
    mc.setKeyframe(sdk2,i=True,f=0)
    mc.setKeyframe(sdk2,i=True,f=40)
    mc.keyframe(sdk2,index=(1,1),a=True,vc=1/3)
    mc.keyframe(sdk2,index=(2,2),a=True,vc=1)

    mc.keyTangent(sdk2,index=(0,2),itt="spline",ott="spline")

    mc.setAttr(sdk2+'.preInfinity',1)
    mc.setAttr(sdk2+'.postInfinity',1)


def _mirrorCVs(posList):
    rPos = [d for d in posList if '_r_' in d['name']]
    lPos = [d for d in posList if '_l_' in d['name']]
    for r,l in zip(rPos,lPos):
        x,y,z = r['pos']
        l['pos']=(-x,y,z)
    outList = rPos+lPos
    return outList
    
def _createLoftBall():
    pass
    
def _SlideOnSurface():
    pass