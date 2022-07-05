import maya.cmds as cmds
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
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
importlib.reload(Namer)
importlib.reload(Builder)
importlib.reload(UI)
importlib.reload(DataFunc)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(LidFunc)
importlib.reload(EyeFunc)
importlib.reload(BrowFunc)

###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigFace(Builder.BuildCtls, Builder.ConnectCtls, Builder.BindGeo, UI.createUI):
    def __init__(self):
        self.usd = cmds.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
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
        self.dir = cmds.fileDialog2(fileFilter="*.json", dialogStyle=1, fm=3, caption ='Set character data directory')[0]
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
            self.data['geo'][x]=cmds.ls(sl=True)
            #print(self.data['geo'][x])
        if flag=='sel':
            cmds.select(self.data['geo'][x])
        
    def assignVerts(self,x,flag):
        if flag=='ass':
            self.data['verts'][x]=cmds.ls(sl=True,fl=True)
            #print(self.data['verts'][x])
        elif flag=='sel':
            cmds.select(self.data['verts'][x])
    
    def names(self):
        self.faceRoot = 'face_root'
        self.animGrp = 'anim_grp'
        self.rigGrp = 'rig_grp'
        self.bindGrp = 'bind_grp'
        
        #execute namer class object
        self.J = Namer.template()
        self.M = Namer.mouth(self.data['verts'])
        self.L = Namer.lid(self.data['verts'])
        self.E = Namer.eye(self.data['verts'])
        self.B = Namer.brow(self.data['verts'])
        self.N = Namer.nose(self.data['verts'])
        
        self.faceCtl = 'face_ctl'
        self.faceUpCtl = 'face_upper_ctl'
        self.faceLoCtl = 'face_lower_ctl'
        self.jawCtl = 'jaw_ctl'
        self.cheekCtlGrp = 'cheek_ctl_grp'
        self.cheekCtls = [d.replace('_bind','_ctl') for d in self.J.cheekBinds]
        self.cheekDrvs = ['cheek_driver_r_nul','cheek_driver_l_nul']
        
        self.allCtls = self.M.microCtls + self.M.macroCtls + self.M.cornerCtls + self.L.ctls + self.E.ctls + self.B.ctls + [self.jawCtl] + self.N.sneerCtls + self.N.nostrilCtls
        self.allCrv = self.M.blendCrvs + self.L.rBlendCrvs + self.L.lBlendCrvs
        self.bindSets = {
            'face': [self.J.faceBind,self.J.faceUpBind,self.J.faceLoBind,self.J.jawBind,self.J.noseBridgeBind]
                    +self.J.browBinds+self.J.cheekBinds+self.J.noseBinds+self.J.eyeSocBinds
                    +self.L.rBinds+self.L.lBinds
                    +self.M.binds,
            'brow': self.J.browBinds,
            'lash': self.L.rBinds+self.L.lBinds,
            'eyeR': [self.J.eyeBinds[0]],
            'eyeL': [self.J.eyeBinds[1]],
            'upTeeth': [self.M.teethBinds[0]],
            'loTeeth': [self.M.teethBinds[1]],
            'tongue': self.M.tongueBinds,
            'extra': [self.J.faceUpBind]
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
            f
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

### mouth macro ctl
### upperteeth parent constraint jawBind & mouthClus(jawCtl & mouthCtl) follow attr
### lowerteeth nul2 parent constraint (double transform w faceLower ctl)
### cheek lower follow
### inner brow ctl
### mCorner ctl double transform with lowerCtl (need driver setup)

#no loc
### linear mouth crv
#no hierarchy on lip jnt, mouth jnt
#mouth driver jnt order
#mouth&eye is initially the same, but mouth has bindmesh following driver jnts
#lipCvCls should follow follicles on bindmesh

### make every joint 0 on transform + direct connection on ctrl

### disable shape visablity & display handle, enable drawing override on display