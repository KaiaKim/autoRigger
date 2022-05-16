import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import Builder
from Kaia_AutoRigger import UI
from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import LidFunc
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
importlib.reload(Builder)
importlib.reload(UI)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(LidFunc)
importlib.reload(EyeFunc)
importlib.reload(BrowFunc)

###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigFace(Builder.BuildRig):
    def __init__(self):
        self.usd = cmds.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
        self.mayascripts = '%s/%s' % (self.usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts
        
        self.winTitle = 'Kaia\'s auto rigger' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigFace' #this needs to be ac word that has no spaces or it won't work! #node name
        
        self.verts = {'head':None, 'lipUpper':None, 'lipLower':None, 'lidUpperR':None, 'lidLowerR':None, 'browR':None}
    
    def quickTest(self,_):
        #some hard coded data for quick testing
        self.verts['head']=['face.vtx[0:6959]']
        self.verts['lipUpper']=['face.vtx[3314]', 'face.vtx[3315]', 'face.vtx[3317]', 'face.vtx[3320]', 'face.vtx[3321]', 'face.vtx[3322]', 'face.vtx[3325]', 'face.vtx[3326]', 'face.vtx[3327]', 'face.vtx[3331]', 'face.vtx[3332]', 'face.vtx[3335]', 'face.vtx[3337]', 'face.vtx[3495]', 'face.vtx[3818]', 'face.vtx[4010]', 'face.vtx[4200]', 'face.vtx[4386]', 'face.vtx[4574]', 'face.vtx[4751]', 'face.vtx[4918]', 'face.vtx[5079]', 'face.vtx[5215]', 'face.vtx[5350]', 'face.vtx[5485]', 'face.vtx[5620]', 'face.vtx[5741]']
        self.verts['lipLower']=['face.vtx[3313]', 'face.vtx[3316]', 'face.vtx[3318]', 'face.vtx[3319]', 'face.vtx[3323]', 'face.vtx[3324]', 'face.vtx[3327]', 'face.vtx[3328]', 'face.vtx[3329]', 'face.vtx[3330]', 'face.vtx[3333]', 'face.vtx[3334]', 'face.vtx[3336]', 'face.vtx[3494]', 'face.vtx[3729]', 'face.vtx[3950]', 'face.vtx[4144]', 'face.vtx[4334]', 'face.vtx[4526]', 'face.vtx[4707]', 'face.vtx[4878]', 'face.vtx[5043]', 'face.vtx[5183]', 'face.vtx[5322]', 'face.vtx[5461]', 'face.vtx[5600]', 'face.vtx[5741]']
        self.verts['lidUpperR']=['face.vtx[6251]', 'face.vtx[6252]', 'face.vtx[6253]', 'face.vtx[6254]', 'face.vtx[6255]', 'face.vtx[6256]', 'face.vtx[6257]', 'face.vtx[6258]', 'face.vtx[6259]', 'face.vtx[6260]', 'face.vtx[6261]', 'face.vtx[6262]', 'face.vtx[6263]', 'face.vtx[6264]', 'face.vtx[6266]', 'face.vtx[6306]', 'face.vtx[6347]']
        self.verts['lidLowerR']=['face.vtx[6239]', 'face.vtx[6240]', 'face.vtx[6241]', 'face.vtx[6242]', 'face.vtx[6243]', 'face.vtx[6244]', 'face.vtx[6245]', 'face.vtx[6246]', 'face.vtx[6247]', 'face.vtx[6248]', 'face.vtx[6249]', 'face.vtx[6250]', 'face.vtx[6251]', 'face.vtx[6277]', 'face.vtx[6313]', 'face.vtx[6347]', 'face.vtx[6348]']
        self.verts['browR']=['face.vtx[5388]']
        
    def assignDelete(self,data,flag):
        if flag=='ass':
            if data == 'head': self.verts['head']=cmds.ls(sl=True)
            else: self.verts[data]=cmds.ls(sl=True,fl=True)
            
        elif flag=='sel':
            cmds.select(self.verts[data])

        elif flag=='del':
            self.verts[data]=None


    def orientData(self,flag=''):
        if flag=='load':
            #read json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/ctlOrient.json',"r") as rfile:
                data = json.load(rfile)
        
        if flag=='mirror' or flag=='save':
            #get transform
            orients = [d+'_orient' for d in self.allCtls]
            data = ModFunc._getTransformData(orients, t=False, r=True)
        
        if flag=='mirror':
            #modify data
            rightData = [d for d in data if '_r_' in d['name']]
            mirrorData = rightData
            for i in mirrorData:
                i['name'] = i['name'].replace('_r_','_l_')
                (rx,ry,rz) = i['rot']
                
                if 'blink' in i['name']:
                    i['rot'] = (-rx,-ry, rz)
                else:
                    i['rot'] = (rx,-ry,-rz)
                
            ModFunc._applyTransformData(mirrorData)

        if flag=='load':
            #apply transform
            ModFunc._applyTransformData(data)
        
        if flag=='save':
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/ctlOrient.json', "w") as wfile:
                json.dump(data, wfile)


    def latticeData(self,flag=''): #mirror lattice point pos
        if flag=='load':
            #read json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/latticePtPos.json',"r") as rfile:
                ptPos = json.load(rfile)
        
        if flag=='mirror' or flag=='save':
            #get transform
            ltsPt = cmds.ls(self.eyeballRLtc + 'Lattice.pt[*][*][*]', fl=1)
            ptPos = ModFunc._getTransformData(ltsPt, t=True, r=False, ws=True)
        
        if flag=='mirror':
            #modify data
            mirrorPos = ptPos
            for i in mirrorPos:
                i['name'] = i['name'].replace('_r_','_l_')
                x,y,z = i['pos']
                i['pos'] = (-x,y,z)
            ModFunc._applyTransformData(mirrorPos)
        
        if flag=='load':
            #apply transform
            ModFunc._applyTransformData(ptPos, ws=True)
        
        if flag=='save':    
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/latticePtPos.json', "w") as wfile:
                json.dump(ptPos, wfile)
                
    def blendCrvData(self,flag=''):
        if flag=='load':
            #read json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/blendCrv.json',"r") as rfile:
                cvPos = json.load(rfile)
        
        if flag=='save':
            #get transform
            allCrv = self.mouthBlendCrvs + self.eyeRBlendCrvs + self.eyeLBlendCrvs
            allCVs = []
            for i in allCrv:
                CVs = ModFunc._getCVs(i)
                allCVs += CVs
            cvPos = ModFunc._getTransformData(allCVs, t=True, r=False, os=True)

        if flag=='load':
            #apply transform
            ModFunc._applyTransformData(cvPos, os=True)
        
        if flag=='save':    
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/blendCrv.json', "w") as wfile:
                json.dump(cvPos, wfile)
                
    def mirrorBlendCrvMouth(self,_):
        #modify data mouth
        cvPos2 = MouthFunc._symmetricMouthCrv(self.mouthBlendCrvs)
        ModFunc._applyTransformData(cvPos2, os=True)
        cvPos3 = MouthFunc._matchCrvRtoL(cvPos2)
        ModFunc._applyTransformData(cvPos3, os=True)
        
    def mirrorBlendCrvEyes(self,_):
        #modify data eyes
        allCVs = []
        for i in self.eyeRBlendCrvs+self.eyeLBlendCrvs:
            CVs = ModFunc._getCVs(i)
            allCVs += CVs
            
        cvPos = ModFunc._getTransformData(allCVs, t=True, r=False, os=True)
        cvPos5 = LidFunc._mirrorCVs(cvPos)
        ModFunc._applyTransformData(cvPos5, os=True)

        
    def enterOrientEdit(self,_):
        print('### enter orient edit mode ###')
        ###lip ctrl
        #unparent lipCvClsoffset from lip ctrl
        for clus in self.lipCvCls:
            cmds.parent(clus+'_offset', w=True) #parent to world

        ###mouth ctrl
        #delete parent constraint of jaw clusters
        #delete parent constraint of lip ctrl nuls
        
        ###mCorner ctrl
        #don't need anything

    
    def exitOrientEdit(self,_):
        print('### exit orient edit mode ###')
        for ctl,clus in zip(self.lipCtls,self.lipCvCls):
            cmds.parent(clus+'_offset',ctl)


    def changeCornerN(self,x,y,z):
        ModFunc._normalizeCtls(self.mCornerCtls,val=(x,y,z))
        
    def changeLipPull(self,one,two):
        for i in self.mCornerCtls:
            cmds.setAttr(i+'.lipOnePull', one)
            cmds.setAttr(i+'.lipTwoPull', two)

        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run01=AutoRigFace()
UI.createWindow(run01)

###DQ skin > attibute editor > support Non-rigid transformation ON
