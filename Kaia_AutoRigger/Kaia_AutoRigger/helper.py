import maya.cmds as mc
import importlib

from Kaia_AutoRigger.modules import util
from Kaia_AutoRigger.modules import getset
from Kaia_AutoRigger.modules import mouth
from Kaia_AutoRigger.modules import lid

importlib.reload(util)
importlib.reload(mouth)
importlib.reload(getset)
importlib.reload(lid)

class HelpExtra():
    def __init__(self):
        pass
    
    def mirrorGuide(self):
        left = [self.B.bigBinds[1], self.N.sneerBinds[1], self.C.binds[1], self.C.binds[3], self.C.binds[5], self.E.socBinds[1]]
        right = [self.B.bigBinds[0], self.N.sneerBinds[0], self.C.binds[0], self.C.binds[2], self.C.binds[4], self.E.socBinds[0]]

        for lf,rt in zip(left,right):
            pos = mc.getAttr(rt+'.t')[0]
            rot = mc.getAttr(rt+'.r')[0]
            
            mc.setAttr(lf+'.t',-pos[0],pos[1],pos[2],type='double3')
            mc.setAttr(lf+'.r',-rot[0],-rot[1],rot[2],type='double3')
            
            mc.setAttr(rt+'.jointOrient',0,0,0,type='double3')
            mc.setAttr(lf+'.jointOrient',0,180,0,type='double3')
            

        cLeft = [self.B.peakBinds[1], self.B.corBinds[1], self.B.inBinds[1], self.N.nostrilBinds[1]]
        cRight = [self.B.peakBinds[0], self.B.corBinds[0], self.B.inBinds[0], self.N.nostrilBinds[0]]

        for lf,rt in zip(cLeft,cRight):
            pos = mc.getAttr(rt+'.t')[0]
            rot = mc.getAttr(rt+'.r')[0]
            
            mc.setAttr(lf+'.t',pos[0],pos[1],-pos[2],type='double3')
            mc.setAttr(lf+'.r',-rot[0],-rot[1],rot[2],type='double3')
    
    
    def mirrorCtlOrient(self,_):
        #get transform
        orients = [d+'_orient' for d in self.allCtls]
        self.data['orients'] = getset.getTransform(orients, t=False, r=True)

        #modify data
        rightData = [d for d in self.data['orients'] if '_r_' in d['name']]
        mirrorData = rightData
        for i in mirrorData:
            i['name'] = i['name'].replace('_r_','_l_')
            (rx,ry,rz) = i['rot']
            if 'blink' in i['name']:
                i['rot'] = (-rx,-ry, rz)
            else:
                i['rot'] = (rx,-ry,-rz)
            
        getset.applyTransform(mirrorData)
            
    def mirrorBlendCrvMouth(self,_):
        #modify data mouth
        cvPos2 = mouth.symmetricMouthCrv(self.M.blendCrvs)
        #print('cvPos2:',cvPos2)
        getset.applyTransform(cvPos2, os=True)
        cvPos3 = mouth.matchCrvRtoL(cvPos2)
        getset.applyTransform(cvPos3, os=True)
        
    def mirrorBlendCrvEyes(self,_):
        #modify data eyes
        allCVs = []
        for i in self.L.rBlendCrvs + self.L.lBlendCrvs:
            CVs = getset.getCVs(i)
            allCVs += CVs
            
        cvPos = getset.getTransform(allCVs, t=True, r=False, os=True)
        cvPos5 = getset.mirrorCVs(cvPos)
        getset.applyTransform(cvPos5, os=True)