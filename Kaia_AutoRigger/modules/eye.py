import maya.cmds as mc
import importlib

from . import util
importlib.reload(util)

###-----------------------------------------------------FUNCTION---------------------------------------------------
def connectEyeCtls(ctls, rotCtl, aimCtl, aimMicroCtls, binds):
    for i,ctl in enumerate(ctls):
        convGrp = mc.group(em=True,p=ctl+'_nul',n=ctl+'_converge')
        rotGrp = mc.group(convGrp, n=ctl+'_rot')
        aimGrp = mc.group(rotGrp, n=ctl+'_aim')
        mc.parent(ctl+'_orient',convGrp)
        '''
        #connectBind
        mc.parentConstraint(ctl, binds[i], mo=True)
        mc.scaleConstraint(ctl, binds[i], mo=False)
        '''
        #connectRotCtl
        mc.connectAttr(rotCtl+'.r',rotGrp+'.r')
        #connectMicroAim
        mc.aimConstraint(aimMicroCtls[i],aimGrp,mo=True)
        
    #connectConverge
    mc.addAttr(aimCtl, shortName='converge', keyable=True, defaultValue=0, minValue=-2, maxValue=2)
    
    mul = mc.createNode('multDoubleLinear')
    mc.connectAttr(aimCtl+'.converge',mul+'.input1')
    mc.setAttr(mul+'.input2',20)
    
    mudi = mc.createNode('multiplyDivide')
    mc.connectAttr(mul+'.output',mudi+'.input1X')
    mc.connectAttr(mul+'.output',mudi+'.input1Y')
    mc.setAttr(mudi+'.input2X',1)
    mc.setAttr(mudi+'.input2Y',-1)
    
    mc.connectAttr(mudi+'.outputX',ctls[0]+'_converge'+'.ry')
    mc.connectAttr(mudi+'.outputY',ctls[1]+'_converge'+'.ry')
    
    