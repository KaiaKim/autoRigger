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

print(cmds.ls(sl=True,fl=True))
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
        '''        
        self.verts['head']=['face.vtx[0:6959]']
        self.verts['lipUpper']=['face.vtx[3314]', 'face.vtx[3315]', 'face.vtx[3317]', 'face.vtx[3320]', 'face.vtx[3321]', 'face.vtx[3322]', 'face.vtx[3325]', 'face.vtx[3326]', 'face.vtx[3327]', 'face.vtx[3331]', 'face.vtx[3332]', 'face.vtx[3335]', 'face.vtx[3337]', 'face.vtx[3495]', 'face.vtx[3818]', 'face.vtx[4010]', 'face.vtx[4200]', 'face.vtx[4386]', 'face.vtx[4574]', 'face.vtx[4751]', 'face.vtx[4918]', 'face.vtx[5079]', 'face.vtx[5215]', 'face.vtx[5350]', 'face.vtx[5485]', 'face.vtx[5620]', 'face.vtx[5741]']
        self.verts['lipLower']=['face.vtx[3313]', 'face.vtx[3316]', 'face.vtx[3318]', 'face.vtx[3319]', 'face.vtx[3323]', 'face.vtx[3324]', 'face.vtx[3327]', 'face.vtx[3328]', 'face.vtx[3329]', 'face.vtx[3330]', 'face.vtx[3333]', 'face.vtx[3334]', 'face.vtx[3336]', 'face.vtx[3494]', 'face.vtx[3729]', 'face.vtx[3950]', 'face.vtx[4144]', 'face.vtx[4334]', 'face.vtx[4526]', 'face.vtx[4707]', 'face.vtx[4878]', 'face.vtx[5043]', 'face.vtx[5183]', 'face.vtx[5322]', 'face.vtx[5461]', 'face.vtx[5600]', 'face.vtx[5741]']
        self.verts['lidUpperR']=['face.vtx[6251]', 'face.vtx[6252]', 'face.vtx[6253]', 'face.vtx[6254]', 'face.vtx[6255]', 'face.vtx[6256]', 'face.vtx[6257]', 'face.vtx[6258]', 'face.vtx[6259]', 'face.vtx[6260]', 'face.vtx[6261]', 'face.vtx[6262]', 'face.vtx[6263]', 'face.vtx[6264]', 'face.vtx[6266]', 'face.vtx[6306]', 'face.vtx[6347]']
        self.verts['lidLowerR']=['face.vtx[6239]', 'face.vtx[6240]', 'face.vtx[6241]', 'face.vtx[6242]', 'face.vtx[6243]', 'face.vtx[6244]', 'face.vtx[6245]', 'face.vtx[6246]', 'face.vtx[6247]', 'face.vtx[6248]', 'face.vtx[6249]', 'face.vtx[6250]', 'face.vtx[6251]', 'face.vtx[6277]', 'face.vtx[6313]', 'face.vtx[6347]', 'face.vtx[6348]']
        self.verts['browR']=['face.vtx[5388]']'''
        
        self.verts['head']=['face.vtx[0:6959]']
        self.verts['lipUpper']=['face.vtx[3331]', 'face.vtx[3332]', 'face.vtx[3334]', 'face.vtx[3337]', 'face.vtx[3338]', 'face.vtx[3339]', 'face.vtx[3342]', 'face.vtx[3343]', 'face.vtx[3344]', 'face.vtx[3348]', 'face.vtx[3349]', 'face.vtx[3352]', 'face.vtx[3354]', 'face.vtx[3520]', 'face.vtx[6862]', 'face.vtx[6863]', 'face.vtx[6865]', 'face.vtx[6868]', 'face.vtx[6869]', 'face.vtx[6870]', 'face.vtx[6873]', 'face.vtx[6874]', 'face.vtx[6875]', 'face.vtx[6879]', 'face.vtx[6880]', 'face.vtx[6883]', 'face.vtx[6885]']
        self.verts['lipLower']=['face.vtx[3330]', 'face.vtx[3333]', 'face.vtx[3335]', 'face.vtx[3336]', 'face.vtx[3340]', 'face.vtx[3341]', 'face.vtx[3344]', 'face.vtx[3345]', 'face.vtx[3346]', 'face.vtx[3347]', 'face.vtx[3350]', 'face.vtx[3351]', 'face.vtx[3353]', 'face.vtx[3519]', 'face.vtx[6861]', 'face.vtx[6864]', 'face.vtx[6866]', 'face.vtx[6867]', 'face.vtx[6871]', 'face.vtx[6872]', 'face.vtx[6875]', 'face.vtx[6876]', 'face.vtx[6877]', 'face.vtx[6878]', 'face.vtx[6881]', 'face.vtx[6882]', 'face.vtx[6884]']
        self.verts['lidUpperR']=['face.vtx[3554]', 'face.vtx[3555]', 'face.vtx[3557]', 'face.vtx[3558]', 'face.vtx[3559]', 'face.vtx[3561]', 'face.vtx[3562]', 'face.vtx[3563]', 'face.vtx[3564]', 'face.vtx[3565]', 'face.vtx[3567]', 'face.vtx[3568]', 'face.vtx[3571]', 'face.vtx[3572]', 'face.vtx[3573]', 'face.vtx[3575]', 'face.vtx[3576]', 'face.vtx[3577]', 'face.vtx[3580]', 'face.vtx[3581]']
        self.verts['lidLowerR']=['face.vtx[3552]', 'face.vtx[3553]', 'face.vtx[3556]', 'face.vtx[3559]', 'face.vtx[3560]', 'face.vtx[3566]', 'face.vtx[3567]', 'face.vtx[3569]', 'face.vtx[3570]', 'face.vtx[3574]', 'face.vtx[3578]', 'face.vtx[3579]', 'face.vtx[3582]', 'face.vtx[3583]']
        self.verts['browR']=['face.vtx[278]']
    def assignDelete(self,data,flag):
        if flag=='ass':
            if data == 'head': self.verts['head']=cmds.ls(sl=True)
            else: self.verts[data]=cmds.ls(sl=True,fl=True)
            print(self.verts[data])
            
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
            data = DataFunc._getTransform(orients, t=False, r=True)
        
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
                
            DataFunc._applyTransform(mirrorData)

        if flag=='load':
            #apply transform
            DataFunc._applyTransform(data)
        
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
            ptPos = DataFunc._getTransform(ltsPt, t=True, r=False, ws=True)
        
        if flag=='mirror':
            #modify data
            mirrorPos = ptPos
            for i in mirrorPos:
                i['name'] = i['name'].replace('_r_','_l_')
                x,y,z = i['pos']
                i['pos'] = (-x,y,z)
            DataFunc._applyTransform(mirrorPos)
        
        if flag=='load':
            #apply transform
            DataFunc._applyTransform(ptPos, ws=True)
        
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
            allCrv = self.M.blendCrvs + self.L.rBlendCrvs + self.L.lBlendCrvs
            allCVs = []
            for i in allCrv:
                CVs = ModFunc._getCVs(i)
                allCVs += CVs
            cvPos = DataFunc._getTransform(allCVs, t=True, r=False, os=True)

        if flag=='load':
            #apply transform
            DataFunc._applyTransform(cvPos, os=True)
        
        if flag=='save':    
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/blendCrv.json', "w") as wfile:
                json.dump(cvPos, wfile)
                
    def mirrorBlendCrvMouth(self,_):
        #modify data mouth
        cvPos2 = MouthFunc._symmetricMouthCrv(self.M.blendCrvs)
        DataFunc._applyTransform(cvPos2, os=True)
        cvPos3 = MouthFunc._matchCrvRtoL(cvPos2)
        DataFunc._applyTransform(cvPos3, os=True)
        
    def mirrorBlendCrvEyes(self,_):
        #modify data eyes
        allCVs = []
        for i in self.L.rBlendCrvs+self.L.lBlendCrvs:
            CVs = ModFunc._getCVs(i)
            allCVs += CVs
            
        cvPos = DataFunc._getTransform(allCVs, t=True, r=False, os=True)
        cvPos5 = LidFunc._mirrorCVs(cvPos)
        DataFunc._applyTransform(cvPos5, os=True)
        
    def enterOrientEdit(self,_):
        print('### enter orient edit mode ###')
        ###lip ctrl
        #unparent lipCvClsoffset from lip ctrl
        for clus in self.M.cvCls:
            cmds.parent(clus+'_offset', w=True) #parent to world

        ###mouth ctrl
        #delete parent constraint of jaw clusters
        #delete parent constraint of lip ctrl nuls
        
        ###mCorner ctrl
        #don't need anything
    
    def exitOrientEdit(self,_):
        print('### exit orient edit mode ###')
        for ctl,clus in zip(self.L.microCtls,self.L.cvCls):
            cmds.parent(clus+'_offset',ctl)

    def changeCornerN(self,x,y,z):
        ModFunc._normalizeCtls(self.M.cornerCtls,val=(x,y,z))
        
    def changeLipPull(self,one,two):
        for i in self.M.cornerCtls:
            cmds.setAttr(i+'.lipOnePull', one)
            cmds.setAttr(i+'.lipTwoPull', two)

        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run01=AutoRigFace()
UI.createWindow(run01)

###DQ skin > attibute editor > support Non-rigid transformation ON

###Delete mouth bind on skeleton
