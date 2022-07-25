import maya.cmds as mc

def _getTransform(inList, t=False, r=False, ws=False, os=False):
    outData = []
    for i in inList:
        if mc.ls(i)==[]:continue #If the node doesn't exist, we keep looping
        
        dic = {'name':i}
        if t==True:
            dic['pos'] = mc.xform(i, q=True, ws=ws, os=os, t=True)
        if r==True:
            dic['rot'] = mc.getAttr(i+'.r')[0]

        outData.append(dic)
    return tuple(outData)

def _applyTransform(inData, ws=False, os=False):
    for i in inData:
        if mc.ls(i['name'])==[]:continue #If the node doesn't exist, we keep looping
        
        if 'pos' in i:
            pos = i['pos']
            mc.move(pos[0],pos[1],pos[2],i['name'], ws=ws, os=os)
        if 'rot' in i: 
            rot = i['rot']
            mc.rotate(rot[0],rot[1],rot[2],i['name'])
        if 'scl' in i:
            scl = i['scl']
            mc.scale(scl[0],scl[1],scl[2],i['name'])
         