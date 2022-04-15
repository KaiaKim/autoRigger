import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import UI
from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import EyeFunc
importlib.reload(UI)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(EyeFunc)

###-----------------------------------------------------CLASS---------------------------------------------------
class BuildRig():
    def __init__(self):
        pass
    
    def names(self):
        self.names = {}
        self.faceRoot = 'face_root'
        self.animGrp = 'anim_grp'
        self.rigGrp = 'rig_grp'
        self.bindGrp = 'bind_grp'
        
        self.faceBind = 'face_bind' #This name is from the template file. No change this!
        self.faceLowerBind = 'face_lower_bind' #No change this!
        self.jawBind = 'jaw_bind' #No change this!
        self.eyeSocketBindR = 'eye_socket_r_bind'
        self.eyeSocketBindL = 'eye_socket_l_bind'
        
        self.lidUpperRCrv = 'upper_lid_r_curve' #No change this!
        self.lidLowerRCrv = 'lower_lid_r_curve' #No change this!
        self.lidUpperLCrv = self.lidUpperRCrv.replace('_r_','_l_') #No change this!
        self.lidLowerLCrv = self.lidLowerRCrv.replace('_r_','_l_')
        
        self.lipUpperCrv = 'lip_upper_curve' #No change this!
        self.lipLowerCrv = 'lip_lower_curve' #No change this!
        self.mouthCrv = 'mouth_curve'
        
        self.headVerts = None
        self.lipUpperVerts = None
        self.lipLowerVerts = None
        self.lidUpperRVerts = None
        self.lidLowerRVerts = None
        self.eyeballRLtc = None
        self.eyeballLLtc = None
        self.eyeballRLtc = 'eye_r_ffd1'
        self.eyeballRLtc = 'eye_r_ffd1'
        
        self.lipUpperLocGrp = 'lip_upper_loc_grp' #Grp means group name. I will use these strings when I create the node.
        self.lipLowerLocGrp = 'lip_lower_loc_grp'
        self.lidRLocGrp = 'lid_r_loc_grp'
        self.lidLLocGrp = 'lid_l_loc_grp'
        self.lipLocs = []
        self.lidRLocs = []
        self.lidLLocs = []
        
        self.lipBinds = []
        self.lidRBinds = []
        self.lidLBinds = []
        
        self.mouthDriverGrp = 'mouth_driver_jnt_grp'
        self.mouthDrivers = []
        
        self.mouthBindmeshesGrp = 'mouth_bindmesh_grp'
        self.mouthBindmeshes = []
        
        self.jawClsGrp = 'jaw_cls_grp'
        self.jawCls = []
        
        self.mouthFolGrp = 'mouth_fol_grp'
        self.mouthFols = []
        
        self.lipCtlGrp = 'lip_ctl_grp'
        self.lipCtls = []
        self.mouthCtlGrp = 'mouth_ctl_grp'
        self.mouthCtls = []
        self.mCornerCtlGrp = 'mouth_corner_ctl_grp'
        self.mCornerCtls = []
        self.lipCvCls = []
        
        self.blinkCtlGrp = 'blink_ctl_grp'
        self.blinkCtls = []
        
        self.mouthBlendCrvGrp = 'mouth_blend_crv_grp'
        self.mouthBlendCrvs = []
        self.eyeBlendCrvGrp = 'eye_blend_crv_grp'
        self.eyeBlendCrvs = []
        
        self.eyeLoft = None
        
        self.allCtls = []
            
    
    def buildMouthRig01(self,_):
        #0:Create Groups
        self.createGrps() 
        
        #1: Generate mouth_curve from lip_curves
        MouthFunc._createMouthCrv(self.mouthCrv, self.lipUpperCrv, self.lipLowerCrv)
        
        #1: Create lip_locs on lip verts & connect to lip_curves
        self.lipUpperLocs = MouthFunc._lipLocsNamer(self.lipUpperVerts, prefix='lip_upper')
        self.lipLowerLocs = MouthFunc._lipLocsNamer(self.lipLowerVerts, prefix='lip_lower')
        self.lipLocs = self.lipUpperLocs + self.lipLowerLocs
        
        upperPos = ModFunc._getPosListFromVerts(self.lipUpperVerts)
        ModFunc._createLocsOnCurve(self.lipUpperLocs, upperPos, self.lipUpperCrv, self.lipUpperLocGrp)
        
        
        lowerPos = ModFunc._getPosListFromVerts(self.lipLowerVerts)
        ModFunc._createLocsOnCurve(self.lipLowerLocs, lowerPos, self.lipLowerCrv, self.lipLowerLocGrp)

        
        #2: Aim constraint lip_locs to jaw_bind
        ModFunc._aimConstLocs(self.lipLocs, self.jawBind, upObj=self.faceLowerBind)
        
        #2: Create lip_bind_jnts && constraint to lip_locs
        self.lipBinds = [d.replace('_loc', '_bind') for d in self.lipLocs]
        ModFunc._createJntsOnLocs(self.lipLocs,self.lipBinds,self.faceLowerBind)
        
        #2: Create mouth drivers
        driverList = ['corner_r','upper_00_r','upper_01_r','upper_m','upper_01_l','upper_00_l','corner_l','lower_00_l','lower_01_l','lower_m','lower_01_r','lower_00_r']
        self.mouthDrivers = ['mouth_'+d+'_driver' for d in driverList]
        ModFunc._createJntsOnCVs(self.mouthDrivers, self.mouthCrv,self.mouthDriverGrp) 

        
        #3: Create Bindmeshes on driver
        self.mouthBindmeshes = [d.replace('_driver','_bindmesh') for d in self.mouthDrivers]
        ModFunc._createBindmeshesOnJnts(self.mouthBindmeshes,self.mouthDrivers,self.mouthBindmeshesGrp)
        
        #4: Create Follicles on Bindmeshes
        self.mouthFols = [d.replace('bindmesh','fol') for d in self.mouthBindmeshes]
        ModFunc._createFolsOnBindmeshes(self.mouthFols,self.mouthBindmeshes,self.mouthFolGrp)
        
        #4: Create Clusters on Bindmeshes
        self.jawCls = [d.replace('bindmesh','cls') for d in self.mouthBindmeshes]
        ModFunc._createClsOnBindmeshes(self.jawCls,self.mouthBindmeshes,self.jawClsGrp)
        
        #4: Create Ctrls
            #lip ctrls
        microNames = [d.replace('fol','ctl').replace('mouth','lip') for d in self.mouthFols]
        
        self.lipCtls = ModFunc._createCtlGrp(self.mouthFols,microNames,self.lipCtlGrp, size=.3 )
        ModFunc._setOffset(self.lipCtls, t=(0,0,1), r=(90,0,0))
        ModFunc._scaleOrient(self.lipCtls)
        ModFunc._overrideColor(microNames, color=(1,1,0))
            
            #mouth ctrls
        macroFols = [d for d in self.mouthFols if '_m_' in d] #'mouth_upper_m_fol','mouth_lower_m_fol'
        macroNames = [d.replace('fol','ctl') for d in macroFols]
        
        self.mouthCtls = ModFunc._createCtlGrp(macroFols, macroNames, self.mouthCtlGrp, size=.5, shape='square')
        ModFunc._setOffset(self.mouthCtls, t=(0,0,1.5), r=(90,0,0))
        ModFunc._scaleOrient(self.mouthCtls)
        ModFunc._overrideColor(macroNames, color=(1,1,0))
        
            #corner ctrls
        cornerFols = [d for d in self.mouthFols if '_corner_' in d]
        cornerNames = [d.replace('fol','ctl') for d in cornerFols]
        
        self.mCornerCtls = ModFunc._createCtlGrp(cornerFols, cornerNames, self.mCornerCtlGrp, size=.5, shape='triangle')
        ModFunc._setOffset(self.mCornerCtls, t=(0,0,1), r=(90,0,0))
        ModFunc._scaleOrient(self.mCornerCtls)
        ModFunc._overrideColor(cornerNames, color=(1,0,0))
        
        self.allCtls += self.lipCtls + self.mouthCtls + self.mCornerCtls
        
        #5: Parent constraint micro nul2 group to macro ctl
        MouthFunc.constMicroToMacro(self.lipCtls)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.mCornerCtls,val=(1,1,1))
    
    def buildMouthRig02(self,_):
        #7: Attach Jaw Clusters to Jaw
        MouthFunc.attachJawCls(self.jawCls, self.mouthCtls, self.faceLowerBind, self.jawBind)
        
        #8: Create lipCV Clusters on lip_curves
        ctlList = [d['ctl'] for d in self.lipCtls]
        self.lipCvCls = MouthFunc._2CurvCvCls(self.lipUpperCrv, self.lipLowerCrv, ctlList)
        
        #10: Corner pin, Lip pull
        MouthFunc.setMouthCornerCtls(self.mCornerCtls, self.mouthCtls, self.jawCls, self.faceLowerBind,self.jawBind)
        
        #set lip pull attribute
        for i in self.mCornerCtls:
            cmds.setAttr(i['ctl']+'.lipOnePull', 0.7)
            cmds.setAttr(i['ctl']+'.lipTwoPull', 0.9)
    
        
    def buildEyeRig01(self,_):
        #1: Mirror Lid Curves
        self.lidUpperLCurv = ModFunc._mirrorObj(self.lidUpperRCrv)
        self.lidLowerLCurv = ModFunc._mirrorObj(self.lidLowerRCrv)
        
        #2: Create lid locs on lid verts & connect to lid curves
        upperRPos = ModFunc._getPosListFromVerts(self.lidUpperRVerts)
        upperRLocs = ModFunc._createLocsOnCurve(self.lidUpperRCrv, upperRPos, self.lidRLocGrp)
        upperRLocs = EyeFunc._eyeLocsNamer(upperRLocs, prefix='lid_upper_r')
        
        upperLPos = ModFunc._mirrorPosX(upperRPos)
        upperLLocs = ModFunc._createLocsOnCurve(self.lidUpperLCurv, upperLPos, self.lidLLocGrp)
        upperLLocs = EyeFunc._eyeLocsNamer(upperLLocs, prefix='lid_upper_l')
        
        lowerRPos = ModFunc._getPosListFromVerts(self.lidLowerRVerts)
        lowerRLocs = ModFunc._createLocsOnCurve(self.lidLowerRCrv, lowerRPos, self.lidRLocGrp, newGrp=False)
        lowerRLocs = EyeFunc._eyeLocsNamer(lowerRLocs, prefix='lid_lower_r')
        
        lowerLPos = ModFunc._mirrorPosX(lowerRPos)
        lowerLLocs = ModFunc._createLocsOnCurve(self.lidLowerLCurv, lowerLPos, self.lidLLocGrp, newGrp=False)
        lowerLLocs = EyeFunc._eyeLocsNamer(lowerLLocs, prefix='lid_lower_l')
        
        self.lidRLocs = upperRLocs + lowerRLocs
        self.lidLLocs = upperLLocs + lowerLLocs
        
        #3: Aim constraint lid locs to eye socket bind
        ModFunc._aimConstLocs(self.lidRLocs,self.eyeSocketBindR)
        ModFunc._aimConstLocs(self.lidLLocs,self.eyeSocketBindL)
        #4: Create lid bind jnts
        self.lidRBinds = [d.replace('_loc', '_bind') for d in self.lidRLocs]
        ModFunc._createJntsOnLocs(self.lidRLocs,self.lidRBinds,self.eyeSocketBindR)
        
        self.lidLBinds = [d.replace('_loc', '_bind') for d in self.lidLLocs]
        ModFunc._createJntsOnLocs(self.lidLLocs,self.lidLBinds,self.eyeSocketBindL)
        #5: Constraint to lid locs
        ModFunc._parentConstIterate(self.lidRLocs,self.lidRBinds)
        ModFunc._parentConstIterate(self.lidLLocs,self.lidLBinds)
        
        #4: Create Ctrls
            #blink ctrls
        blinkNames = ['blink_upper_r_ctl', 'blink_lower_r_ctl', 'blink_upper_l_ctl', 'blink_lower_l_ctl']
        socketBinds = [self.eyeSocketBindR, self.eyeSocketBindR, self.eyeSocketBindL, self.eyeSocketBindL]
        self.blinkCtls = ModFunc._createCtlGrp(socketBinds, blinkNames, self.blinkCtlGrp, size=6, const=False)
        EyeFunc._roatateCtrlShape(blinkNames)
        ModFunc._scaleOrient(self.blinkCtls)
        ModFunc._overrideColor(blinkNames, color=(1,0,0))
        
        self.allCtls += self.blinkCtls
        
        '''
        ModFunc._createClsOn2Curv()
        ModFunc._createCtlGrp()
        
        EyeFunc._createLoftBall()
        EyeFunc._SlideOnSurface()
        '''
        
    def BuildMouthBlendshapes01(self,_):
        #1: Duplicate orig curve
        self.mouthBlendCrvs = MouthFunc._createBsCrv(self.mouthCrv,self.mouthBlendCrvGrp)
        #2: Create Blendshape Node
        bsNode = MouthFunc._createBsNode(self.mouthCrv, self.mouthBlendCrvs)
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(bsNode)
        #4: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.mCornerCtls, self.mouthBlendCrvs, bsNode)
            
            
    def BuildEyeBlendshapes01(self,_):
        #1: Duplicate orig curve
        origList = [self.lidUpperRCrv, self.lidLowerRCrv, self.lidUpperLCrv, self.lidLowerLCrv]
        suffixList = ['_open','_closed'] #['_open','_neutral','_mid','_closed']
        self.eyeBlendCrvs = EyeFunc._createBsCrv(origList, suffixList, self.eyeBlendCrvGrp)
        #2: Create Blendshape Node
        bsNodeList = EyeFunc._createBsNode(origList,suffixList)
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        EyeFunc._connectCornerCtrl(self.blinkCtls, self.eyeBlendCrvs, bsNodeList)

        

    
    def createGrps(self):
        self.faceRoot = cmds.group(n=self.faceRoot, em=True)
        self.animGrp = cmds.group(n=self.animGrp, em=True)
        self.rigGrp = cmds.group(n=self.rigGrp, em=True)
        self.bindGrp = cmds.group(n=self.bindGrp, em=True)
        
    def arrangeGrps(self,_):
        #these are rather simple parent commands, we keep going even if there's an error.
        try:
            cmds.parent(self.animGrp,self.rigGrp,self.bindGrp,self.faceRoot)
        except: print('face_grp parent skipped')
        
        try:
            cmds.parent(self.faceBind, self.bindGrp)
        except: print('face_grp parent skipped')
        
        try:
            cmds.parent(
                self.lipUpperCrv, self.lipLowerCrv,
                self.lipUpperLocGrp, self.lipLowerLocGrp,
                self.mouthCrv,
                self.mouthBindmeshesGrp,self.jawClsGrp, self.mouthFolGrp,
                self.mouthDriverGrp,
                self.rigGrp)
        except: print('rig_grp parent skipped')
        
        try:
            cmds.parent(
                self.lipCtlGrp, self.mouthCtlGrp,
                self.animGrp)
        except: print('anim_grp parent skipped')
        
        
        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
