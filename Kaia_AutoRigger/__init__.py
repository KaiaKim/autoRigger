import maya.cmds as mc
from functools import partial
import importlib
import json

from Kaia_AutoRigger import namer
from Kaia_AutoRigger import data_
from Kaia_AutoRigger import builder
from Kaia_AutoRigger import helper
from Kaia_AutoRigger import binder

from Kaia_AutoRigger.ui import main
from Kaia_AutoRigger.ui import handler

importlib.reload(namer)
importlib.reload(data_)
importlib.reload(builder)
importlib.reload(helper)
importlib.reload(binder)

importlib.reload(main)
importlib.reload(handler)
###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigFace(data_.ImportExport, builder.BuildRig, helper.HelpExtra, binder.BindGeo, main.createUI, handler.ButtonHandler):
    def __init__(self):
        self.usd = mc.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
        self.mayascripts = '%s/%s' % (self.usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts
        
        self.winTitle = 'Kaia\'s auto rigger' #display name
        self.winName = 'kaiaAutoRigFace' #node name
        
        self.dir = None
        
        self.data = {
            'geo':{
                'face':None, 'brow':None, 'lash':None,
                'eyeR':None, 'eyeL':None, 'upTeeth':None,
                'loTeeth':None, 'tongue':None
                },
            'verts':{
                'lipUpper':None,'lipLower':None, 
                'lidUpperR':None,'lidLowerR':None
                },
            'orients':[],
            'bsCrv':[],
            'attr':{}
        }
    
        self.createWindow()
        
    def setNames(self):
        self.guideGrp = 'face_GUIDE_Grp'
        self.bindGrp = 'face_BIND_Grp'
        self.NTGrp = 'face_NT_Grp'
        self.noSelectLayer = 'noSelect'
        self.BSCrvSet = 'BSCurve_set'
        
        #execute namer class object
        self.F = namer.Face()
        self.M = namer.Mouth(self.data['verts'])
        self.TE = namer.Teeth()
        self.TO = namer.Tongue()
        self.L = namer.Lid(self.data['verts'])
        self.E = namer.Eye()
        self.B = namer.Brow()
        self.N = namer.Nose()
        
        self.allBinds = (
                        self.F.binds + self.B.binds + self.N.binds
                        + self.E.socBinds + self.E.binds
                        + self.TE.binds + self.TO.binds
                        + self.L.rBinds + self.L.lBinds
                        + self.M.binds
                        )
                    
        self.allCtls = (
                        self.F.ctls + self.M.lipCtls + self.M.cornerCtls 
                        + self.L.ctls + self.L.microCtls[0] + self.L.microCtls[1] + self.L.microCtls[2] + self.L.microCtls[3]
                        + self.E.ctls + self.B.ctls
                        + self.N.ctls + self.TO.ctls + self.TE.ctls
                        )
        self.allCrv = self.M.blendCrvs + self.L.rBlendCrvs + self.L.lBlendCrvs
        
        self.bindSets = {
            'face': [self.F.bind, self.F.upBind, self.F.jawBind]
                    + self.B.binds + self.N.binds
                    + self.L.rBinds + self.L.lBinds
                    + self.M.binds,
            'brow': self.B.binds,
            'lash': self.L.rBinds + self.L.lBinds,
            'eyeR': [self.E.binds[0]],
            'eyeL': [self.E.binds[1]],
            'upTeeth': [self.TE.binds[0]],
            'loTeeth': [self.TE.binds[1]],
            'tongue': self.TO.binds
        }
        


###-----------------------------------------------------EXECUTE---------------------------------------------------------------
if __name__ == "__main__":
    Kaia_AutoRigger.AutoRigFace()
    
###DQ skin > attibute editor > support Non-rigid transformation ON



#cheek seperate, lower face seperate


### 1. eye close shape on guide O
### 2. Lock values on guide joints O
### 3. Smart clusters O
### 4. Absolute options for clusters O
### 5. mirror guide >> mirror lip curve too O
### 6. Auto mirror joints


### 7. Duplicate Binds from Guide to break connections
### 8. Duplicate Curves from Guide
### 9. unlock all values for joints

### 7. hide mouth left curve

### 8. Ditch Cheek rig, Eye rig
