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
    
    def names(self,_):
        self.faceRoot = 'face_root'
        self.animGrp = 'anim_grp'
        self.rigGrp = 'rig_grp'
        self.bindGrp = 'bind_grp'
        
        self.faceBind = 'face_bind' #This name is from the template file. No change this!
        self.faceLowerBind = 'face_lower_bind' #No change this!
        self.jawBind = 'jaw_bind' #No change this!
        self.eyeSocketBindR = 'eye_socket_r_bind' #No change this!
        self.eyeSocketBindL = 'eye_socket_l_bind' #No change this!
        
        self.lidUpperRCrv = 'upper_lid_r_curve' #No change this!
        self.lidLowerRCrv = 'lower_lid_r_curve' #No change this!
        self.lidUpperLCrv = self.lidUpperRCrv.replace('_r_','_l_')
        self.lidLowerLCrv = self.lidLowerRCrv.replace('_r_','_l_')
        
        self.lipUpperCrv = 'lip_upper_curve' #No change this!
        self.lipLowerCrv = 'lip_lower_curve' #No change this!
        self.mouthCrv = 'mouth_curve'
        
        ###
        self.eyeballRLtc = 'eye_r_ffd1'
        self.eyeballRLtc = 'eye_r_ffd1'
        
        self.lipUpperLocGrp = 'lip_upper_loc_grp' #Grp means group name
        self.lipLowerLocGrp = 'lip_lower_loc_grp'
        self.lidRLocGrp = 'lid_r_loc_grp'
        self.lidLLocGrp = 'lid_l_loc_grp'
        self.lipUpperLocs = MouthFunc._lipLocsNamer(self.lipUpperVerts, prefix='lip_upper')
        self.lipLowerLocs = MouthFunc._lipLocsNamer(self.lipLowerVerts, prefix='lip_lower')
        self.lipLocs = self.lipUpperLocs + self.lipLowerLocs
        
        self.lidUpperRLocs = EyeFunc._eyeLocsNamer(self.lidUpperRVerts, prefix='lid_upper_r')
        self.lidUpperLLocs = EyeFunc._eyeLocsNamer(self.lidUpperRVerts, prefix='lid_upper_l') #we're just getting len of the list. left&right doesn't matter
        self.lidLowerRLocs = EyeFunc._eyeLocsNamer(self.lidLowerRVerts, prefix='lid_lower_r')
        self.lidLowerLLocs = EyeFunc._eyeLocsNamer(self.lidLowerRVerts, prefix='lid_lower_l')
        self.lidRLocs = self.lidUpperRLocs + self.lidLowerRLocs
        self.lidLLocs = self.lidUpperLLocs + self.lidLowerLLocs
        
        self.lipBinds = [d.replace('_loc', '_bind') for d in self.lipLocs]
        self.lidRBinds = [d.replace('_loc', '_bind') for d in self.lidRLocs]
        self.lidLBinds = [d.replace('_loc', '_bind') for d in self.lidLLocs]
        
        self.mouthDriverGrp = 'mouth_driver_jnt_grp'
        driverList = ['corner_r','upper_00_r','upper_01_r','upper_m','upper_01_l','upper_00_l','corner_l','lower_00_l','lower_01_l','lower_m','lower_01_r','lower_00_r']
        self.mouthDrivers = ['mouth_'+d+'_driver' for d in driverList]
        
        self.mouthBindmeshesGrp = 'mouth_bindmesh_grp'
        self.mouthBindmeshes = [d.replace('_driver','_bindmesh') for d in self.mouthDrivers]
        
        self.mouthFolGrp = 'mouth_fol_grp'
        self.mouthFols = [d.replace('bindmesh','fol') for d in self.mouthBindmeshes]
        
        self.jawClsGrp = 'jaw_cls_grp'
        self.jawCls = [d.replace('bindmesh','cls') for d in self.mouthBindmeshes]
        
        self.lipCtlGrp = 'lip_ctl_grp'
        self.lipCtls =  [d.replace('fol','ctl').replace('mouth','lip') for d in self.mouthFols]
        self.mouthCtlGrp = 'mouth_ctl_grp'
        self.mMacroFols = [d for d in self.mouthFols if '_m_' in d] #'mouth_upper_m_fol','mouth_lower_m_fol'
        self.mouthCtls = [d.replace('fol','ctl') for d in self.mMacroFols]
        self.mCornerCtlGrp = 'mouth_corner_ctl_grp'
        self.mCornerFols = [d for d in self.mouthFols if '_corner_' in d]
        self.mCornerCtls = [d.replace('fol','ctl') for d in self.mCornerFols]
        self.lipCvCls = [d.replace('lip_','lipCv_').replace('_ctl','_cls') for d in self.lipCtls] #ex) lipCV_corner_r_cls
        
        self.blinkCtlGrp = 'blink_ctl_grp'
        self.blinkCtls = ['blink_upper_r_ctl', 'blink_lower_r_ctl', 'blink_upper_l_ctl', 'blink_lower_l_ctl']
        
        self.mouthBlendCrvGrp = 'mouth_blend_crv_grp'
        suffixList = ['_wide','_small','_smile','_frown']
        self.mouthBlendCrvs = [self.mouthCrv+'_r'+d for d in suffixList]+[self.mouthCrv+'_r'+d for d in suffixList]
        self.mouthBsNode = 'mouth_curve_blend'
        ###
        self.eyeRBlendCrvGrp = 'eye_r_blend_crv_grp'
        self.eyeLBlendCrvGrp = 'eye_l_blend_crv_grp'
        self.eyeRCrvs = [self.lidUpperRCrv, self.lidLowerRCrv]
        self.eyeLCrvs = [self.lidUpperLCrv, self.lidLowerLCrv]
        
        suffixList = ['_open','_closed','_neutral','_mid']
        self.eyeRBlendCrvs = [self.lidUpperRCrv+d for d in suffixList]+[self.lidLowerRCrv+d for d in suffixList]
        self.eyeLBlendCrvs = [self.lidUpperLCrv+d for d in suffixList]+[self.lidLowerLCrv+d for d in suffixList]
                
        nodeNames = ['upper_r_open','upper_r_closed','lower_r_open','lower_r_closed']
        self.eyeRBsNodes = ['lid_'+d+'_blend' for d in nodeNames]
        self.eyeLBsNodes = [d.replace('_r_','_l_') for d in self.eyeRBsNodes]
        ###
        self.eyeLoft = None
        
        self.allCtls = self.lipCtls + self.mouthCtls + self.mCornerCtls + self.blinkCtls
            
    
    def buildMouthRig01(self,_):
        #0:Create Groups
        self.createGrps() 
        
        #1: Generate mouth_curve from lip_curves
        MouthFunc._createMouthCrv(self.mouthCrv, self.lipUpperCrv, self.lipLowerCrv)
        
        #1: Create lip_locs on lip verts & connect to lip_curves
        upperPos = ModFunc._getPosListFromVerts(self.lipUpperVerts)
        ModFunc._createLocsOnCurve(self.lipUpperLocs, upperPos, self.lipUpperCrv, self.lipUpperLocGrp)
        
        lowerPos = ModFunc._getPosListFromVerts(self.lipLowerVerts)
        ModFunc._createLocsOnCurve(self.lipLowerLocs, lowerPos, self.lipLowerCrv, self.lipLowerLocGrp)
        
        #2: Aim constraint lip_locs to jaw_bind
        ModFunc._aimConstLocs(self.lipLocs, self.jawBind, upObj=self.faceLowerBind)
        
        #2: Create lip_bind_jnts && constraint to lip_locs
        ModFunc._createJntsOnLocs(self.lipLocs,self.lipBinds,self.faceLowerBind)
        
        #2: Create mouth drivers
        ModFunc._createJntsOnCVs(self.mouthDrivers, self.mouthCrv,self.mouthDriverGrp) 
        
        #3: Create Bindmeshes on driver
        ModFunc._createBindmeshesOnJnts(self.mouthBindmeshes,self.mouthDrivers,self.mouthBindmeshesGrp)
        
        #4: Create Follicles on Bindmeshes
        ModFunc._createFolsOnBindmeshes(self.mouthFols,self.mouthBindmeshes,self.mouthFolGrp)
        
        #4: Create Clusters on Bindmeshes
        ModFunc._createClsOnBindmeshes(self.jawCls,self.mouthBindmeshes,self.jawClsGrp)
        
        #4: Create Ctrls
            #lip ctrls
        ModFunc._createCtlGrp(self.mouthFols,self.lipCtls,self.lipCtlGrp, size=.3 )
        ModFunc._setOffset(self.lipCtls, t=(0,0,1), r=(90,0,0))
        ModFunc._scaleOrient(self.lipCtls)
        ModFunc._overrideColor(self.lipCtls, color=(1,1,0))
            
            #mouth ctrls
        ModFunc._createCtlGrp(self.mMacroFols, self.mouthCtls, self.mouthCtlGrp, size=.5, shape='square')
        ModFunc._setOffset(self.mouthCtls, t=(0,0,1.5), r=(90,0,0))
        ModFunc._scaleOrient(self.mouthCtls)
        ModFunc._overrideColor(self.mouthCtls, color=(1,1,0))
        
            #corner ctrls
        ModFunc._createCtlGrp(self.mCornerFols, self.mCornerCtls, self.mCornerCtlGrp, size=.5, shape='triangle')
        ModFunc._setOffset(self.mCornerCtls, t=(0,0,1), r=(90,0,0))
        ModFunc._scaleOrient(self.mCornerCtls)
        ModFunc._overrideColor(self.mCornerCtls, color=(1,0,0))
        
        #5: Parent constraint micro nul2 group to macro ctl
        MouthFunc.constMicroToMacro(self.lipCtls)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.mCornerCtls,val=(1,1,1))
    
    def buildMouthRig02(self,_):
        #7: Attach Jaw Clusters to Jaw
        MouthFunc.attachJawCls(self.jawCls, self.mouthCtls, self.faceLowerBind, self.jawBind)
        
        #8: Create lipCV Clusters on lip_curves
        MouthFunc._2CurvCvCls(self.lipCvCls, self.lipUpperCrv, self.lipLowerCrv )
        
        #10: Corner pin, Lip pull
        MouthFunc.setMouthCornerCtls(self.mCornerCtls, self.mouthCtls, self.jawCls, self.faceLowerBind,self.jawBind)
        
        #set lip pull attribute
        for i in self.mCornerCtls:
            cmds.setAttr(i+'.lipOnePull', 0.7)
            cmds.setAttr(i+'.lipTwoPull', 0.9)
            
        
    def buildEyeRig01(self,_):
        #1: Mirror Lid Curves
        ModFunc._mirrorObj(self.lidUpperLCrv, self.lidUpperRCrv)
        ModFunc._mirrorObj(self.lidLowerLCrv, self.lidLowerRCrv)
        
        #2: Create lid locs on lid verts & connect to lid curves
        upperRPos = ModFunc._getPosListFromVerts(self.lidUpperRVerts)
        ModFunc._createLocsOnCurve(self.lidUpperRLocs, upperRPos, self.lidUpperRCrv, self.lidRLocGrp) #names,posList,curv,
        
        upperLPos = ModFunc._mirrorPosX(upperRPos)
        ModFunc._createLocsOnCurve(self.lidUpperLLocs, upperLPos, self.lidUpperLCrv, self.lidLLocGrp)
        
        lowerRPos = ModFunc._getPosListFromVerts(self.lidLowerRVerts)
        ModFunc._createLocsOnCurve(self.lidLowerRLocs, lowerRPos, self.lidLowerRCrv, self.lidRLocGrp, newGrp=False)
        
        lowerLPos = ModFunc._mirrorPosX(lowerRPos)
        ModFunc._createLocsOnCurve(self.lidLowerLLocs, lowerLPos, self.lidLowerLCrv, self.lidLLocGrp, newGrp=False)

        #3: Aim constraint lid locs to eye socket bind
        ModFunc._aimConstLocs(self.lidRLocs,self.eyeSocketBindR)
        ModFunc._aimConstLocs(self.lidLLocs,self.eyeSocketBindL)
        
        #4: Create lid bind jnts
        ModFunc._createJntsOnLocs(self.lidRLocs,self.lidRBinds,self.eyeSocketBindR)
        ModFunc._createJntsOnLocs(self.lidLLocs,self.lidLBinds,self.eyeSocketBindL)
        
        #5: Constraint to lid locs
        ModFunc._parentConstIterate(self.lidRLocs,self.lidRBinds)
        ModFunc._parentConstIterate(self.lidLLocs,self.lidLBinds)
        
        #4: Create Ctrls
            #blink ctrls
        socketBinds = [self.eyeSocketBindR, self.eyeSocketBindR, self.eyeSocketBindL, self.eyeSocketBindL]
        ModFunc._createCtlGrp(socketBinds, self.blinkCtls, self.blinkCtlGrp, size=6, const=False) #drivenList, nameList, grpName, 
        EyeFunc._roatateCtrlShape(self.blinkCtls)
        ModFunc._scaleOrient(self.blinkCtls)
        ModFunc._overrideColor(self.blinkCtls, color=(1,0,0))
        
        '''
        ModFunc._createCtlGrp()
        
        EyeFunc._createLoftBall()
        EyeFunc._SlideOnSurface()
        '''
        
    def BuildMouthBlendshapes01(self,_):
        #1: Duplicate orig curve
        MouthFunc._createBsCrv(self.mouthCrv,self.mouthBlendCrvs,self.mouthBlendCrvGrp)
        #2: Create Blendshape Node
        MouthFunc._createBsNode(self.mouthBsNode, self.mouthCrv, self.mouthBlendCrvs)
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(self.mouthBsNode)
        #4: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.mCornerCtls, self.mouthBlendCrvs, self.mouthBsNode)
            
        
    def BuildEyeBlendshapes01(self,_):
        #1: Duplicate orig curve
        EyeFunc._createBsCrv(self.eyeRCrvs, self.eyeRBlendCrvs, self.eyeRBlendCrvGrp)
        EyeFunc._createBsCrv(self.eyeLCrvs, self.eyeLBlendCrvs, self.eyeLBlendCrvGrp)
        #2: Create Blendshape Node
        EyeFunc._createBsNode(self.eyeRBsNodes, self.eyeRCrvs, self.eyeRBlendCrvs)
        EyeFunc._createBsNode(self.eyeLBsNodes, self.eyeLCrvs, self.eyeLBlendCrvs)
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        #EyeFunc._connectCornerCtrl(self.blinkCtls, self.eyeBlendCrvs, bsNodeList)

    
    def createGrps(self):
        cmds.group(n=self.faceRoot, em=True)
        cmds.group(n=self.animGrp, em=True)
        cmds.group(n=self.rigGrp, em=True)
        cmds.group(n=self.bindGrp, em=True)
        
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
