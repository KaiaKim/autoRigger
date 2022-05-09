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
    
    def cutHead(self,_):
        #select edge loop
        
        #detach body&head
        #seperate
        #get body vertex(face)
        #combine body&head
        #merge vertex
            ###body finish
            
        #duplicate body
        #delete body vertex(face)
            ###head finish

        #select head
        #select body
        #deform-blendshape (check topology off, local)
        #weight 1
        print('cut head func')
        pass
    
    def quickTest(self,_):
        #some hard coded data for quick testing
        self.headVerts=['body.vtx[0:6959]']
        self.lipUpperVerts=['body.vtx[3314]', 'body.vtx[3315]', 'body.vtx[3317]', 'body.vtx[3320]', 'body.vtx[3321]', 'body.vtx[3322]', 'body.vtx[3325]', 'body.vtx[3326]', 'body.vtx[3327]', 'body.vtx[3331]', 'body.vtx[3332]', 'body.vtx[3335]', 'body.vtx[3337]', 'body.vtx[3495]', 'body.vtx[3818]', 'body.vtx[4010]', 'body.vtx[4200]', 'body.vtx[4386]', 'body.vtx[4574]', 'body.vtx[4751]', 'body.vtx[4918]', 'body.vtx[5079]', 'body.vtx[5215]', 'body.vtx[5350]', 'body.vtx[5485]', 'body.vtx[5620]', 'body.vtx[5741]']
        self.lipLowerVerts=['body.vtx[3313]', 'body.vtx[3316]', 'body.vtx[3318]', 'body.vtx[3319]', 'body.vtx[3323]', 'body.vtx[3324]', 'body.vtx[3327]', 'body.vtx[3328]', 'body.vtx[3329]', 'body.vtx[3330]', 'body.vtx[3333]', 'body.vtx[3334]', 'body.vtx[3336]', 'body.vtx[3494]', 'body.vtx[3729]', 'body.vtx[3950]', 'body.vtx[4144]', 'body.vtx[4334]', 'body.vtx[4526]', 'body.vtx[4707]', 'body.vtx[4878]', 'body.vtx[5043]', 'body.vtx[5183]', 'body.vtx[5322]', 'body.vtx[5461]', 'body.vtx[5600]', 'body.vtx[5741]']
        self.lidUpperRVerts=['body.vtx[6251]', 'body.vtx[6252]', 'body.vtx[6253]', 'body.vtx[6254]', 'body.vtx[6255]', 'body.vtx[6256]', 'body.vtx[6257]', 'body.vtx[6258]', 'body.vtx[6259]', 'body.vtx[6260]', 'body.vtx[6261]', 'body.vtx[6262]', 'body.vtx[6263]', 'body.vtx[6264]', 'body.vtx[6266]', 'body.vtx[6306]', 'body.vtx[6347]']
        self.lidLowerRVerts=['body.vtx[6239]', 'body.vtx[6240]', 'body.vtx[6241]', 'body.vtx[6242]', 'body.vtx[6243]', 'body.vtx[6244]', 'body.vtx[6245]', 'body.vtx[6246]', 'body.vtx[6247]', 'body.vtx[6248]', 'body.vtx[6249]', 'body.vtx[6250]', 'body.vtx[6251]', 'body.vtx[6277]', 'body.vtx[6313]', 'body.vtx[6347]', 'body.vtx[6348]']
        self.browRVert=['body.vtx[5388]']
        
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

#keyframe -option over -index 0 -absolute -floatChange 1 lid_upper_r_closed_blend_upper_lid_r_curve_closed ;
#keyframe -index 0 -absolute -valueChange 1 lid_upper_r_closed_blend_upper_lid_r_curve_closed ;
#keyTangent -index 0 -outTangentType linear lid_upper_r_closed_blend_upper_lid_r_curve_closed ;
#setAttr "lid_upper_r_closed_blend_upper_lid_r_curve_closed.preInfinity" 1;
#setAttr "lid_upper_r_closed_blend_upper_lid_r_curve_closed.postInfinity" 1;