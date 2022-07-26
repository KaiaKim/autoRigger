###functions about get, set, mirror

import maya.cmds as mc

###---------------------------------------------------------------------------------------------------
def getCrvShape(crv):
    return mc.listRelatives(crv, type='nurbsCurve')[0]

def getCVs(crv):
    return mc.ls(crv + '.cv[*]', fl=1)

def getTransform(inList, t=False, r=False, ws=False, os=False):
    outData = []
    for i in inList:
        if mc.ls(i)==[]: continue #If the node doesn't exist, we keep looping
        
        dic = {'name':i}
        if t==True:
            dic['pos'] = mc.xform(i, q=True, ws=ws, os=os, t=True)
        if r==True:
            dic['rot'] = mc.getAttr(i+'.r')[0]

        outData.append(dic)
    return tuple(outData)

def applyTransform(inData, ws=False, os=False):
    for i in inData:
        if mc.ls(i['name'])==[]: continue
        
        if 'pos' in i:
            pos = i['pos']
            mc.move(pos[0], pos[1], pos[2], i['name'], ws=ws, os=os)
        if 'rot' in i: 
            rot = i['rot']
            mc.rotate(rot[0], rot[1], rot[2], i['name'])
        if 'scl' in i:
            scl = i['scl']
            mc.scale(scl[0], scl[1], scl[2], i['name'])
            
def mirrorObj(name,right):
    left = mc.duplicate(right, n=name)[0]
    mc.scale(-1, 1, 1, left)
    mc.makeIdentity(left, apply=True)
    mc.delete(left, constructionHistory=True)

def mirrorPosX(posList):
    mirList = []
    for pos in posList:
        x,y,z = pos
        mirList.append((-x,y,z))
    return mirList
         