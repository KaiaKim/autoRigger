import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

###-----------------------------------------------------FUNCTION---------------------------------------------------
def _createDrivCrv(names,origs):
    for orig,name in zip(origs,names):
        cmds.duplicate(orig,n=name)
        cmds.rebuildCurve(name,d=1,kcp=True)

def _createDrivJnts(names,curv):
    jntList = []
    curvShape = ModFunc._getCrvShape(curv)
    cvs = ModFunc._getCVs(curv)

    for name,cv in zip(names,cvs):
        cmds.select(cl=True)
        jnt= cmds.joint(rad=.3,n=name)
        pos = cmds.xform(cv,q=True,ws=True,t=True) 
        cmds.move(pos[0],pos[1],pos[2],jnt)
        jntList.append(jnt)


def _attachLidCtls(ctls,crv):
    crvShape = ModFunc._getCrvShape(crv)

    for num,ctl in enumerate(ctls):
        nul=ctl+'_nul'
        poc1 = cmds.createNode('pointOnCurveInfo')
        cmds.connectAttr(crvShape+'.worldSpace[0]', poc1+'.inputCurve', f=True)
        cmds.setAttr(poc1 + '.parameter',num)
        cmds.connectAttr(poc1+'.position', nul+'.t')


def _skinCrv(jnts,crv):
    cmds.select(jnts,crv)
    cmds.skinCluster(maximumInfluences=1)

def _createBsCrv(crvs,names,grpName):
    grp = cmds.group(em=True,n=grpName)
    
    for name in names:
        if 'upper' in name:
            orig = crvs[0]
        elif 'lower' in name:
            orig = crvs[1]
        
        if ('upper' in name and'neutral' in name) or ('lower' in name and'closed' in name): #lower_closed = upper_neut = upper_orig
            orig = crvs[0]
        if ('lower' in name and'neutral' in name) or ('upper' in name and 'closed' in name): #upper_closed = lower_neut = lower_ orig
            orig = crvs[1]

        dup = cmds.duplicate(orig,n=name)
        cmds.parent(dup, grp)



def _createBsNode(nodes,crvs,targList):
    for node in nodes:
        if 'upper' in node: x=0
        elif 'lower' in node: x=1
        orig=crvs[x]
        cmds.blendShape(orig, n=node, o='local')
        if '_open' in node:
            cmds.blendShape(node, e=True, t=(orig, 1, targList[0+4*x], 1.0))
            cmds.setAttr(node+'.'+targList[0+4*x],1)
        elif '_closed' in node:
            #print('_closedTarget:',targList[3+4*x])
            cmds.blendShape(node, e=True, t=(orig, 1, targList[3+4*x], 1.0))
            cmds.blendShape(node, e=True, ib=True, t=(orig, 1, targList[1+4*x], 0.333))
            cmds.blendShape(node, e=True, ib=True, t=(orig, 1, targList[2+4*x], 0.666))
            

            
def _connectCornerCtrl(blinkCtls, blendCrvs, bsNodes):
        #upper closed
    #set driven key node1
    sdk1 = cmds.setDrivenKeyframe( bsNodes[1]+'.'+blendCrvs[3], cd=blinkCtls[0]+'.rx' )
    sdk1 = bsNodes[1]+'_'+blendCrvs[3]
        #lower closed
    #reverse node
    rev = cmds.createNode('reverse')
    #addDoubleLinear node
    addDou = cmds.createNode('addDoubleLinear')
    #clamp node
    clmp = cmds.createNode('clamp')
    
    #set driven key node2
    sdk2 = cmds.setDrivenKeyframe(clmp+'.inputR', cd=blinkCtls[1]+'.rx')
    sdk2 = clmp+'_'+'inputR'
    
    #driven1 output >> reverse inputX
    cmds.connectAttr(sdk1+'.output',rev+'.inputX')
    #reverse outputX >> addDoubleLinear input1
    cmds.connectAttr(rev+'.outputX',addDou+'.input1')
    #addDoubleLinear input2, 0.333
    cmds.setAttr(addDou+'.input2',0.333)
    #addDoubleLinear output >> clamp maxR
    cmds.connectAttr(addDou+'.output',clmp+'.maxR')
    #clamp outputR >> blend weight lower_lid_l_closed_curve
    cmds.connectAttr( clmp+'.outputR', bsNodes[3]+'.'+ blendCrvs[7] )
    
    ###
    cmds.keyframe(sdk1,index=(0,0),a=True,fc=-20,vc=0)
    cmds.setKeyframe(sdk1,i=True,f=0)
    cmds.setKeyframe(sdk1,i=True,f=40)
    cmds.keyframe(sdk1,index=(1,1),a=True,vc=1/3)
    cmds.keyframe(sdk1,index=(2,2),a=True,vc=1)

    cmds.keyTangent(sdk1,index=(0,2),itt="spline",ott="spline")

    cmds.setAttr(sdk1+'.preInfinity',1)
    cmds.setAttr(sdk1+'.postInfinity',1)
    
    ###
    cmds.keyframe(sdk2,index=(0,0),a=True,fc=-20,vc=0)
    cmds.setKeyframe(sdk2,i=True,f=0)
    cmds.setKeyframe(sdk2,i=True,f=40)
    cmds.keyframe(sdk2,index=(1,1),a=True,vc=1/3)
    cmds.keyframe(sdk2,index=(2,2),a=True,vc=1)

    cmds.keyTangent(sdk2,index=(0,2),itt="spline",ott="spline")

    cmds.setAttr(sdk2+'.preInfinity',1)
    cmds.setAttr(sdk2+'.postInfinity',1)


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