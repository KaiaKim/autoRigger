import maya.cmds as mc
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

def _createDrv(drvs,targs,parent):
    for drv,targ in zip(drvs,targs):
        mc.group(em=True,w=True,n=drv)
        mc.connectAttr(targ+'.worldMatrix',drv+'.offsetParentMatrix')
        mc.disconnectAttr(targ+'.worldMatrix',drv+'.offsetParentMatrix')

        mc.parent(drv,parent)
        mc.makeIdentity(drv,apply=True,t=1)
        
        mc.pointConstraint(targ,drv,mo=False)

def _connectCtls(ctls,cornerCtls,val):
    for ctl,cornerCtl in zip(ctls,cornerCtls):
        auto = ctl + '_auto'
        mult1 = mc.createNode('multiplyDivide',n=ctl+'_mult')
        mc.connectAttr(cornerCtl+'.t',mult1+'.input1')
        mc.setAttr(mult1+'.input2',val[0],val[1],val[2],type='double3')
        mc.connectAttr(mult1+'.output',auto+'.t')
        
def _connectBinds(ctls,binds):
    for ctl,bind in zip(ctls,binds):
        mult1 = ctl+'_mult'
        col1 = mc.createNode('colorMath')
        mc.connectAttr(ctl+'.t',col1+'.colorA')
        mc.connectAttr(mult1+'.output',col1+'.colorB')
        mc.connectAttr(col1+'.outColor',bind+'.t')