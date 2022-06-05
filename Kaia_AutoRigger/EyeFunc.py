import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

###-----------------------------------------------------FUNCTION---------------------------------------------------
def _connectEyeCtls(ctls, rotCtl, aimCtl, aimMicroCtls, binds):
    for i,ctl in enumerate(ctls):
        convGrp = cmds.group(em=True,p=ctl+'_nul',n=ctl+'_converge')
        rotGrp = cmds.group(convGrp, n=ctl+'_rot')
        aimGrp = cmds.group(rotGrp, n=ctl+'_aim')
        cmds.parent(ctl+'_orient',convGrp)
        #connectBind
        cmds.parentConstraint(ctl, binds[i], mo=True)
        cmds.scaleConstraint(ctl, binds[i], mo=False)
        #connectRotCtl
        cmds.connectAttr(rotCtl+'.r',rotGrp+'.r')
        #connectMicroAim
        cmds.aimConstraint(aimMicroCtls[i],aimGrp,mo=True)
        
    #connectConverge
    cmds.addAttr(aimCtl, shortName='converge', keyable=True, defaultValue=0, minValue=-2, maxValue=2)
    
    mul = cmds.createNode('multDoubleLinear')
    cmds.connectAttr(aimCtl+'.converge',mul+'.input1')
    cmds.setAttr(mul+'.input2',20)
    
    mudi = cmds.createNode('multiplyDivide')
    cmds.connectAttr(mul+'.output',mudi+'.input1X')
    cmds.connectAttr(mul+'.output',mudi+'.input1Y')
    cmds.setAttr(mudi+'.input2X',1)
    cmds.setAttr(mudi+'.input2Y',-1)
    
    cmds.connectAttr(mudi+'.outputX',ctls[0]+'_converge'+'.ry')
    cmds.connectAttr(mudi+'.outputY',ctls[1]+'_converge'+'.ry')
    
    