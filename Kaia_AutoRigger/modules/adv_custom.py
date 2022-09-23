import maya.cmds as mc
###----------------------GLOBAL VARIABLES------------------------
def deleteExtra():
    faceFKctls = ['FKOffsetJaw_M','FKAimEye_R','FKAimEye_L']
    eyeAim = 'AimSystem'
    facebinds = ['EyeEnd_L', 'Eye_L', 'JawEnd_M', 'Jaw_M', 'EyeEnd_R', 'Eye_R']

    mc.delete(faceFKctls)
    mc.delete(eyeAim)
    mc.delete(facebinds)

def connectFaceToBody(faceRoot):
    const1 = mc.parentConstraint('FKHead_M', faceRoot, mo=True)[0]
    mc.setAttr(const1+'.interpType', 2) #shortest

if __name__ == "__main__":
    deleteExtra()
