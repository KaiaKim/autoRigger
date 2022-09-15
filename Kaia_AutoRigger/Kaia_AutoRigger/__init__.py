import maya.cmds as mc
from functools import partial
import importlib
import json

from Kaia_AutoRigger import namer
from Kaia_AutoRigger import data_
from Kaia_AutoRigger import builder
from Kaia_AutoRigger import helper
from Kaia_AutoRigger import binder
from Kaia_AutoRigger import checker

from Kaia_AutoRigger.ui import main
from Kaia_AutoRigger.ui import handler

importlib.reload(namer)
importlib.reload(data_)
importlib.reload(builder)
importlib.reload(helper)
importlib.reload(binder)
importlib.reload(checker)

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
                'loTeeth':None, 'tongue':None, 'extra':None
                },
            'verts':{
                'lipUpper':None, 'lipLower':None, 'lidUpperR':None,
                'lidLowerR':None, 'browR':None
                },
            'orients':[],
            'bsCrv':[],
            'attr':{}
        }

        self.ctrlSet = 'ctrlSet'
    

    def names(self):
        self.NTGrp = 'face_NT_grp'
        
        #execute namer class object
        self.F = namer.Face()
        self.M = namer.Mouth(self.data['verts'])
        self.C = namer.Cheek()
        self.T = namer.TeethTongue()
        self.L = namer.Lid(self.data['verts'])
        self.E = namer.Eye()
        self.B = namer.Brow()
        self.N = namer.Nose()
        
        self.allBinds = mc.ls('*_bind')
        self.allCtls = self.M.lipCtls + self.M.cornerCtls + self.L.ctls + self.E.ctls + self.B.ctls + [self.F.jawCtl] + self.N.sneerCtls
        self.allCrv = self.M.blendCrvs + self.L.rBlendCrvs + self.L.lBlendCrvs
        
        self.bindSets = {
            'face': [self.F.bind, self.F.upBind, self.F.loBind, self.F.jawBind, self.N.bridgeBind]
                    + self.B.binds + self.C.binds + self.N.binds + self.E.socBinds
                    + self.L.rBinds + self.L.lBinds
                    + self.M.binds,
            'brow': self.B.binds,
            'lash': self.L.rBinds + self.L.lBinds,
            'eyeR': [self.E.binds[0]],
            'eyeL': [self.E.binds[1]],
            'upTeeth': [self.T.teethBinds[0]],
            'loTeeth': [self.T.teethBinds[1]],
            'tongue': self.T.tongueBinds,
            'extra': [self.F.upBind]
        }
        


###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run01=AutoRigFace()
run01.createWindow()

###DQ skin > attibute editor > support Non-rigid transformation ON

###face ctl > face nul

###lip ctl grp unparent
###mouth curve constraint to face root

###no cls nul
###setAttr "cluster1.relative" 1;
###parent constraint clusters on ctrl


###nose bind not connected
#cheek seperate, lower face seperate

