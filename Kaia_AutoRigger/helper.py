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
        left = ['brow_l_bind', 'sneer_l_bind', 'cheek_upper_l_bind', 'cheek_l_bind', 'cheek_lower_l_bind', 'eye_socket_l_bind']
        right = [d.replace('_l_','_r_') for d in left]

        for lf,rt in zip(left,right):
            pos = mc.getAttr(rt+'.t')[0]
            rot = mc.getAttr(rt+'.r')[0]
            
            mc.setAttr(lf+'.t',-pos[0],pos[1],pos[2],type='double3')
            mc.setAttr(lf+'.r',-rot[0],-rot[1],rot[2],type='double3')
            
            mc.setAttr(rt+'.jointOrient',0,0,0,type='double3')
            mc.setAttr(lf+'.jointOrient',0,180,0,type='double3')
            
            
        cLeft = ['brow_peak_l_bind', 'brow_corrugator_l_bind', 'brow_inner_l_bind', 'nostril_l_bind']
        cRight = [d.replace('_l_','_r_') for d in cLeft]

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