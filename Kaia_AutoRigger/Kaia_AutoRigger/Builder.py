import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import DataFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import LidFunc
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
from Kaia_AutoRigger import opmBaker
importlib.reload(ModFunc)
importlib.reload(DataFunc)
importlib.reload(MouthFunc)
importlib.reload(LidFunc)
importlib.reload(BrowFunc)
importlib.reload(opmBaker)

###-----------------------------------------------------CLASS---------------------------------------------------
class BuildCtls():
    def __init__(self):
        pass
        
    def buildRig01(self,_):
        self.createGrps()
        self.face01()
        self.mouth01()
        self.lid01()
        #self.eye01()
        self.brow01()
        self.nose01()
        
        DataFunc._applyTransform(self.data['orients'])
        DataFunc._applyTransform(self.data['bsCrv'], os=True)
    
    def deleteRig01(self,_):
        pass
    
    def face01(self):
        #0: Create Face Ctls
        ModFunc._createCtlGrp(self.J.faceBind,self.faceCtl,self.animGrp, ori=False,size=8)
        ModFunc._offsetCtls(self.faceCtl,r=(90,0,0))
        
        #0: Create Upper Face Ctls
        ModFunc._createCtlGrp(self.J.faceUpBind,self.faceUpCtl, self.faceCtl,  ori=False,  size=12 )
        ModFunc._offsetCtls(self.faceUpCtl, r=(90,0,0))
        
        #0: Create Lower Face Ctls
        ModFunc._createCtlGrp(self.J.faceLoBind, self.faceLoCtl, self.faceCtl,  ori=False,  size=12, shape='square' )
        ModFunc._offsetCtls(self.faceLoCtl, r=(90,0,0))
        
        ModFunc._overrideColor([self.faceUpCtl, self.faceLoCtl], color=(1,1,0))
        
        #0: Create Jaw Ctls
        ModFunc._createCtlGrp(self.J.jawBind, self.jawCtl, self.faceLoCtl,   size=1.5, shape='triangle')
        ModFunc._offsetCtls(self.jawCtl,t=(0,-2,12), r=(180,0,0),s=(-1,.7,1))
        ModFunc._overrideColor(self.jawCtl, color=(1,1,0))
        
        #0: Create Cheek Ctls
        ModFunc._createCtlGrp(self.J.cheekBinds, self.cheekCtls, self.cheekCtlGrp,  size=.5 )
        ModFunc._overrideColor(self.cheekCtls, color=(1,1,0))
        
        #scale orient z
        for ctl in self.cheekCtls:
            if '_l_' in ctl:
                cmds.scale(1,1,-1,ctl+'_orient')
        
        cmds.parent(self.cheekCtlGrp,self.faceCtl)
        
    
    def mouth01(self):
        #1: Generate mouth_curve from lip_curves
        MouthFunc._createMouthCrv(self.M.crv, self.M.upperCrv, self.M.lowerCrv)
        
        #1: Create lip_locs on lip verts & connect to lip_curves
        upperPos = ModFunc._getPosListFromVerts(self.data['verts']['lipUpper'])
        ModFunc._createBindsOnCrv(self.M.binds, upperPos, self.M.upperCrv, self.M.upperBindGrp)
        lowerPos = ModFunc._getPosListFromVerts(self.data['verts']['lipLower'])
        ModFunc._createBindsOnCrv(self.M.binds, lowerPos, self.M.lowerCrv, self.M.lowerBindGrp)

        #2: Create mouth drivers
        MouthFunc._createMouthDrivers(self.M.drivs, self.M.crv,self.M.drivGrp) 
        
        #3: Create Bindmeshes on driver
        MouthFunc._createBindmeshesOnJnts(self.M.bindmeshes,self.M.drivs,self.M.bindmeshesGrp)
        
        #4: Create Follicles on Bindmeshes
        MouthFunc._createFolsOnBindmeshes(self.M.fols,self.M.bindmeshes,self.M.folGrp)
        
        #4: Create Clusters on Bindmeshes
            #big clus
        MouthFunc._createClsOnAll(self.M.clus, self.M.bindmeshes)
            #jaw clus
        upWeights = [.7,.9,1,.9,.7]
        MouthFunc._createClsOnAll(self.M.jawClus[0], self.M.bindmeshes[1:6], weights=upWeights) #upper
        loWeights = [.7,.9,1,.9,.7]
        MouthFunc._createClsOnAll(self.M.jawClus[1], self.M.bindmeshes[7:], weights=loWeights) #lower
            #corner clus
        MouthFunc._createClsOnEach(self.M.cornerClus,[self.M.bindmeshes[0],self.M.bindmeshes[6]])
            #lip clus
        MouthFunc._createClsOnEach(self.M.lipClus,self.M.bindmeshes)
        
        cmds.group(self.M.clus,self.M.jawClus,self.M.cornerClus,self.M.lipClus, n=self.M.clusGrp)
        
        #4: Create Ctrls
            #lip micro ctrls
        ModFunc._createCtlGrp(self.M.fols,self.M.microCtls,self.M.microCtlGrp, size=.3, opm=True )
        ModFunc._offsetCtls(self.M.microCtls, t=(0,-1,0))

            #lip macro ctrls
        ModFunc._createCtlGrp(self.M.macroFols, self.M.macroCtls, self.M.macroCtlGrp,
         size=1, shape='square')
        ModFunc._offsetCtls(self.M.macroCtls, t=(0,-1.5,0), r=(0,0,45), s=(3,1,1))

            #big ctl
        ModFunc._createCtlGrp(self.J.faceLoBind,self.M.ctl, self.faceLoCtl,
           ori=False, size=4, shape='square')
        ModFunc._offsetCtls(self.M.ctl, t=(0,-4.5,12), r=(0,0,45), s=(1,.8,1))

            #corner ctrls
        ModFunc._createCtlGrp(self.M.cornerFols, self.M.cornerCtls, self.M.ctl,
          size=.5, shape='triangle')
        ModFunc._offsetCtls(self.M.cornerCtls, t=(0,-1.5,0), r=(0,0,-30))
            #teeth ctrls
        jawTipList = [self.J.jawTipBind, self.J.jawTipBind]
        ModFunc._createCtlGrp(jawTipList,self.M.teethCtls,self.faceCtl,
           size=1, shape='semiCircle')
        for i,ctl in enumerate(self.M.teethCtls):
            val=1
            if i==1: val=-1
            ModFunc._offsetCtls(ctl,s=(2,val,1))
            cmds.rotate(0,0,0,ctl+'_nul')
            cmds.move(7,val*.7,0,ctl+'_nul',r=True)
            
            #tongue ctrls
        ModFunc._createCtlGrp(self.M.tongueBinds,self.M.tongueCtls,self.faceCtl,
          ori=False, size=1, shape='circle')
        ModFunc._offsetCtls(self.M.tongueCtls,r=(0,90,0),s=(1,1,1))
        for i in range(len(self.M.tongueCtls)-1):
            cmds.parent(self.M.tongueCtls[i+1]+'_nul',self.M.tongueCtls[i]) #child, parent /1,0 /2,1 /3,2 /4,3 /5,4 /6,5
            ###
        ModFunc._overrideColor(self.M.microCtls, color=(1,1,0)) #yellow
        ModFunc._overrideColor(self.M.macroCtls+[self.M.ctl]+self.M.cornerCtls, color=(1,0,0)) #red
        ModFunc._overrideColor(self.M.teethCtls+self.M.tongueCtls,color=(1,.5,.5)) #pink
        ModFunc._scaleOrient(self.M.microCtls+self.M.macroCtls+self.M.cornerCtls)
        ModFunc._90dOrient(self.M.microCtls+self.M.macroCtls+self.M.cornerCtls)
        cmds.parent(self.M.microCtlGrp, self.M.macroCtlGrp, self.faceCtl)
        
        #5: Parent constraint micro nul2 group to macro ctl
        MouthFunc.constMicroToMacro(self.M.microCtls)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.M.cornerCtls,val=(2,2,2))
        
            ###Mouth crv blendshapes
        #1: Duplicate orig curve
        MouthFunc._createBsCrv(self.M.crv,self.M.blendCrvs,self.M.blendCrvGrp)
        
        #2: Create Blendshape Node
        MouthFunc._createBsNode(self.M.bsNode, self.M.crv, self.M.blendCrvs)
        
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(self.M.bsNode)
        
        
    def lid01(self):
        #1: Mirror Lid Curves
        ModFunc._mirrorObj(self.L.crvs[2], self.L.crvs[0])
        ModFunc._mirrorObj(self.L.crvs[3], self.L.crvs[1])
        
        #2: Create lid Binds on lid verts & connect to lid curves
        upperRPos = ModFunc._getPosListFromVerts(self.data['verts']['lidUpperR'])
        ModFunc._createBindsOnCrv(self.L.upperRBinds, upperRPos, self.L.crvs[0], self.L.rBindGrp) #names,posList,curv,
        
        upperLPos = ModFunc._mirrorPosX(upperRPos)
        ModFunc._createBindsOnCrv(self.L.upperLBinds, upperLPos, self.L.crvs[2], self.L.lBindGrp)
        
        lowerRPos = ModFunc._getPosListFromVerts(self.data['verts']['lidLowerR'])
        ModFunc._createBindsOnCrv(self.L.lowerRBinds, lowerRPos, self.L.crvs[1], self.L.rBindGrp)
        
        lowerLPos = ModFunc._mirrorPosX(lowerRPos)
        ModFunc._createBindsOnCrv(self.L.lowerLBinds, lowerLPos, self.L.crvs[3], self.L.lBindGrp)

        #3: Aim constraint lid binds to eye socket bind
        ModFunc._aimConstIterate(self.L.rBinds,self.J.eyeSocBinds[0])
        ModFunc._aimConstIterate(self.L.lBinds,self.J.eyeSocBinds[1])

        for i in range(4):
            #3: Create Lid Driver Curve
            LidFunc._createDrivCrv(self.L.drivCrvs[i],self.L.crvs[i])
            #4: Create Blink Driver Joints
            LidFunc._createBlinkDrivers(self.L.drivs[i],self.L.drivCrvs[i],self.L.drivGrp)
            
            #5: Create Lid tweak Ctls
            ModFunc._createCtlGrp(self.L.drivs[i], self.L.microCtls[i], self.L.microCtlGrp, ori=False, opm=True, size=.3)
            ModFunc._offsetCtls(self.L.microCtls[i], t=(0,0,.7))
            ModFunc._overrideColor(self.L.microCtls[i], color=(1,1,0))
            
            #5: Create Lid Driver Joints
            LidFunc._createlidDrivers(self.L.lidDrivs[i],self.L.drivs[i],self.L.microCtls[i],self.L.lidDrivGrp)
            
            #6: Skin Driver joints to lid curves
            ModFunc._skinCrv(self.L.lidDrivs[i],self.L.crvs[i]) #0,1,2,3,4
        
        #7: parent lid ctl grp to face upper ctl
        cmds.parent(self.L.microCtlGrp,self.faceUpCtl)
        
        #4: Create blink Ctls
        socketBinds = [self.J.eyeSocBinds[0], self.J.eyeSocBinds[0], self.J.eyeSocBinds[1], self.J.eyeSocBinds[1]]
        ModFunc._createCtlGrp(socketBinds, self.L.ctls, self.L.ctlGrp, size=1, shape='arch')
        ModFunc._offsetCtls(self.L.ctls[:2], t=(0,0,7), s=(1.2,-.7,1)) #r
        ModFunc._offsetCtls(self.L.ctls[2:], t=(0,0,7), s=(1.2,.7,1)) #l
        cmds.scale(1,-1,1,self.L.ctls[0]+'_orient') #lower_r
        cmds.scale(1,-1,1,self.L.ctls[3]+'_orient') #upper_l
        ModFunc._overrideColor(self.L.ctls, color=(0,0,1))
        cmds.parent(self.L.ctlGrp,self.faceUpCtl)
        
            ###lid crv blendshapes
        #1: Duplicate orig curve
        LidFunc._createBsCrv(self.L.crvs[:2], self.L.rBlendCrvs, self.L.rBlendCrvGrp)
        LidFunc._createBsCrv(self.L.crvs[2:], self.L.lBlendCrvs, self.L.lBlendCrvGrp)
        
        
    def eye01(self):
        #4: Create Eye Ctls
            #eye_rot_ctl
        ModFunc._createCtlGrp(self.J.eyeSocBinds[1], self.E.rotCtl, self.faceUpCtl, 
         ori=False,  mid=True, size=1, shape='triangle' )
        ModFunc._offsetCtls(self.E.rotCtl, t=(0,0,7.5), r=(90,0,0))
        ModFunc._overrideColor(self.E.rotCtl, color=(0,0,1))
                
            #eye_R_ctl, eye_L_ctl
        ModFunc._createCtlGrp(self.J.eyeBinds, self.E.ctls, self.faceUpCtl, 
          size=.7 )
        ModFunc._offsetCtls(self.E.ctls, t=(0,0,6))
        ModFunc._overrideColor(self.E.ctls, color=(0,0,1))
                
            #eye aim macro ctl
        ModFunc._createCtlGrp(self.J.eyeSocBinds[1], self.E.aimCtl, self.faceUpCtl, 
         ori=False,  mid=True, size=1, shape='square' )
        ModFunc._offsetCtls(self.E.aimCtl,r=(0,0,45),s=(7,1,1))
        ModFunc._overrideColor(self.E.aimCtl, color=(0,0,1))

            #eye aim micro ctls LR
        targList = [self.E.aimCtl, self.E.aimCtl]
        ModFunc._createCtlGrp(targList, self.E.aimMicroCtls, self.E.aimCtl, 
         ori=False,  mid=True, size=1 )
        ModFunc._overrideColor(self.E.aimMicroCtls, color=(0,0,1))
        
            ###initial offset
        cmds.move(0,0,20,self.E.aimCtl+'_nul',r=True)
        cmds.move(-3,0,0,self.E.aimMicroCtls[0]+'_nul',r=True)
        cmds.move(3,0,0,self.E.aimMicroCtls[1]+'_nul',r=True)
        
            #pupil ctl
        ModFunc._createCtlGrp(self.E.ctls, self.E.pupilCtls, self.faceUpCtl,
          ori=False, shape='pentagon', size=.5)
        ModFunc._overrideColor(self.E.pupilCtls, color=(0,0,1))
        
    def brow01(self):
        #2: Create Brow Ctls
            #brow_r_ctl
        browPosLocs = BrowFunc.LocsOnVert(self.data['verts']['browR'])
        
        ModFunc._createCtlGrp(browPosLocs, self.B.ctls, self.B.ctlGrp,  size=.7, shape='square' )
        ModFunc._offsetCtls(self.B.ctls, r=(0,0,45), s=(5,1,1) )
        ModFunc._scaleOrient(self.B.ctls)
        ModFunc._overrideColor(self.B.ctls, color=(1,1,0))
        cmds.parent(self.B.ctlGrp, self.faceUpCtl)
        cmds.delete(browPosLocs[0],browPosLocs[1])
        
            #orientCompensate
        compensates = BrowFunc._createCompenGrp(self.B.ctls)
        
            #brow_inner_r_ctl
        ModFunc._createCtlGrp(compensates, self.B.inCtls, self.B.ctlGrp,  size=.6, shape='square' )
        ModFunc._offsetCtls(self.B.inCtls, r=(0,0,45))
        ModFunc._scaleOrient(self.B.inCtls)
        ModFunc._overrideColor(self.B.inCtls, color=(1,1,0))
 
            #brow_peak_r_ctl
        ModFunc._createCtlGrp(compensates, self.B.peakCtls, self.B.ctlGrp,  size=.6, shape='square' )
        ModFunc._offsetCtls(self.B.peakCtls, r=(0,0,45))
        ModFunc._scaleOrient(self.B.peakCtls)
        ModFunc._overrideColor(self.B.peakCtls, color=(1,1,0))
        '''
        #for some reason parent constraint flips the child?? I have to set up the offset manually??
        cmds.setAttr(self.B.inCtls[1]+'_nul'+'_parentConstraint1.target[0].targetOffsetRotateX', 180)
        cmds.setAttr(self.B.peakCtls[1]+'_nul'+'_parentConstraint1.target[0].targetOffsetRotateX', 180)
        '''
        '''
        cmds.move(0,0,2,self.E.aimCtl+'_nul',r=True)
        '''
        cmds.move(3,0,0,self.B.inCtls[0]+'_orient',r=True)
        cmds.move(-3,0,0,self.B.inCtls[1]+'_orient',r=True)
        cmds.move(-1,0,0,self.B.peakCtls[0]+'_orient',r=True)
        cmds.move(1,0,0,self.B.peakCtls[1]+'_orient',r=True)
        
        #3: Create Custom Attributes for Brow Ctls
        BrowFunc._createFollowAttr(self.B.ctls)
        BrowFunc._createFollowAttr(self.B.inCtls)
        BrowFunc._createFollowAttr(self.B.peakCtls)
        
        #4: Create brow local Driver under ctl nul
        pos = cmds.xform(self.data['verts']['browR'],q=True,t=True,ws=True)
        parents = [self.B.ctls[0]+'_nul', self.B.ctls[1]+'_nul']
        BrowFunc._createLocalDrv(self.B.ctls,self.B.localDrv,pos,parents)
        BrowFunc._createLocalDrv(self.B.inCtls,self.B.inLocalDrv,pos,parents)
        BrowFunc._createLocalDrv(self.B.peakCtls,self.B.peakLocalDrv,pos,parents)
            
        #5: Create brow Driver
        pos = cmds.xform(self.J.browBigBinds[0],q=True,t=True,ws=True)
        cmds.group(n=self.B.xfGrp,em=True)
        cmds.parentConstraint(self.J.faceUpBind,self.B.xfGrp,mo=False)
        cmds.scaleConstraint(self.J.faceUpBind,self.B.xfGrp,mo=False)
        
        BrowFunc._createDrv(self.B.ctls,self.B.drv,pos,self.B.xfGrp)
        BrowFunc._createDrv(self.B.inCtls,self.B.inDrv,pos,self.B.xfGrp)
        BrowFunc._createDrv(self.B.peakCtls,self.B.peakDrv,pos,self.B.xfGrp)
        
        #6: Create Brow Meat jnts
        
    def nose01(self):
        #0: Create Nose Bridge Ctls
        ModFunc._createCtlGrp(self.J.noseBridgeBind,self.N.bridgeCtl,self.faceCtl,
          size=2.5, shape='square')
        ModFunc._offsetCtls(self.N.bridgeCtl,t=(0,-1,1), r=(0,0,45), s=(1,1,1))
        
        #1: Create Nose Follow Driver
        cmds.group(em=True,n=self.N.bridgeAuto)
        cmds.parent(self.N.bridgeAuto,self.N.bridgeCtl+'_orient',r=True)
        cmds.parent(self.N.bridgeCtl,self.N.bridgeAuto)
        
        #0: Create Nose Ctls
        ModFunc._createCtlGrp([self.J.noseBigBind],[self.N.ctl], self.N.bridgeCtl,
           size=2)
         
        ModFunc._createCtlGrp(self.J.sneerBinds,self.N.sneerCtls, self.N.ctl,
           size=.7, shape='arch')
        ModFunc._offsetCtls(self.N.sneerCtls, t=(0,0,1), s=(.7,.7,.7))
        
        ModFunc._createCtlGrp(self.J.nostrilBinds,self.N.nostrilCtls, self.N.ctl,
           size=.4, shape='pentagon')
        ModFunc._offsetCtls(self.N.nostrilCtls, t=(0,-.6,0), r=(90,0,0))
         
        ModFunc._overrideColor([self.N.ctl,self.N.bridgeCtl]+self.N.sneerCtls+self.N.nostrilCtls, color=(0,1,0))

    
    def createGrps(self):
        cmds.group(n=self.faceRoot, em=True)
        cmds.group(n=self.animGrp, em=True)
        cmds.group(n=self.rigGrp, em=True)
        cmds.group(n=self.bindGrp, em=True)
        

class ConnectCtls():
    def __init__(self):
        pass
    
    def buildRig02(self,_):
        self.face02()
        self.mouth02()
        self.lid02()
        #self.eye02()
        self.brow02()
        self.nose02()

        self.hideExtra()
        self.arrangeGrps()
    
    def deleteRig02(self,_):
        pass
    
    def face02(self):
        for bind in self.J.allBinds: opmBaker.bake_transform_to_offset_parent_matrix(bind)
        
        #1: connect face upper bind
        ModFunc._connectTransform(self.faceUpCtl,self.J.faceUpBind)
        #1: Parent constraint face lower bind
        ModFunc._connectTransform(self.faceLoCtl,self.J.faceLoBind)
        #1: Parent constraint jaw bind
        ModFunc._connectTransform(self.jawCtl,self.J.jawBind)
        
        
        '''
        #1: Parent constraint cheek binds
        ModFunc._parentConstIterate(self.cheekCtls,self.J.cheekBinds)
        '''
        #2: Make Cheek joints follow mCorner ctls
        ModFunc._createCheekDrv(self.cheekDrvs,self.M.cornerCtls,self.faceCtl)
        
        ModFunc._createCheekAuto(self.cheekCtls[0:2],self.cheekDrvs,(.1,.5,.1) )
        ModFunc._createCheekAuto(self.cheekCtls[2:4],self.cheekDrvs,(.5,.5,.5))
    
    def mouth02(self):
        P1 = self.J.faceUpBind
        P2 = self.J.jawBind
        '''
        #6: Connect Teeth Ctrl
        cmds.parentConstraint(P1,self.M.teethCtls[0]+'_nul',mo=True)
        cmds.parentConstraint(P2,self.M.teethCtls[1]+'_nul',mo=True)
        ModFunc._parentConstIterate(self.M.teethCtls, self.M.teethBinds)
        
        #7: Connect Tongue Ctrl
        ModFunc._parentConstIterate(self.M.tongueCtls, self.M.tongueBinds)
        '''
        cmds.parent(self.M.tongueCtls[0]+'_nul',self.jawCtl)
            
        #8: Create lipCV Clusters
        MouthFunc._createLipDrivers(self.M.lipDrivs, self.M.fols, self.M.microCtls, self.M.lipDrivGrp)
        
        #6: Skin Driver joints to lid curves
        ModFunc._skinCrv(self.M.lipDrivs[0:7],self.M.upperCrv) #0,1,2,3,4,5,6
        ModFunc._skinCrv(self.M.lipDrivs[6:]+[self.M.lipDrivs[0]],self.M.lowerCrv) #6,7,8,9,10,11,0

        #9: parent constraint corner ctl nul to jaw
        ###create corner pin attr
        for ctl,clus in zip(self.M.cornerCtls,self.M.cornerClus):
            cmds.addAttr(ctl, shortName='cornerPin', k=True, defaultValue=0, minValue=-1, maxValue=1)

            MouthFunc.attachCorner(ctl, clus, P1, P2)
        ###important!


        #10: Parent constraint big cluster to big ctl
        '''
        cmds.parentConstraint(self.M.ctl, self.M.clus,mo=True) #bigctl
        '''
        MouthFunc.constWithDriver(self.M.jawClusDrvs[0], self.faceUpCtl, self.M.jawClus[0],self.animGrp) #upper jaw
        MouthFunc.constWithDriver(self.M.jawClusDrvs[1], self.jawCtl, self.M.jawClus[1],self.animGrp) #lower jaw
        

        
        #4: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.M.cornerCtls, self.M.blendCrvs, self.M.bsNode)

    def lid02(self):
        #2: Create Blendshape Node
        LidFunc._createBsNode(self.L.rBsNodes, self.L.drivCrvs[:2], self.L.rBlendCrvs)
        LidFunc._createBsNode(self.L.lBsNodes, self.L.drivCrvs[2:], self.L.lBlendCrvs)
        
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        LidFunc._connectCornerCtrl(self.L.ctls[:2], self.L.rBlendCrvs, self.L.rBsNodes) # first two elements (right ctrls)
        LidFunc._connectCornerCtrl(self.L.ctls[2:], self.L.lBlendCrvs, self.L.lBsNodes) #last two elements (left ctrls)
    
    def eye02(self):
        #5: Connect Eye Ctls
        EyeFunc._connectEyeCtls(self.E.ctls, self.E.rotCtl, self.E.aimCtl, self.E.aimMicroCtls, self.J.eyeBinds)
        
        #note: create pupil joints!
        pupilNuls = [self.E.pupilCtls[0]+'_nul', self.E.pupilCtls[1]+'_nul']
        ModFunc._parentIterate(self.E.ctls,pupilNuls)
        
    def brow02(self):
        #6: Connect Brow Ctls to Brow Drivers
        wuo = self.faceUpCtl
        BrowFunc._connectBrowCtls(self.B.ctls,self.B.localDrv,self.B.drv,self.J.browBigBinds,wuo)
        BrowFunc._connectBrowCtls(self.B.inCtls,self.B.inLocalDrv,self.B.inDrv,self.J.browInBinds,wuo)
        BrowFunc._connectBrowCtls(self.B.peakCtls,self.B.peakLocalDrv,self.B.peakDrv,self.J.browPeakBinds,wuo)
        
        #7: Connect Main Follow Y to Inner Follow Y:
        for main,inner,peak in zip(self.B.ctls,self.B.inCtls,self.B.peakCtls):
            cmds.connectAttr(main+'.followY',inner+'.followY')
            cmds.connectAttr(main+'.followY',peak+'.followY')
    
        #EXTRA: Set Follow Attr (hard coding)
        cmds.setAttr(self.B.ctls[0]+'.followY',0,.5,0,type='double3')
        cmds.setAttr(self.B.ctls[0]+'.followZ',.348,0,.937,type='double3')
        cmds.setAttr(self.B.ctls[1]+'.followY',0,.5,0,type='double3')
        cmds.setAttr(self.B.ctls[1]+'.followZ',-.348,0,.937,type='double3')
    
    def nose02(self):
        '''
        #1: Parent constraint nose binds
        ModFunc._parentConstIterate([self.N.ctl]+self.N.sneerCtls+self.N.nostrilCtls,[self.J.noseBigBind]+self.J.sneerBinds+self.J.nostrilBinds)
        '''
        #2: Attach nose ctl
         ###create noseBridge_ctl_followLoc
        loc1 = cmds.spaceLocator()[0]
        cmds.parent(loc1,self.N.bridgeAuto,r=True) #not preserve position
        '''
         ###noseBridge_ctl_nul is parent constraint to lowerbind
        const1 = cmds.parentConstraint(self.J.faceUpBind,self.N.bridgeCtl+'_nul',mo=True)[0]
         ###followLoc is parent constraint to upperbind
        const2 = cmds.parentConstraint(self.J.faceLoBind,loc1,mo=True)[0]
         ###break connection: constraint parent inverse matrix
        cmds.disconnectAttr(loc1+'.parentInverseMatrix',const2+'.constraintParentInverseMatrix')
        '''
        
         ###create blendColor node
        rotBlend = cmds.createNode('blendColors')
         ###connect attr noseBridge_ctl_nul.r to color1
        cmds.connectAttr(loc1+'.r',rotBlend+'.color1')
         ###set attr color2, 0,0,0, type='double3 #default
         ###connect attr blendColorRot.outColor, nose_ctl_blend.r
        cmds.connectAttr(rotBlend+'.output',self.N.bridgeAuto+'.r')
         
         ###switch attribute
         ###create attr on noseBridge_ctl 'noseFollow' defaultValue=.5, minValue=0, maxValue=1
        cmds.addAttr(self.N.bridgeCtl,shortName='noseFollow', keyable=True, defaultValue=.5, minValue=0, maxValue=1)
         ###connect attr noseBridge_ctl.noseFollow, blendColorRot.blender
        cmds.connectAttr(self.N.bridgeCtl+'.noseFollow',rotBlend+'.blender')
         ###You would create another blend color node to connect translate
        
        #3: offset rotate value with orient grp?
        '''
        #4: Parent Constraint noseBridge bind to noseBridge ctl
        cmds.parentConstraint(self.N.bridgeCtl, self.J.noseBridgeBind)
        
        #5: Parent nose ctl nul to noseBridge ctl
        cmds.parent(self.N.ctl+'_nul',self.N.bridgeCtl)
        '''
        
    def hideExtra(self):
        pass
        '''
        cmds.select(self.M.drivs,self.M.lipClus,self.M.lipDrivs,self.L.lidDrivs)
        cmds.hide()
        '''
        
    def arrangeGrps(self):
        #these are rather simple parent commands, we keep going even if there's an error.
        try:
            cmds.parent(self.animGrp,self.rigGrp,self.bindGrp,self.faceRoot)
        except: print('face_grp parent skipped')
        
        try:
            cmds.parent(self.J.faceBind,
            self.L.rBindGrp,self.L.lBindGrp, 
            self.M.upperBindGrp,self.M.lowerBindGrp,
            self.bindGrp)
        except: print('bind_grp parent skipped')
        

        cmds.parent(
                self.M.upperCrv, self.M.lowerCrv,self.M.crv,
                self.M.bindmeshesGrp, self.M.clusGrp, self.M.folGrp,
                self.M.drivGrp,self.M.lipDrivGrp,
                self.M.blendCrvGrp, 
                self.L.crvs,self.L.drivCrvs,
                self.L.drivGrp,self.L.lidDrivGrp,
                self.L.rBlendCrvGrp, self.L.lBlendCrvGrp,
                self.B.xfGrp,
                self.rigGrp)
        #except: print('rig_grp parent skipped')


        
class BindGeo():
    def __init__(self):
        pass
    
    def buildRig03(self,_):
        self.skinNodes = []
        for jntKey,jnt in self.bindSets.items():
            maxit = 4
            if 'eyeR'==jntKey or 'eyeL'==jntKey or 'extra'==jntKey: maxit=1
            for geoKey,geos in self.data['geo'].items():
                if geoKey==jntKey: 
                    for obj in geos:#iterate geo list
                        cmds.select(obj,jnt)#select bind ctl
                        try:
                            node = cmds.skinCluster(tsb=True,mi=maxit,sm=0)#bind skin
                            ###name the skinCluster based on geo!!!
                            ###or auto renames the skinCluster names before export?
                            self.skinNodes.append(node)
                        except: print('###'+ geo +' is already skinned ###')
                
    def selectGeo(self,x):
        cmds.select(self.data['geo'][x])
            
    def selectBinds(self,x,_):
        for bind in self.bindSets[x]:
            try:
                cmds.select(bind, add=True)
            except: print(bind,'doesn\'t exist. Select skipped')
        
    def deleteRig03(self,_):
        cmds.delete(self.skinNodes)
#-----------------------------------------------------EXECUTE---------------------------------------------------------------
