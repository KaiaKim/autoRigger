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
        cvPos2 = mouth._symmetricMouthCrv(self.M.blendCrvs)
        #print('cvPos2:',cvPos2)
        getset.applyTransform(cvPos2, os=True)
        cvPos3 = mouth._matchCrvRtoL(cvPos2)
        getset.applyTransform(cvPos3, os=True)
        
    def mirrorBlendCrvEyes(self,_):
        #modify data eyes
        allCVs = []
        for i in self.L.rBlendCrvs + self.L.lBlendCrvs:
            CVs = util.getCVs(i)
            allCVs += CVs
            
        cvPos = getset.getTransform(allCVs, t=True, r=False, os=True)
        cvPos5 = LidFunc._mirrorCVs(cvPos)
        getset.applyTransform(cvPos5, os=True)