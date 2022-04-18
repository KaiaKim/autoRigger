import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import Builder
from Kaia_AutoRigger import UI
from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
importlib.reload(Builder)
importlib.reload(UI)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(EyeFunc)
importlib.reload(BrowFunc)

###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigFace(Builder.BuildRig):
    def __init__(self):
        self.usd = cmds.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
        self.mayascripts = '%s/%s' % (self.usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts
        
        self.winTitle = 'Kaia\'s auto rigger' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigFace' #this needs to be ac word that has no spaces or it won't work! #node name
    
        self.headVerts = None
        self.lipUpperVerts = None
        self.lipLowerVerts = None
        self.lidUpperRVerts = None
        self.lidLowerRVerts = None
        
    def quickTest(self,_):
        #some hard coded data for quick testing
        self.headVerts=['forBody.vtx[0:6959]']
        self.lipUpperVerts=['forBody.vtx[3314]', 'forBody.vtx[3315]', 'forBody.vtx[3317]', 'forBody.vtx[3320]', 'forBody.vtx[3321]', 'forBody.vtx[3322]', 'forBody.vtx[3325]', 'forBody.vtx[3326]', 'forBody.vtx[3327]', 'forBody.vtx[3331]', 'forBody.vtx[3332]', 'forBody.vtx[3335]', 'forBody.vtx[3337]', 'forBody.vtx[3495]', 'forBody.vtx[3818]', 'forBody.vtx[4010]', 'forBody.vtx[4200]', 'forBody.vtx[4386]', 'forBody.vtx[4574]', 'forBody.vtx[4751]', 'forBody.vtx[4918]', 'forBody.vtx[5079]', 'forBody.vtx[5215]', 'forBody.vtx[5350]', 'forBody.vtx[5485]', 'forBody.vtx[5620]', 'forBody.vtx[5741]']
        self.lipLowerVerts=['forBody.vtx[3313]', 'forBody.vtx[3316]', 'forBody.vtx[3318]', 'forBody.vtx[3319]', 'forBody.vtx[3323]', 'forBody.vtx[3324]', 'forBody.vtx[3327]', 'forBody.vtx[3328]', 'forBody.vtx[3329]', 'forBody.vtx[3330]', 'forBody.vtx[3333]', 'forBody.vtx[3334]', 'forBody.vtx[3336]', 'forBody.vtx[3494]', 'forBody.vtx[3729]', 'forBody.vtx[3950]', 'forBody.vtx[4144]', 'forBody.vtx[4334]', 'forBody.vtx[4526]', 'forBody.vtx[4707]', 'forBody.vtx[4878]', 'forBody.vtx[5043]', 'forBody.vtx[5183]', 'forBody.vtx[5322]', 'forBody.vtx[5461]', 'forBody.vtx[5600]', 'forBody.vtx[5741]']
        self.lidUpperRVerts=['forBody.vtx[6251]', 'forBody.vtx[6252]', 'forBody.vtx[6253]', 'forBody.vtx[6254]', 'forBody.vtx[6255]', 'forBody.vtx[6256]', 'forBody.vtx[6257]', 'forBody.vtx[6258]', 'forBody.vtx[6259]', 'forBody.vtx[6260]', 'forBody.vtx[6261]', 'forBody.vtx[6262]', 'forBody.vtx[6263]', 'forBody.vtx[6264]', 'forBody.vtx[6266]', 'forBody.vtx[6306]', 'forBody.vtx[6347]']
        self.lidLowerRVerts=['forBody.vtx[6239]', 'forBody.vtx[6240]', 'forBody.vtx[6241]', 'forBody.vtx[6242]', 'forBody.vtx[6243]', 'forBody.vtx[6244]', 'forBody.vtx[6245]', 'forBody.vtx[6246]', 'forBody.vtx[6247]', 'forBody.vtx[6248]', 'forBody.vtx[6249]', 'forBody.vtx[6250]', 'forBody.vtx[6251]', 'forBody.vtx[6277]', 'forBody.vtx[6313]', 'forBody.vtx[6347]', 'forBody.vtx[6348]']
        self.browRVert=['forBody.vtx[5388]']
        
    def assignDelete(self,data,flag):
        if flag=='ass':
            if data == 'headVerts': self.headVerts=cmds.ls(sl=True)
            elif data == 'lipUpperVerts': self.lipUpperVerts=cmds.ls(sl=True,fl=True)
            elif data == 'lipLowerVerts': self.lipLowerVerts=cmds.ls(sl=True,fl=True)
            elif data == 'lidUpperRVerts': self.lidUpperRVerts=cmds.ls(sl=True,fl=True)
            elif data == 'lidLowerRVerts': self.lidLowerRVerts=cmds.ls(sl=True,fl=True)
            elif data == 'browRVert': self.browRVert=cmds.ls(sl=True,fl=True)
        elif flag=='sel':
            if data == 'headVerts': cmds.select(self.headVerts)
            elif data == 'lipUpperVerts': cmds.select(self.lipUpperVerts)
            elif data == 'lipLowerVerts': cmds.select(self.lipLowerVerts)
            elif data == 'lidUpperRVerts': cmds.select(self.lidUpperRVerts)
            elif data == 'lidLowerRVerts': cmds.select(self.lidLowerRVerts)
            elif data == 'browRVert': cmds.select(self.browRVert)
        elif flag=='del':
            if data == 'headVerts': self.headVerts=None
            elif data == 'lipUpperVerts': self.lipUpperVerts=None
            elif data == 'lipLowerVerts': self.lipLowerVerts=None
            elif data == 'lidUpperRVerts': self.lidUpperRVerts=None
            elif data == 'lidLowerRVerts': self.lidLowerRVerts=None
            elif data == 'browRVert': self.browRVert=None

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
        cvPos5 = EyeFunc._mirrorCVs(cvPos)
        ModFunc._applyTransformData(cvPos5, os=True)
        
        cvPos = ModFunc._getTransformData(allCVs, t=True, r=False, os=True)
        cvPos4 = EyeFunc._matchCloseCrv(cvPos)
        ModFunc._applyTransformData(cvPos4, os=True)
        
        
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
    
    def saveNames(self,_):
        pass
        
        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run01=AutoRigFace()
UI.createWindow(run01)
### 3. orient edit mode (unparent the clusters - edit orient - reparent the clusters)

###DQ skin > attibute editor > support Non-rigid transformation ON
