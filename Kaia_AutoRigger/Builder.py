import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import UI
from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
importlib.reload(UI)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(EyeFunc)
importlib.reload(BrowFunc)

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
        self.faceUpperBind = 'face_upper_bind' #No change this!
        self.faceLowerBind = 'face_lower_bind' #No change this!
        self.jawBind = 'jaw_bind' #No change this!
        self.eyeSocketRBind = 'eye_socket_r_bind' #No change this!
        self.eyeSocketLBind = 'eye_socket_l_bind' #No change this!
        self.eyeBinds = ['eye_r_bind','eye_l_bind'] #No change this!
        self.browCorBinds = ['brow_corrugator_r_bind','brow_corrugator_l_bind']  #No change this!
        
        self.lidCrvs = ['upper_lid_r_curve', 'lower_lid_r_curve', 'upper_lid_l_curve', 'lower_lid_l_curve'] #No change this!
        self.lidDrivCrvs = [d.replace('_curve','_driver_curve') for d in self.lidCrvs] #lid driver curve
        self.lipUpperCrv = 'lip_upper_curve' #No change this!
        self.lipLowerCrv = 'lip_lower_curve' #No change this!
        self.mouthCrv = 'mouth_curve' #No change this!
        
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
        
        self.faceUpperCtl = 'face_upper_ctl'
        self.eyeRotMacroCtl = 'eye_rot_ctl'
        self.eyeMicroCtls = ['eye_r_ctl','eye_l_ctl']
        self.eyeAimMacroCtl = 'eye_aim_ctl'
        self.eyeAimMicroCtls = ['eye_r_aim_ctl','eye_l_aim_ctl']
        self.blinkCtlGrp = 'blink_ctl_grp'
        self.blinkCtls = ['blink_upper_r_ctl', 'blink_lower_r_ctl', 'blink_upper_l_ctl', 'blink_lower_l_ctl']
        
        self.browCtlGrp = 'brow_ctl_grp'
        self.browCtls = ['brow_r_ctl','brow_l_ctl']
        self.browInCtls = ['brow_inner_r_ctl','brow_inner_l_ctl']
        self.browPeakCtls = ['brow_peak_r_ctl','brow_peak_l_ctl']
        
        self.mouthBlendCrvGrp = 'mouth_blend_crv_grp'
        suffixList = ['_wide','_small','_smile','_frown']
        self.mouthBlendCrvs = []
        for suffix in suffixList:
            self.mouthBlendCrvs.append(self.mouthCrv+'_r'+suffix)
            self.mouthBlendCrvs.append(self.mouthCrv+'_l'+suffix)
        self.mouthBsNode = 'mouth_curve_blend'
        ###
        self.eyeRBlendCrvGrp = 'eye_r_blend_crv_grp'
        self.eyeLBlendCrvGrp = 'eye_l_blend_crv_grp'
        
        suffixList = ['_open','_neutral','_mid','_closed']
        self.eyeRBlendCrvs = [self.lidCrvs[0]+d for d in suffixList]+[self.lidCrvs[1]+d for d in suffixList]
        self.eyeLBlendCrvs = [self.lidCrvs[2]+d for d in suffixList]+[self.lidCrvs[2]+d for d in suffixList]
                
        nodeNames = ['upper_r_open','upper_r_closed','lower_r_open','lower_r_closed']
        self.eyeRBsNodes = ['lid_'+d+'_blend' for d in nodeNames]
        self.eyeLBsNodes = [d.replace('_r_','_l_') for d in self.eyeRBsNodes]
        ###
        self.eyeLoft = None
        
        self.allCtls = self.lipCtls + self.mouthCtls + self.mCornerCtls + self.blinkCtls + self.eyeMicroCtls + self.browCtls
    
    def buildRig01(self,_):
        self.createGrps()
        self.face01()
        self.mouth01()
        self.eye01()
        self.brow01()
    
    def buildRig02(self,_):
        self.mouth02()
        self.eye02()
        self.brow02()
        self.mouthBs01()
        self.eyeBs01()
    
    def face01(self):
        #0:Create Face Ctls
            #face upper ctl
        #nulgrp
        #face_upper_ctl
        ModFunc._createCtlGrp([self.faceUpperBind],[self.faceUpperCtl], self.animGrp, newGrp=False, ori=False, size=12 )
        ModFunc._offsetCtls([self.faceUpperCtl], t=(0,0,0), r=(90,0,0))
        ModFunc._overrideColor([self.faceUpperCtl], color=(0,0,1))
    
    def mouth01(self):
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
        ModFunc._offsetCtls(self.lipCtls, t=(0,0,1), r=(90,0,0))
        ModFunc._scaleOrient(self.lipCtls)
        ModFunc._overrideColor(self.lipCtls, color=(1,1,0))
            
            #mouth ctrls
        ModFunc._createCtlGrp(self.mMacroFols, self.mouthCtls, self.mouthCtlGrp, size=.5, shape='square')
        ModFunc._offsetCtls(self.mouthCtls, t=(0,0,1.5), r=(90,0,0))
        ModFunc._scaleOrient(self.mouthCtls)
        ModFunc._overrideColor(self.mouthCtls, color=(1,1,0))
        
            #corner ctrls
        ModFunc._createCtlGrp(self.mCornerFols, self.mCornerCtls, self.mCornerCtlGrp, size=.5, shape='triangle')
        ModFunc._offsetCtls(self.mCornerCtls, t=(0,0,1), r=(90,-30,0))
        ModFunc._scaleOrient(self.mCornerCtls)
        ModFunc._overrideColor(self.mCornerCtls, color=(1,0,0))
        
        #5: Parent constraint micro nul2 group to macro ctl
        MouthFunc.constMicroToMacro(self.lipCtls)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.mCornerCtls,val=(1,1,1))
    
    def mouth02(self):
        #7: Attach Jaw Clusters to Jaw
        MouthFunc.attachJawCls(self.jawCls, self.mouthCtls, self.faceLowerBind, self.jawBind)
        
        #8: Create lipCV Clusters on lip_curves
        MouthFunc._2CurvCvCls(self.lipCvCls, self.lipCtls, self.lipUpperCrv, self.lipLowerCrv )
        
        #10: Corner pin, Lip pull
        MouthFunc.setMouthCornerCtls(self.mCornerCtls, self.mouthCtls, self.jawCls, self.faceLowerBind,self.jawBind)
        
        #set lip pull attribute
        for i in self.mCornerCtls:
            cmds.setAttr(i+'.lipOnePull', 0.7)
            cmds.setAttr(i+'.lipTwoPull', 0.9)
            
        
    def eye01(self):
        #1: Mirror Lid Curves
        ModFunc._mirrorObj(self.lidCrvs[2], self.lidCrvs[0])
        ModFunc._mirrorObj(self.lidCrvs[3], self.lidCrvs[1])
        
        
        #2: Create lid locs on lid verts & connect to lid curves
        upperRPos = ModFunc._getPosListFromVerts(self.lidUpperRVerts)
        ModFunc._createLocsOnCurve(self.lidUpperRLocs, upperRPos, self.lidCrvs[0], self.lidRLocGrp) #names,posList,curv,
        
        upperLPos = ModFunc._mirrorPosX(upperRPos)
        ModFunc._createLocsOnCurve(self.lidUpperLLocs, upperLPos, self.lidCrvs[2], self.lidLLocGrp)
        
        lowerRPos = ModFunc._getPosListFromVerts(self.lidLowerRVerts)
        ModFunc._createLocsOnCurve(self.lidLowerRLocs, lowerRPos, self.lidCrvs[1], self.lidRLocGrp, newGrp=False)
        
        lowerLPos = ModFunc._mirrorPosX(lowerRPos)
        ModFunc._createLocsOnCurve(self.lidLowerLLocs, lowerLPos, self.lidCrvs[3], self.lidLLocGrp, newGrp=False)

        #3: Aim constraint lid locs to eye socket bind
        ModFunc._aimConstLocs(self.lidRLocs,self.eyeSocketRBind)
        ModFunc._aimConstLocs(self.lidLLocs,self.eyeSocketLBind)
        
        #4: Create lid bind jnts
        ModFunc._createJntsOnLocs(self.lidRLocs,self.lidRBinds,self.eyeSocketRBind)
        ModFunc._createJntsOnLocs(self.lidLLocs,self.lidLBinds,self.eyeSocketLBind)
        
        #5: Constraint to lid locs
        ModFunc._parentConstIterate(self.lidRLocs,self.lidRBinds)
        ModFunc._parentConstIterate(self.lidLLocs,self.lidLBinds)
        
        #3: Create Lid Driver Curve
        EyeFunc._createDrivCrv(self.lidDrivCrvs,self.lidCrvs)
        
        #4: Create Lid Ctls
        
        #4: Create blink Ctls
        socketBinds = [self.eyeSocketRBind, self.eyeSocketRBind, self.eyeSocketLBind, self.eyeSocketLBind]
        ModFunc._createCtlGrp(socketBinds, self.blinkCtls, self.blinkCtlGrp, size=6, const=False) #drivenList, nameList, grpName, 
        EyeFunc._roatateCtrlShape(self.blinkCtls)
        ModFunc._scaleOrient(self.blinkCtls)
        ModFunc._overrideColor(self.blinkCtls, color=(1,0,0))
        cmds.parent(self.blinkCtlGrp,self.faceUpperCtl)
        
        #4: Create Eye Ctls
            #eye_rot_ctl
        ModFunc._createCtlGrp([self.eyeSocketLBind], [self.eyeRotMacroCtl], self.faceUpperCtl, newGrp=False, ori=False, const=False, mid=True, size=1, shape='triangle' )
        ModFunc._offsetCtls([self.eyeRotMacroCtl], t=(0,0,7.5), r=(90,0,0))
        ModFunc._overrideColor([self.eyeRotMacroCtl], color=(1,0,0))
                
            #eye_R_ctl, eye_L_ctl
        ModFunc._createCtlGrp(self.eyeBinds, self.eyeMicroCtls, self.faceUpperCtl, newGrp=False, const=False, size=.7 )
        ModFunc._offsetCtls(self.eyeMicroCtls, t=(0,0,6))
        ModFunc._overrideColor(self.eyeMicroCtls, color=(1,1,0))
                
            #eye aim macro ctl
        ModFunc._createCtlGrp([self.eyeSocketLBind], [self.eyeAimMacroCtl], self.faceUpperCtl, newGrp=False, ori=False, const=False, mid=True, size=1, shape='square' )
        ModFunc._offsetCtls([self.eyeAimMacroCtl],r=(0,0,45),s=(7,1,1))
        ModFunc._overrideColor([self.eyeAimMacroCtl], color=(1,1,0))

            #eye aim micro ctls LR
        targList = [self.eyeAimMacroCtl, self.eyeAimMacroCtl]
        ModFunc._createCtlGrp(targList, self.eyeAimMicroCtls, self.eyeAimMacroCtl, newGrp=False, ori=False, const=False, mid=True, size=1 )
        ModFunc._overrideColor(self.eyeAimMicroCtls, color=(1,1,0))
        
        cmds.move(0,0,20,self.eyeAimMacroCtl+'_nul',r=True)
        cmds.move(-3,0,0,self.eyeAimMicroCtls[0]+'_nul',r=True)
        cmds.move(3,0,0,self.eyeAimMicroCtls[1]+'_nul',r=True)
        
        '''
        EyeFunc._createLoftBall()
        EyeFunc._SlideOnSurface()
        '''
        
    def eye02(self):
        #5: Connect Eye Ctls
            #eye rot micro ctls LR
                #nulgrp
                #aimgrp + aim constraint
                #rotgrp + rot connection
                #convergegrp + rot y connection
                #eye_R_Ctl >> parentConst, scaleConst >> eye_r_bind
        
        pass
    
    def brow01(self):
        #2: Create Brow Ctls
            #brow_r_ctl
        browPosLocs = BrowFunc.LocsOnVert(self.browRVert)
        
        ModFunc._createCtlGrp(browPosLocs, self.browCtls, self.browCtlGrp, const=False, size=.7, shape='square' )
        ModFunc._offsetCtls(self.browCtls, r=(0,0,45), s=(5,1,1) )
        ModFunc._scaleOrient(self.browCtls)
        ModFunc._overrideColor(self.browCtls, color=(1,1,0))
        
        cmds.delete(browPosLocs[0],browPosLocs[1])
        
            #orientCompensate
        compensates = BrowFunc._createCompenGrp(self.browCtls)
        
            #brow_inner_r_ctl
        ModFunc._createCtlGrp(compensates, self.browInCtls, self.browCtlGrp, newGrp=False, size=.6, shape='square' )
        ModFunc._offsetCtls(self.browInCtls, r=(0,0,45))
        ModFunc._scaleOrient(self.browInCtls)
        ModFunc._overrideColor(self.browInCtls, color=(1,1,0))
 
            #brow_peak_r_ctl
        ModFunc._createCtlGrp(compensates, self.browPeakCtls, self.browCtlGrp, newGrp=False, size=.6, shape='square' )
        ModFunc._offsetCtls(self.browPeakCtls, r=(0,0,45))
        ModFunc._scaleOrient(self.browPeakCtls)
        ModFunc._overrideColor(self.browPeakCtls, color=(1,1,0))
        
        #for some reason parent constraint flips the child?? I have to set up the offset manually??
        cmds.setAttr(self.browInCtls[1]+'_nul'+'_parentConstraint1.target[0].targetOffsetRotateX', 180)
        cmds.setAttr(self.browPeakCtls[1]+'_nul'+'_parentConstraint1.target[0].targetOffsetRotateX', 180)
        
        cmds.move(0,0,2,self.eyeAimMacroCtl+'_nul',r=True)
        cmds.move(-1,0,0,self.browInCtls[0]+'_orient',r=True)
        cmds.move(1,0,0,self.browInCtls[1]+'_orient',r=True)
        cmds.move(3,0,0,self.browPeakCtls[0]+'_orient',r=True)
        cmds.move(-3,0,0,self.browPeakCtls[1]+'_orient',r=True)

    
    def brow02(self):
        #3: Connect Brow Ctls
        
        #4: Aim Constraint?
        pass
    
    def mouthBs01(self):
        #1: Duplicate orig curve
        MouthFunc._createBsCrv(self.mouthCrv,self.mouthBlendCrvs,self.mouthBlendCrvGrp)
        
        #2: Create Blendshape Node
        MouthFunc._createBsNode(self.mouthBsNode, self.mouthCrv, self.mouthBlendCrvs)
        
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(self.mouthBsNode)
        
        #4: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.mCornerCtls, self.mouthBlendCrvs, self.mouthBsNode)
            
        
    def eyeBs01(self):
        #1: Duplicate orig curve
        EyeFunc._createBsCrv(self.lidCrvs[:2], self.eyeRBlendCrvs, self.eyeRBlendCrvGrp)
        EyeFunc._createBsCrv(self.lidCrvs[2:], self.eyeLBlendCrvs, self.eyeLBlendCrvGrp)
        
        #2: Create Blendshape Node
        EyeFunc._createBsNode(self.eyeRBsNodes, self.lidCrvs[:2], self.eyeRBlendCrvs)
        EyeFunc._createBsNode(self.eyeLBsNodes, self.lidCrvs[2:], self.eyeLBlendCrvs)
        
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        EyeFunc._connectCornerCtrl(self.blinkCtls[:2], self.eyeRBlendCrvs, self.eyeRBsNodes) # first two elements (right ctrls)
        EyeFunc._connectCornerCtrl(self.blinkCtls[2:], self.eyeLBlendCrvs, self.eyeLBsNodes) #last two elements (left ctrls)
        
        #EXTRA: set different color for orig crvs
        eyeCrvs = [self.lidCrvs[0], self.lidCrvs[1], self.lidCrvs[2], self.lidCrvs[3]]
        ModFunc._overrideColor(eyeCrvs,color=(0,1,1))

    
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
