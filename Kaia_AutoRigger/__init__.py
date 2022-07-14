import maya.cmds as mc
from functools import partial
import importlib
import json

from Kaia_AutoRigger import Namer
from Kaia_AutoRigger import Builder
from Kaia_AutoRigger import UI
from Kaia_AutoRigger import DataFunc
from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import LidFunc

importlib.reload(Namer)
importlib.reload(Builder)
importlib.reload(UI)
importlib.reload(DataFunc)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(LidFunc)


###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigFace(Builder.BuildCtls, Builder.ConnectCtls, Builder.BindGeo, UI.createUI):
    def __init__(self):
        self.usd = mc.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
        self.mayascripts = '%s/%s' % (self.usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts
        
        self.winTitle = 'Kaia\'s auto rigger' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigFace' #this needs to be ac word that has no spaces or it won't work! #node name
        
        self.dir = None
        
        self.data = {
            'geo':{'face':None,'brow':None,'lash':None,'eyeR':None,'eyeL':None,'upTeeth':None,'loTeeth':None,'tongue':None,'extra':None},
            'verts':{'lipUpper':None,'lipLower':None,'lidUpperR':None,'lidLowerR':None,'browR':None},
            'orients':[],
            'bsCrv':[],
            'attr':{}
        }
    
    def setDir(self,_):
        #get file path
        self.dir = mc.fileDialog2(fileFilter="*.json", dialogStyle=1, fm=3, caption ='Set character data directory')[0]
        print('Directory:',self.dir)
        
    def importData(self):
        if self.dir==None:
            print('please set directory first')
            return
        
        #read json files
        with open(self.dir+'/geoNames.json',"r") as rfile: self.data['geo'] = json.load(rfile)
        with open(self.dir+'/vertIndices.json',"r") as rfile: self.data['verts'] = json.load(rfile)
        with open(self.dir+'/ctlOrient.json',"r") as rfile: self.data['orients'] = json.load(rfile)
        with open(self.dir+'/blendshapeCrv.json',"r") as rfile: self.data['bsCrv'] = json.load(rfile)
    
    def exportData(self,_):
        if self.dir==None:
            print('please set directory first')
            return
            
        #get orient data
        orients = [d+'_orient' for d in self.allCtls]
        self.data['orients'] = DataFunc._getTransform(orients, t=False, r=True)
        
        #get blendshape crv data
        allCVs = []
        for i in self.allCrv:
            CVs = ModFunc._getCVs(i)
            allCVs += CVs
        self.data['bsCrv'] = DataFunc._getTransform(allCVs, t=True, r=False, os=True)
        
        #write json files
        with open(self.dir+'/geoNames.json', "w") as wfile: json.dump(self.data['geo'], wfile)
        with open(self.dir+'/vertIndices.json',"w") as wfile: json.dump(self.data['verts'], wfile)
        with open(self.dir+'/ctlOrient.json',"w") as wfile: json.dump(self.data['orients'], wfile)
        with open(self.dir+'/blendshapeCrv.json',"w") as wfile: json.dump(self.data['bsCrv'], wfile)
    
    def assignGeo(self,x,flag):
        if flag=='ass':
            self.data['geo'][x]=mc.ls(sl=True)
            #print(self.data['geo'][x])
        if flag=='sel':
            mc.select(self.data['geo'][x])
        
    def assignVerts(self,x,flag):
        if flag=='ass':
            self.data['verts'][x]=mc.ls(sl=True,fl=True)
            #print(self.data['verts'][x])
        elif flag=='sel':
            mc.select(self.data['verts'][x])
    
    def names(self):
        self.faceRoot = 'face_root'
        self.animGrp = 'anim_grp'
        self.rigGrp = 'rig_grp'
        self.bindGrp = 'bind_grp'
        
        #execute namer class object
        self.F = Namer.face()
        self.M = Namer.mouth(self.data['verts'])
        self.C = Namer.cheek()
        self.T = Namer.teethTongue()
        self.L = Namer.lid(self.data['verts'])
        self.E = Namer.eye()
        self.B = Namer.brow()
        self.N = Namer.nose()
        
        self.allBinds = ['face_bind', 'face_upper_bind', 'brow_l_bind', 'brow_inner_l_bind', 'brow_corrugator_l_bind', 'brow_peak_l_bind', 'brow_r_bind', 'brow_inner_r_bind', 'brow_corrugator_r_bind', 'brow_peak_r_bind', 'teeth_upper_bind', 'eye_socket_l_bind', 'eye_l_bind', 'eye_socket_r_bind', 'eye_r_bind', 'cheek_upper_l_bind', 'cheek_upper_r_bind', 'face_lower_bind', 'nose_bridge_bind', 'nose_bind', 'sneer_l_bind', 'nostril_l_bind', 'sneer_r_bind', 'nostril_r_bind', 'cheek_r_bind', 'cheek_l_bind', 'jaw_trans_bind', 'jaw_bind', 'jaw_tip_bind', 'teeth_lower_bind', 'cheek_lower_r_bind', 'cheek_lower_l_bind', 'tongue_01_bind', 'tongue_02_bind', 'tongue_03_bind', 'tongue_04_bind', 'tongue_05_bind', 'tongue_06_bind', 'tongue_07_bind'] 
        self.allCtls = self.M.lipCtls + self.M.cornerCtls + self.L.ctls + self.E.ctls + self.B.ctls + [self.F.jawCtl] + self.N.sneerCtls
        self.allCrv = self.M.blendCrvs + self.L.rBlendCrvs + self.L.lBlendCrvs
        self.bindSets = {
            'face': [self.F.bind,self.F.upBind,self.F.loBind,self.F.jawBind,self.N.bridgeBind]
                    +self.B.binds+self.C.binds+self.N.binds+self.E.socBinds
                    +self.L.rBinds+self.L.lBinds
                    +self.M.binds,
            'brow': self.B.binds,
            'lash': self.L.rBinds+self.L.lBinds,
            'eyeR': [self.E.binds[0]],
            'eyeL': [self.E.binds[1]],
            'upTeeth': [self.T.teethBinds[0]],
            'loTeeth': [self.T.teethBinds[1]],
            'tongue': self.T.tongueBinds,
            'extra': [self.F.upBind]
        }

    
    def mirrorCtlOrient(self,_):
        #get transform
        orients = [d+'_orient' for d in self.allCtls]
        self.data['orients'] = DataFunc._getTransform(orients, t=False, r=True)

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
            
        DataFunc._applyTransform(mirrorData)
            
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
        

    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run01=AutoRigFace()
run01.createWindow()

###DQ skin > attibute editor > support Non-rigid transformation ON

