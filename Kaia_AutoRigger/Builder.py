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
class BuildRig(Namer.templateNames):
    def __init__(self):
        pass
    
    def names(self,_):
        self.faceRoot = 'face_root'
        self.animGrp = 'anim_grp'
        self.rigGrp = 'rig_grp'
        self.bindGrp = 'bind_grp'

        self.binds()
        
        self.faceCtl = 'face_ctl'
        self.faceUpperCtl = 'face_upper_ctl'
        self.jawCtl = 'jaw_ctl'
        self.cheekCtlGrp = 'cheek_ctl_grp'
        self.cheekCtls = [d.replace('_bind','_ctl') for d in self.cheekBinds]
        self.cheekDrvs = ['cheek_driver_r_nul','cheek_driver_l_nul']
        
        #execute namer class object
        self.M = Namer.mouth(self.verts)
        self.L = Namer.lid(self.verts)
        self.E = Namer.eye(self.verts)
        self.B = Namer.brow(self.verts)
        self.N = Namer.nose(self.verts)
        
        self.allCtls = self.M.microCtls + self.M.macroCtls + self.M.cornerCtls + self.L.ctls + self.E.ctls + self.B.ctls + [self.jawCtl] + self.N.sneerCtls + self.N.nostrilCtls

        
    def buildRig01(self,_):
        self.createGrps()
        self.face01()
        self.mouth01()
        self.lid01()
        self.eye01()
        self.brow01()
    
    def buildRig02(self,_):
        self.face02()
        self.mouth02()
        self.lid02()
        self.eye02()
        self.brow02()

        self.hideExtra()
        self.arrangeGrps()
    
    def face01(self):
        #0: Create Face Ctls
        ModFunc._createCtlGrp([self.faceBind],[self.faceCtl],self.animGrp, newGrp=False,ori=False,const=False,size=8)
        ModFunc._offsetCtls([self.faceCtl],r=(90,0,0))
        
        #0: Create Upper Face Ctls
        ModFunc._createCtlGrp([self.faceUpperBind],[self.faceUpperCtl], self.faceCtl, newGrp=False, ori=False, const=False, size=12 )
        ModFunc._offsetCtls([self.faceUpperCtl], r=(90,0,0))
        
        ModFunc._overrideColor([self.faceCtl, self.faceUpperCtl], color=(1,1,0))
        
        #0: Create Jaw Ctls
        ModFunc._createCtlGrp([self.jawBind], [self.jawCtl], self.animGrp, newGrp=False, const=False, size=1.5, shape='triangle')
        ModFunc._offsetCtls([self.jawCtl],t=(0,-2,12), r=(180,0,0),s=(-1,.7,1))
        ModFunc._overrideColor([self.jawCtl], color=(1,1,0))
        
        #0: Create Nose Ctls
        ModFunc._createCtlGrp([self.noseBind],[self.N.ctl], self.animGrp,
         newGrp=False, const=False, size=2)
         
        ModFunc._createCtlGrp(self.sneerBinds,self.N.sneerCtls, self.N.ctl,
         newGrp=False, const=False, size=.7, shape='arch')
        ModFunc._offsetCtls(self.N.sneerCtls, t=(0,0,2), s=(.7,.7,.7))
        
        ModFunc._createCtlGrp(self.nostrilBinds,self.N.nostrilCtls, self.N.ctl,
         newGrp=False, const=False, size=.4, shape='pentagon')
        ModFunc._offsetCtls(self.N.nostrilCtls, t=(0,-.6,0), r=(90,0,0))
         
        ModFunc._overrideColor([self.N.ctl]+self.N.sneerCtls+self.N.nostrilCtls, color=(0,1,0))
        
        #0: Create Cheek Ctls
        ModFunc._createCtlGrp(self.cheekBinds, self.cheekCtls, self.cheekCtlGrp, const=False, size=.5 )
        ModFunc._overrideColor(self.cheekCtls, color=(1,1,0))
        
        #scale orient z
        for ctl in self.cheekCtls:
            if '_l_' in ctl:
                cmds.scale(1,1,-1,ctl+'_orient')
        
        cmds.parent(self.cheekCtlGrp,self.faceCtl)
        
        #1: Create Cheek lift jnts
        
    
    def face02(self):
        #1: Parent constraint face upper bind
        cmds.parentConstraint(self.faceUpperCtl,self.faceUpperBind,mo=True)
        
        #1: Parent constraint jaw bind
        cmds.parentConstraint(self.jawCtl,self.jawBind,mo=True)
        cmds.parent(self.jawCtl+'_nul',self.M.bigCtl)
        
        #1: Parent constraint nose binds
        ModFunc._parentConstIterate([self.N.ctl]+self.N.sneerCtls+self.N.nostrilCtls,[self.noseBind]+self.sneerBinds+self.nostrilBinds)
        
        #1: Parent constraint cheek binds
        ModFunc._parentConstIterate(self.cheekCtls,self.cheekBinds)
        #2: Make Cheek joints follow mCorner ctls
        ModFunc._createCheekDrv(self.cheekDrvs,self.M.cornerCtls,self.faceCtl)
        
        ModFunc._createCheekAuto(self.cheekCtls[0:2],self.cheekDrvs,(.1,.5,.1) )
        ModFunc._createCheekAuto(self.cheekCtls[2:4],self.cheekDrvs,(.5,.5,.5))
    
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
        ModFunc._createJntsOnLocs(self.M.locs,self.M.binds,self.faceLowerBind) ###parent change!
        
        #2: Create mouth drivers
        ModFunc._createJntsOnCVs(self.M.drivJnts, self.M.crv,self.M.drivJntGrp) 
        
        #3: Create Bindmeshes on driver
        ModFunc._createBindmeshesOnJnts(self.M.bindmeshes,self.M.drivJnts,self.M.bindmeshesGrp)
        
        #4: Create Follicles on Bindmeshes
        ModFunc._createFolsOnBindmeshes(self.M.fols,self.M.bindmeshes,self.M.folGrp)
        
        #4: Create Clusters on Bindmeshes
        ModFunc._createClsOnBindmeshes(self.M.clus,self.M.bindmeshes,self.M.clusGrp)
        
        #4: Create Ctrls
            #lip micro ctrls
        ModFunc._createCtlGrp(self.M.fols,self.M.microCtls,self.M.microCtlGrp, size=.3 )
        ModFunc._offsetCtls(self.M.microCtls, t=(0,-1,0))

            #lip macro ctrls
        ModFunc._createCtlGrp(self.M.macroFols, self.M.macroCtls, self.M.macroCtlGrp,
         size=1, shape='square')
        ModFunc._offsetCtls(self.M.macroCtls, t=(0,-1.5,0), r=(0,0,45), s=(3,1,1))

            #big ctl
        ModFunc._createCtlGrp([self.faceLowerBind],[self.M.bigCtl], self.faceCtl,
         newGrp=False, const=False, ori=False, size=4, shape='square')
        ModFunc._offsetCtls([self.M.bigCtl], t=(0,-2.5,12), r=(0,0,45), s=(1,.8,1))
            #lip thick ctl
        ModFunc._createCtlGrp(self.M.macroFols,self.M.thickCtls, self.M.thickCtlGrp,
        size=.5, shape='semiCircle')
        ModFunc._offsetCtls(self.M.thickCtls, t=(0,-1.5,0), s=(2.5,1,1))
        cmds.scale(1,1,-1,self.M.thickCtls[1]+'_orient')
            #corner ctrls
        ModFunc._createCtlGrp(self.M.cornerFols, self.M.cornerCtls, self.M.cornerCtlGrp,
         const=False, size=.5, shape='triangle')
        ModFunc._offsetCtls(self.M.cornerCtls, t=(0,-1.5,0), r=(0,0,-30))
        
            ###
        ModFunc._overrideColor(self.M.microCtls, color=(1,1,0))
        ModFunc._overrideColor(self.M.macroCtls+[self.M.bigCtl]+self.M.thickCtls+self.M.cornerCtls, color=(1,0,0))
        ModFunc._scaleOrient(self.M.microCtls+self.M.macroCtls+self.M.thickCtls+self.M.cornerCtls)
        ModFunc._90dOrient(self.M.microCtls+self.M.macroCtls+self.M.thickCtls+self.M.cornerCtls)
        
        #5: Parent constraint micro nul2 group to macro ctl
        MouthFunc.constMicroToMacro(self.M.microCtls)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.M.cornerCtls,val=(3,3,3))
    
    def mouth02(self):
        #6: Parent Constraint mouth bind
        cmds.parentConstraint(self.M.bigCtl,self.faceLowerBind)
            
        #7: Attach Jaw Clusters to Jaw
        MouthFunc.attachJawCls(self.M.clus, self.M.macroCtls, self.faceLowerBind, self.jawBind)
        
        #8: Create lipCV Clusters on lip_curves
        MouthFunc._2CurvCvCls(self.M.cvCls, self.M.microCtls, self.M.upperCrv, self.M.lowerCrv )
        
        #9: parent constraint corner ctl nul to jaw
        MouthFunc.attachCornerCtls(self.M.cornerCtls, self.faceLowerBind, self.jawBind)
        
        #10: Corner pin, Lip pull
        MouthFunc.setMouthCornerCtls(self.M.cornerCtls, self.M.macroCtls, self.M.clus, self.faceLowerBind,self.jawBind)
        
        #set lip pull attribute
        for i in self.M.cornerCtls:
            cmds.setAttr(i+'.lipOnePull', 0.7)
            cmds.setAttr(i+'.lipTwoPull', 0.9)
            
            ###Mouth crv blendshapes
        #1: Duplicate orig curve
        MouthFunc._createBsCrv(self.M.crv,self.M.blendCrvs,self.M.blendCrvGrp)
        
        #2: Create Blendshape Node
        MouthFunc._createBsNode(self.M.bsNode, self.M.crv, self.M.blendCrvs)
        
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(self.M.bsNode)
        
        #4: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.M.cornerCtls, self.M.blendCrvs, self.M.bsNode)
 
        
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

        #5: Create Lid Driver Joints
        for num,crv in enumerate(self.L.drivCrvs):
            LidFunc._createDrivJnts(self.L.drivJnts[num*5:num*5+5],crv) #0,1,2,3,4
        
        #4: Create Lid tweak Ctls
        ModFunc._createCtlGrp(self.L.drivJnts, self.L.microCtls, self.L.microCtlGrp, ori=False, const=False, size=.3)
        ModFunc._offsetCtls(self.L.microCtls, t=(0,0,.7))
        ModFunc._overrideColor(self.L.microCtls, color=(1,1,0))
        cmds.parent(self.L.microCtlGrp,self.faceUpperCtl)
        
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
        ModFunc._overrideColor(self.L.ctls, color=(0,0,1))
        cmds.parent(self.L.ctlGrp,self.faceUpperCtl)
        
    def lid02(self):
            ###lid crv blendshapes
        #1: Duplicate orig curve
        LidFunc._createBsCrv(self.L.crvs[:2], self.L.rBlendCrvs, self.L.rBlendCrvGrp)
        LidFunc._createBsCrv(self.L.crvs[2:], self.L.lBlendCrvs, self.L.lBlendCrvGrp)
        
        #2: Create Blendshape Node
        LidFunc._createBsNode(self.L.rBsNodes, self.L.drivCrvs[:2], self.L.rBlendCrvs)
        LidFunc._createBsNode(self.L.lBsNodes, self.L.drivCrvs[2:], self.L.lBlendCrvs)
        
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        LidFunc._connectCornerCtrl(self.L.ctls[:2], self.L.rBlendCrvs, self.L.rBsNodes) # first two elements (right ctrls)
        LidFunc._connectCornerCtrl(self.L.ctls[2:], self.L.lBlendCrvs, self.L.lBsNodes) #last two elements (left ctrls)
        
    
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
        ModFunc._overrideColor([self.E.aimCtl], color=(0,0,1))

            #eye aim micro ctls LR
        targList = [self.E.aimCtl, self.E.aimCtl]
        ModFunc._createCtlGrp(targList, self.E.aimMicroCtls, self.E.aimCtl, 
        newGrp=False, ori=False, const=False, mid=True, size=1 )
        ModFunc._overrideColor(self.E.aimMicroCtls, color=(0,0,1))
        
            ###initial offset
        cmds.move(0,0,20,self.E.aimCtl+'_nul',r=True)
        cmds.move(-3,0,0,self.E.aimMicroCtls[0]+'_nul',r=True)
        cmds.move(3,0,0,self.E.aimMicroCtls[1]+'_nul',r=True)
        
            #pupil ctl
        ModFunc._createCtlGrp(self.E.ctls, self.E.pupilCtls, self.faceUpperCtl,
        newGrp=False, const=False, ori=False, shape='pentagon', size=.5)
        ModFunc._overrideColor(self.E.pupilCtls, color=(0,0,1))
        
    def eye02(self):
        #5: Connect Eye Ctls
        EyeFunc._connectEyeCtls(self.E.ctls, self.E.rotCtl, self.E.aimCtl, self.E.aimMicroCtls, self.eyeBinds)
        
        #note: create pupil joints!
        pupilNuls = [self.E.pupilCtls[0]+'_nul', self.E.pupilCtls[1]+'_nul']
        ModFunc._parentIterate(self.E.ctls,pupilNuls)
        
    def brow01(self):
        #2: Create Brow Ctls
            #brow_r_ctl
        browPosLocs = BrowFunc.LocsOnVert(self.verts['browR'])
        
        ModFunc._createCtlGrp(browPosLocs, self.B.ctls, self.B.ctlGrp, const=False, size=.7, shape='square' )
        ModFunc._offsetCtls(self.B.ctls, r=(0,0,45), s=(5,1,1) )
        ModFunc._scaleOrient(self.B.ctls)
        ModFunc._overrideColor(self.B.ctls, color=(1,1,0))
        cmds.parent(self.B.ctlGrp, self.faceUpperCtl)
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
        cmds.move(3,0,0,self.B.inCtls[0]+'_orient',r=True)
        cmds.move(-3,0,0,self.B.inCtls[1]+'_orient',r=True)
        cmds.move(-1,0,0,self.B.peakCtls[0]+'_orient',r=True)
        cmds.move(1,0,0,self.B.peakCtls[1]+'_orient',r=True)
        
        #3: Create Custom Attributes for Brow Ctls
        BrowFunc._createFollowAttr(self.B.ctls)
        BrowFunc._createFollowAttr(self.B.inCtls)
        BrowFunc._createFollowAttr(self.B.peakCtls)
        
        #4: Create brow local Driver under ctl nul
        pos = cmds.xform(self.verts['browR'],q=True,t=True,ws=True)
        parents = [self.B.ctls[0]+'_nul', self.B.ctls[1]+'_nul']
        BrowFunc._createLocalDrv(self.B.ctls,self.B.localDrv,pos,parents)
        BrowFunc._createLocalDrv(self.B.inCtls,self.B.inLocalDrv,pos,parents)
        BrowFunc._createLocalDrv(self.B.peakCtls,self.B.peakLocalDrv,pos,parents)
            
        #5: Create brow Driver
        pos = cmds.xform(self.browBinds[0],q=True,t=True,ws=True)
        cmds.group(n=self.B.xfGrp,em=True)
        cmds.parentConstraint(self.faceUpperBind,self.B.xfGrp,mo=False)
        cmds.scaleConstraint(self.faceUpperBind,self.B.xfGrp,mo=False)
        
        BrowFunc._createDrv(self.B.ctls,self.B.drv,pos,self.B.xfGrp)
        BrowFunc._createDrv(self.B.inCtls,self.B.inDrv,pos,self.B.xfGrp)
        BrowFunc._createDrv(self.B.peakCtls,self.B.peakDrv,pos,self.B.xfGrp)
        
        #6: Create Brow Meat jnts
        
    def brow02(self):
        #6: Connect Brow Ctls to Brow Drivers
        wuo = self.faceUpperCtl
        BrowFunc._connectBrowCtls(self.B.ctls,self.B.localDrv,self.B.drv,self.browBinds,wuo)
        BrowFunc._connectBrowCtls(self.B.inCtls,self.B.inLocalDrv,self.B.inDrv,self.browInBinds,wuo)
        BrowFunc._connectBrowCtls(self.B.peakCtls,self.B.peakLocalDrv,self.B.peakDrv,self.browPeakBinds,wuo)
        
        #7: Connect Main Follow Y to Inner Follow Y:
        for main,inner,peak in zip(self.B.ctls,self.B.inCtls,self.B.peakCtls):
            cmds.connectAttr(main+'.followY',inner+'.followY')
            cmds.connectAttr(main+'.followY',peak+'.followY')
    
        #EXTRA: Set Follow Attr (hard coding)
        cmds.setAttr(self.B.ctls[0]+'.followY',0,.5,0,type='double3')
        cmds.setAttr(self.B.ctls[0]+'.followZ',.348,0,.937,type='double3')
        cmds.setAttr(self.B.ctls[1]+'.followY',0,.5,0,type='double3')
        cmds.setAttr(self.B.ctls[1]+'.followZ',-.348,0,.937,type='double3')
            
    def hideExtra(self):
        cmds.select(self.M.drivJnts,self.M.clus,self.M.cvCls,self.L.drivJnts)
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
                self.M.bindmeshesGrp,self.M.clusGrp, self.M.folGrp,
                self.M.drivJntGrp,
                self.M.blendCrvGrp, self.L.rBlendCrvGrp, self.L.lBlendCrvGrp,
                self.B.xfGrp,
                self.rigGrp)
        except: print('rig_grp parent skipped')
        
        try:
            cmds.parent(
                self.M.microCtlGrp, self.M.macroCtlGrp, self.M.cornerCtlGrp,
                self.M.thickCtlGrp,
                self.animGrp)
        except: print('anim_grp parent skipped')
        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
