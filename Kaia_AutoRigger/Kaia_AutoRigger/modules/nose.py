import maya.cmds as mc
import importlib

from . import util
importlib.reload(util)

def connectNoseFollow(ctl, bind, P1):
    #noseFollow attribute
    mc.addAttr(ctl, sn='noseFollow', k=True, dv=.5, min=0, max=1)
    
    mult1=mc.createNode('multiplyDivide')
    mc.connectAttr(P1+'.r', mult1+'.input1')
    mc.connectAttr(ctl+'.noseFollow', mult1+'.input2X')
    mc.connectAttr(ctl+'.noseFollow', mult1+'.input2Y')
    mc.connectAttr(ctl+'.noseFollow', mult1+'.input2Z')
    col1=mc.createNode('colorMath')
    mc.connectAttr(ctl+'.r', col1+'.colorA')
    mc.connectAttr(mult1+'.output', col1+'.colorB')
    mc.connectAttr(col1+'.outColor', bind+'.r')
    
    ###You would create another blend color node to connect translate