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