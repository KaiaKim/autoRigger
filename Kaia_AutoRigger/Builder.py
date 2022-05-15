import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import Namer
from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import LidFunc
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
importlib.reload(Namer)
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(LidFunc)
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

        self.faceUpperCtl = 'face_upper_ctl'

        #execute namer class object
        self.M = Namer.mouth(self.verts)
        self.L = Namer.lid(self.verts)
        self.E = Namer.eye(self.verts)
        self.B = Namer.brow(self.verts)
        
        self.allCtls = self.M.microCtls + self.M.macroCtls + self.M.cornerCtls + self.L.ctls + self.E.ctls + self.B.ctls

        
    def buildRig01(self,_):
        self.createGrps()
        self.face01()
        self.mouth01()
        self.lid01()
        self.eye01()
        self.brow01()
    
    def buildRig02(self,_):
        self.mouth02()
        self.eye02()
        self.brow02()
        self.mouthBs01()
        self.lidBs01()
        
        self.hideExtra()
        self.arrangeGrps()
    
    def face01(self):
        #0:Create Face Ctls
        ModFunc._createCtlGrp([self.faceUpperBind],[self.faceUpperCtl], self.animGrp, newGrp=False, ori=False, size=12 )
        ModFunc._offsetCtls([self.faceUpperCtl], t=(0,0,0), r=(90,0,0))
        ModFunc._overrideColor([self.faceUpperCtl], color=(1,1,0))
    
    def mouth01(self):
        #1: Generate mouth_curve from lip_curves
        MouthFunc._createMouthCrv(self.M.crv, self.M.upperCrv, self.M.lowerCrv)
        
        #1: Create lip_locs on lip verts & connect to lip_curves
        upperPos = ModFunc._getPosListFromVerts(self.verts['lipUpper'])
        ModFunc._createLocsOnCurve(self.M.upperLocs, upperPos, self.M.upperCrv, self.M.upperLocGrp)
        
        lowerPos = ModFunc._getPosListFromVerts(self.verts['lipLower'])
        ModFunc._createLocsOnCurve(self.M.lowerLocs, lowerPos, self.M.lowerCrv, self.M.lowerLocGrp)
        
        #2: Aim constraint lip_locs to jaw_bind
        ModFunc._aimConstLocs(self.M.locs, self.jawBind, upObj=self.faceLowerBind)
        
        #2: Create lip_bind_jnts && constraint to lip_locs
        ModFunc._createJntsOnLocs(self.M.locs,self.M.binds,self.faceLowerBind)
        
        #2: Create mouth drivers
        ModFunc._createJntsOnCVs(self.M.drivJnts, self.M.crv,self.M.drivJntGrp) 
        
        #3: Create Bindmeshes on driver
        ModFunc._createBindmeshesOnJnts(self.M.bindmeshes,self.M.drivJnts,self.M.bindmeshesGrp)
        
        #4: Create Follicles on Bindmeshes
        ModFunc._createFolsOnBindmeshes(self.M.fols,self.M.bindmeshes,self.M.folGrp)
        
        #4: Create Clusters on Bindmeshes
        ModFunc._createClsOnBindmeshes(self.M.jawCls,self.M.bindmeshes,self.M.jawClsGrp)
        
        #4: Create Ctrls
            #lip ctrls
        ModFunc._createCtlGrp(self.M.fols,self.M.microCtls,self.M.microCtlGrp, size=.3 )
        ModFunc._offsetCtls([d for d in self.M.microCtls if 'upper' in d or 'corner' in d], t=(0,-1,0)) #upper
        ModFunc._offsetCtls([d for d in self.M.microCtls if 'lower' in d], t=(0,1,0)) #lower
        ModFunc._90dOrient(self.M.microCtls)
        ModFunc._scaleOrient(self.M.microCtls)
        ModFunc._overrideColor(self.M.microCtls, color=(1,1,0))
            
            #mouth ctrls
        ModFunc._createCtlGrp(self.M.macroFols, self.M.macroCtls, self.M.macroCtlGrp, size=.5, shape='square')
        ModFunc._offsetCtls([self.M.macroCtls[0]], t=(0,-1.5,0)) #upper
        ModFunc._offsetCtls([self.M.macroCtls[1]], t=(0,1.5,0)) #lower
        ModFunc._90dOrient(self.M.macroCtls)
        ModFunc._scaleOrient(self.M.macroCtls)
        ModFunc._overrideColor(self.M.macroCtls, color=(1,1,0))
        
            #corner ctrls
        ModFunc._createCtlGrp(self.M.cornerFols, self.M.cornerCtls, self.M.cornerCtlGrp, const=False, size=.5, shape='triangle')
        ModFunc._offsetCtls(self.M.cornerCtls, t=(0,-1.5,0), r=(0,0,-30))
        ModFunc._90dOrient(self.M.cornerCtls)
        ModFunc._scaleOrient(self.M.cornerCtls)
        ModFunc._overrideColor(self.M.cornerCtls, color=(1,0,0))

        #5: Parent constraint micro nul2 group to macro ctl
        MouthFunc.constMicroToMacro(self.M.microCtls)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.M.cornerCtls,val=(3,3,3))
    
    def mouth02(self):
        #7: Attach Jaw Clusters to Jaw
        MouthFunc.attachJawCls(self.M.jawCls, self.M.macroCtls, self.faceLowerBind, self.jawBind)
        
        #8: Create lipCV Clusters on lip_curves
        MouthFunc._2CurvCvCls(self.M.cvCls, self.M.microCtls, self.M.upperCrv, self.M.lowerCrv )

        #9: parent constraint corner ctl nul to jaw
            ###
        MouthFunc.attachCornerCtls(self.M.cornerCtls, self.faceLowerBind, self.jawBind)
        
        #10: Corner pin, Lip pull
        MouthFunc.setMouthCornerCtls(self.M.cornerCtls, self.M.macroCtls, self.M.jawCls, self.faceLowerBind,self.jawBind)
        
        #set lip pull attribute
        for i in self.M.cornerCtls:
            cmds.setAttr(i+'.lipOnePull', 0.7)
            cmds.setAttr(i+'.lipTwoPull', 0.9)
            
        
    def lid01(self):
        #1: Mirror Lid Curves
        ModFunc._mirrorObj(self.L.crvs[2], self.L.crvs[0])
        ModFunc._mirrorObj(self.L.crvs[3], self.L.crvs[1])
        
        #2: Create lid locs on lid verts & connect to lid curves
        upperRPos = ModFunc._getPosListFromVerts(self.verts['lidUpperR'])
        ModFunc._createLocsOnCurve(self.L.upperRLocs, upperRPos, self.L.crvs[0], self.L.rLocGrp) #names,posList,curv,
        
        upperLPos = ModFunc._mirrorPosX(upperRPos)
        ModFunc._createLocsOnCurve(self.L.upperLLocs, upperLPos, self.L.crvs[2], self.L.lLocGrp)
        
        lowerRPos = ModFunc._getPosListFromVerts(self.verts['lidLowerR'])
        ModFunc._createLocsOnCurve(self.L.lowerRLocs, lowerRPos, self.L.crvs[1], self.L.rLocGrp, newGrp=False)
        
        lowerLPos = ModFunc._mirrorPosX(lowerRPos)
        ModFunc._createLocsOnCurve(self.L.lowerLLocs, lowerLPos, self.L.crvs[3], self.L.lLocGrp, newGrp=False)

        #3: Aim constraint lid locs to eye socket bind
        ModFunc._aimConstLocs(self.L.rLocs,self.eyeSocketRBind)
        ModFunc._aimConstLocs(self.L.lLocs,self.eyeSocketLBind)
        
        #4: Create lid bind jnts
        ModFunc._createJntsOnLocs(self.L.rLocs,self.L.rBinds,self.eyeSocketRBind)
        ModFunc._createJntsOnLocs(self.L.lLocs,self.L.lBinds,self.eyeSocketLBind)
        
        #5: Constraint to lid locs
        ModFunc._parentConstIterate(self.L.rLocs,self.L.rBinds)
        ModFunc._parentConstIterate(self.L.lLocs,self.L.lBinds)
        
        #3: Create Lid Driver Curve
        LidFunc._createDrivCrv(self.L.drivCrvs,self.L.crvs)
        
        ###
        #5: Create Lid Driver Joints
        for num,crv in enumerate(self.L.drivCrvs):
            LidFunc._createDrivJnts(self.L.drivJnts[num*5:num*5+5],crv) #0,1,2,3,4
        
        #4: Create Lid tweak Ctls
        ModFunc._createCtlGrp(self.L.drivJnts, self.L.microCtls, self.L.microCtlGrp, ori=False, const=False, size=.3)
        ModFunc._offsetCtls(self.L.microCtls, t=(0,0,.7))
        ModFunc._overrideColor(self.L.microCtls, color=(1,1,0))
        
        #5: attach lid tweak ctl nuls to driver crvs
        for num,crv in enumerate(self.L.drivCrvs):
            LidFunc._attachLidCtls(self.L.microCtls[num*5:num*5+5],crv)
        
        #5: parent lid Drivers to lid tweak ctls
        ModFunc._parentIterate(self.L.microCtls,self.L.drivJnts)
        
        #6: Skin Driver joints to lid curves
        for num,crv in enumerate(self.L.crvs):
            LidFunc._skinCrv(self.L.drivJnts[num*5:num*5+5],crv) #0,1,2,3,4
        
        
        #4: Create blink Ctls
        socketBinds = [self.eyeSocketRBind, self.eyeSocketRBind, self.eyeSocketLBind, self.eyeSocketLBind]
        ModFunc._createCtlGrp(socketBinds, self.L.ctls, self.L.ctlGrp, size=1, shape='arch', const=False)
        ModFunc._offsetCtls(self.L.ctls[:2], t=(0,0,7), s=(1.2,-.7,1)) #r
        ModFunc._offsetCtls(self.L.ctls[2:], t=(0,0,7), s=(1.2,.7,1)) #l
        cmds.scale(1,-1,1,self.L.ctls[0]+'_orient') #lower_r
        cmds.scale(1,-1,1,self.L.ctls[3]+'_orient') #upper_l
        ModFunc._overrideColor(self.L.ctls, color=(1,0,0))
        cmds.parent(self.L.ctlGrp,self.faceUpperCtl)
        
    def lid02(self):
        pass
    
    def eye01(self):
        #4: Create Eye Ctls
            #eye_rot_ctl
        ModFunc._createCtlGrp([self.eyeSocketLBind], [self.E.rotCtl], self.faceUpperCtl, 
        newGrp=False, ori=False, const=False, mid=True, size=1, shape='triangle' )
        ModFunc._offsetCtls([self.E.rotCtl], t=(0,0,7.5), r=(90,0,0))
        ModFunc._overrideColor([self.E.rotCtl], color=(0,0,1))
                
            #eye_R_ctl, eye_L_ctl
        ModFunc._createCtlGrp(self.eyeBinds, self.E.ctls, self.faceUpperCtl, 
        newGrp=False, const=False, size=.7 )
        ModFunc._offsetCtls(self.E.ctls, t=(0,0,6))
        ModFunc._overrideColor(self.E.ctls, color=(0,0,1))
                
            #eye aim macro ctl
        ModFunc._createCtlGrp([self.eyeSocketLBind], [self.E.aimCtl], self.faceUpperCtl, 
        newGrp=False, ori=False, const=False, mid=True, size=1, shape='square' )
        ModFunc._offsetCtls([self.E.aimCtl],r=(0,0,45),s=(7,1,1))
        ModFunc._overrideColor([self.E.aimCtl], color=(1,1,0))

            #eye aim micro ctls LR
        targList = [self.E.aimCtl, self.E.aimCtl]
        ModFunc._createCtlGrp(targList, self.E.aimMicroCtls, self.E.aimCtl, 
        newGrp=False, ori=False, const=False, mid=True, size=1 )
        ModFunc._overrideColor(self.E.aimMicroCtls, color=(1,1,0))
        
        cmds.move(0,0,20,self.E.aimCtl+'_nul',r=True)
        cmds.move(-3,0,0,self.E.aimMicroCtls[0]+'_nul',r=True)
        cmds.move(3,0,0,self.E.aimMicroCtls[1]+'_nul',r=True)
        
        '''
        LidFunc._createLoftBall()
        LidFunc._SlideOnSurface()
        '''
        
    def eye02(self):
        #5: Connect Eye Ctls
        EyeFunc._connectEyeCtls(self.E.ctls, self.E.rotCtl, self.E.aimCtl, self.E.aimMicroCtls, self.eyeBinds)
        
                
        pass
    
    def brow01(self):
        #2: Create Brow Ctls
            #brow_r_ctl
        browPosLocs = BrowFunc.LocsOnVert(self.verts['browR'])
        
        ModFunc._createCtlGrp(browPosLocs, self.B.ctls, self.B.ctlGrp, const=False, size=.7, shape='square' )
        ModFunc._offsetCtls(self.B.ctls, r=(0,0,45), s=(5,1,1) )
        ModFunc._scaleOrient(self.B.ctls)
        ModFunc._overrideColor(self.B.ctls, color=(1,1,0))
        
        cmds.delete(browPosLocs[0],browPosLocs[1])
        
            #orientCompensate
        compensates = BrowFunc._createCompenGrp(self.B.ctls)
        
            #brow_inner_r_ctl
        ModFunc._createCtlGrp(compensates, self.B.inCtls, self.B.ctlGrp, newGrp=False, size=.6, shape='square' )
        ModFunc._offsetCtls(self.B.inCtls, r=(0,0,45))
        ModFunc._scaleOrient(self.B.inCtls)
        ModFunc._overrideColor(self.B.inCtls, color=(1,1,0))
 
            #brow_peak_r_ctl
        ModFunc._createCtlGrp(compensates, self.B.peakCtls, self.B.ctlGrp, newGrp=False, size=.6, shape='square' )
        ModFunc._offsetCtls(self.B.peakCtls, r=(0,0,45))
        ModFunc._scaleOrient(self.B.peakCtls)
        ModFunc._overrideColor(self.B.peakCtls, color=(1,1,0))
        
        #for some reason parent constraint flips the child?? I have to set up the offset manually??
        cmds.setAttr(self.B.inCtls[1]+'_nul'+'_parentConstraint1.target[0].targetOffsetRotateX', 180)
        cmds.setAttr(self.B.peakCtls[1]+'_nul'+'_parentConstraint1.target[0].targetOffsetRotateX', 180)
        
        cmds.move(0,0,2,self.E.aimCtl+'_nul',r=True)
        cmds.move(-1,0,0,self.B.inCtls[0]+'_orient',r=True)
        cmds.move(1,0,0,self.B.inCtls[1]+'_orient',r=True)
        cmds.move(3,0,0,self.B.peakCtls[0]+'_orient',r=True)
        cmds.move(-3,0,0,self.B.peakCtls[1]+'_orient',r=True)

    
    def brow02(self):
        #3: Connect Brow Ctls
        
        #4: Aim Constraint?
        pass
    
    def mouthBs01(self):
        #1: Duplicate orig curve
        MouthFunc._createBsCrv(self.M.crv,self.M.blendCrvs,self.M.blendCrvGrp)
        
        #2: Create Blendshape Node
        MouthFunc._createBsNode(self.M.bsNode, self.M.crv, self.M.blendCrvs)
        
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(self.M.bsNode)
        
        #4: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.M.cornerCtls, self.M.blendCrvs, self.M.bsNode)
            
        
    def lidBs01(self):
        #1: Duplicate orig curve
        LidFunc._createBsCrv(self.L.crvs[:2], self.L.rBlendCrvs, self.L.rBlendCrvGrp)
        LidFunc._createBsCrv(self.L.crvs[2:], self.L.lBlendCrvs, self.L.lBlendCrvGrp)
        
        #2: Create Blendshape Node
        LidFunc._createBsNode(self.L.rBsNodes, self.L.drivCrvs[:2], self.L.rBlendCrvs)
        LidFunc._createBsNode(self.L.lBsNodes, self.L.drivCrvs[2:], self.L.lBlendCrvs)
        
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        LidFunc._connectCornerCtrl(self.L.ctls[:2], self.L.rBlendCrvs, self.L.rBsNodes) # first two elements (right ctrls)
        LidFunc._connectCornerCtrl(self.L.ctls[2:], self.L.lBlendCrvs, self.L.lBsNodes) #last two elements (left ctrls)
        
    def hideExtra(self):
        cmds.select(self.M.drivJnts,self.M.jawCls,self.M.cvCls,self.L.drivJnts)
        cmds.hide()

    
    def createGrps(self):
        cmds.group(n=self.faceRoot, em=True)
        cmds.group(n=self.animGrp, em=True)
        cmds.group(n=self.rigGrp, em=True)
        cmds.group(n=self.bindGrp, em=True)
        
    def arrangeGrps(self):
        #these are rather simple parent commands, we keep going even if there's an error.
        try:
            cmds.parent(self.animGrp,self.rigGrp,self.bindGrp,self.faceRoot)
        except: print('face_grp parent skipped')
        
        try:
            cmds.parent(self.faceBind, self.bindGrp)
        except: print('face_grp parent skipped')
        
        try:
            cmds.parent(
                self.M.upperCrv, self.M.lowerCrv,
                self.M.upperLocGrp, self.M.lowerLocGrp,
                self.L.rLocGrp, self.L.lLocGrp,
                self.M.crv,
                self.M.bindmeshesGrp,self.M.jawClsGrp, self.M.folGrp,
                self.M.drivJntGrp,
                self.M.blendCrvGrp, self.L.rBlendCrvGrp, self.L.lBlendCrvGrp,
                self.rigGrp)
        except: print('rig_grp parent skipped')
        
        try:
            cmds.parent(
                self.M.microCtlGrp, self.M.macroCtlGrp, self.M.cornerCtlGrp,
                self.L.microCtlGrp, self.B.ctlGrp,
                self.animGrp)
        except: print('anim_grp parent skipped')
        
        
        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
