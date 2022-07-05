import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

def LocsOnVert(inVert):
    locR = cmds.spaceLocator()[0]
    locL = cmds.spaceLocator()[0]
    posR = cmds.xform(inVert,q=True,t=True,ws=True)
    cmds.move(posR[0],posR[1],posR[2],locR)
    cmds.move(-(posR[0]),posR[1],posR[2],locL)
    return [locR,locL]
    
def _createCompenGrp(targs):
    outList = []
    for targ in targs:
        compen = cmds.group(em=True, p=targ, n=targ+'_orientCompensate')
        const = cmds.parentConstraint(targ,compen,mo=False)
        cmds.delete(const)
        outList.append(compen)
    return outList
    
def _createFollowAttr(ctls):
    for ctl in ctls:
        cmds.addAttr(ctl, sn='followY', at='double3')
        cmds.addAttr(ctl, sn='followYX', at='double',p='followY',dv=0,k=True)
        cmds.addAttr(ctl, sn='followYY', at='double',p='followY',dv=0,k=True)
        cmds.addAttr(ctl, sn='followYZ', at='double',p='followY',dv=0,k=True)
        
        cmds.addAttr(ctl, sn='followZ', at='double3')
        cmds.addAttr(ctl, sn='followZX', at='double',p='followZ',dv=0,k=True)
        cmds.addAttr(ctl, sn='followZY', at='double',p='followZ',dv=0,k=True)
        cmds.addAttr(ctl, sn='followZZ', at='double',p='followZ',dv=0,k=True)

def _createLocalDrv(ctls,drvs,pos,parents):
    for ctl,drv,par in zip(ctls,drvs,parents):
        cmds.group(n=drv,em=True)
        cmds.group(drv,n=drv+'_nul')
        cmds.move(pos[0],pos[1],pos[2],drv+'_nul')
        cmds.parent(drv+'_nul',par)

def _createDrv(ctls,drvs,pos,parent):
    for ctl,drv in zip(ctls,drvs):
        yGrp = cmds.group(n=drv+'Y',em=True)
        zGrp = cmds.group(yGrp,n=drv+'Z')
        cmds.group(zGrp,n=drv+'_nul')
        cmds.move(pos[0],pos[1],pos[2],drv+'_nul')
        cmds.parent(drv+'_nul',parent)
        
def _connectBrowCtls(ctls,ldrvs,drvs,binds,worldUpperObj):
    for ctl,ldrv,drv,bind in zip(ctls,ldrvs,drvs,binds):
        '''
        cmds.pointConstraint(ctl,ldrv)
        cmds.aimConstraint(ldrv,drv+'Y',wuo=worldUpperObj,mo=True)
        '''
        #FollowZ
        mudi1 = cmds.createNode('multiplyDivide')
        cmds.connectAttr(ldrv+'.tz',mudi1+'.input1X')
        cmds.connectAttr(ldrv+'.tz',mudi1+'.input1Y')
        cmds.connectAttr(ldrv+'.tz',mudi1+'.input1Z')
        cmds.connectAttr(ctl+'.followZ',mudi1+'.input2')
        cmds.connectAttr(mudi1+'.output',drv+'Z'+'.t')
        
        #FollowY
        mudi2 = cmds.createNode('multiplyDivide')
        cmds.connectAttr(ldrv+'.ty',mudi2+'.input1X')
        cmds.connectAttr(ldrv+'.ty',mudi2+'.input1Y')
        cmds.connectAttr(ldrv+'.ty',mudi2+'.input1Z')
        cmds.connectAttr(ctl+'.followY',mudi2+'.input2')            
        cmds.connectAttr(mudi2+'.output',drv+'Y'+'.t')
        
        cmds.parentConstraint(drv+'Y',bind)
        