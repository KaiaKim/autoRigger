import maya.cmds as mc
from functools import partial
import importlib
import json

from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import DataFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import LidFunc
from Kaia_AutoRigger import EyeFunc
from Kaia_AutoRigger import BrowFunc
from Kaia_AutoRigger import CheekFunc
from Kaia_AutoRigger import opmBaker
importlib.reload(ModFunc)
importlib.reload(DataFunc)
importlib.reload(MouthFunc)
importlib.reload(LidFunc)
importlib.reload(BrowFunc)
importlib.reload(CheekFunc)
importlib.reload(opmBaker)

###-----------------------------------------------------CLASS---------------------------------------------------
class BuildCtls():
    def __init__(self):
        pass
        
    def buildRig01(self,_):
        self.createGrps()
        self.face01()
        self.mouth01()
        self.cheek01()
        self.teethTongue01()
        self.lid01()
        self.eye01()
        self.brow01()
        self.nose01()
        
        self.colorCtls()
        
        DataFunc._applyTransform(self.data['orients'])
        DataFunc._applyTransform(self.data['bsCrv'], os=True)
    
    def face01(self):
        #0: Create Face Ctls
        ModFunc._createCtlGrp(self.F.bind,self.F.ctl,self.animGrp, ori=False,size=8)
        ModFunc._offsetCtls(self.F.ctl,r=(90,0,0))
        
        #0: Create Upper Face Ctls
        ModFunc._createCtlGrp(self.F.upBind,self.F.upCtl, self.F.ctl, ori=False, size=1 ,shape='triangle')
        ModFunc._offsetCtls(self.F.upCtl, t=(0,-1.5,12), s=(1,.4,1))
        
        #0: Create Lower Face Ctls
        ModFunc._createCtlGrp(self.F.loBind, self.F.loCtl, self.F.ctl, ori=False, size=12, shape='semiCircle' )
        ModFunc._offsetCtls(self.F.loCtl, t=(0,-6,0), r=(180,0,0))
        
        #0: Create Jaw Ctls
        ModFunc._createCtlGrp(self.F.jawBind, self.F.jawCtl, self.F.loCtl, size=1, shape='triangle')
        ModFunc._offsetCtls(self.F.jawCtl,t=(0,-6,10), r=(180,0,0), s=(1,.6,1))
   
    
    def mouth01(self):
        #1: Generate mouth_curve from lip_curves
        MouthFunc._createMouthCrv(self.M.crv, self.M.upCrv, self.M.loCrv)
        
        #1: Create lip binds
        upperPos = ModFunc._getPosListFromVerts(self.data['verts']['lipUpper'])
        ModFunc._createBindsOnCrv(self.M.upBinds, upperPos, self.M.upCrv, self.M.upBindGrp)
        lowerPos = ModFunc._getPosListFromVerts(self.data['verts']['lipLower'])
        ModFunc._createBindsOnCrv(self.M.loBinds, lowerPos, self.M.loCrv, self.M.loBindGrp)
        
        ###temp: aim constraint lip binds
        ModFunc._aimConstIterate(self.M.binds, self.F.loBind)
        
        #2: Create mouth drivers
        MouthFunc._createMouthDrivers(self.M.drivs, self.M.crv,self.M.drivGrp) 

        #4: Create Ctrls
            #lip micro ctrls
        ModFunc._createCtlGrp(self.M.drivs,self.M.lipCtls,self.M.lipCtlGrp, size=.3, opm=True)
        ModFunc._offsetCtls(self.M.lipCtls, t=(0,0,1))
            #big ctl
        ModFunc._createCtlGrp(self.F.loBind,self.M.ctl, self.F.loCtl,
           ori=False, size=4, shape='square')
        ModFunc._offsetCtls(self.M.ctl, t=(0,-4.5,12), s=(1,.5,1))
            #corner ctrls
        ModFunc._createCtlGrp([self.M.drivs[0],self.M.drivs[6]], self.M.cornerCtls, self.M.ctl,
          size=.5, shape='triangle')
        ModFunc._offsetCtls(self.M.cornerCtls, t=(0,0,1.2), r=(0,0,-30))
            ###
        ModFunc._scaleOrient(self.M.lipCtls+self.M.cornerCtls)
        mc.parent(self.M.lipCtlGrp, self.F.ctl)
        
        #5: Add handle toggle attribute on corner ctl
        for ctl in self.M.cornerCtls: ModFunc._handleToggle(ctl)
        
        #6: Normalize Corner Ctls
        ModFunc._normalizeCtls(self.M.cornerCtls,val=(2,2,2))
        
            ###Mouth crv blendshapes
        #1: Duplicate orig curve
        MouthFunc._createBsCrv(self.M.crv,self.M.blendCrvs,self.M.blendCrvGrp)
        #2: Create Blendshape Node
        MouthFunc._createBsNode(self.M.bsNode, self.M.crv, self.M.blendCrvs)
        #3: Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(self.M.bsNode)
        
    def cheek01(self):
        #0: Create Cheek Ctls
        ModFunc._createCtlGrp(self.C.binds, self.C.ctls, self.C.ctlGrp, size=.5 )
        ModFunc._offsetCtls([self.C.ctls[0],self.C.ctls[2],self.C.ctls[4]],t=(0,0,.5))
        ModFunc._offsetCtls([self.C.ctls[1],self.C.ctls[3],self.C.ctls[5]],t=(0,0,-.5))
        
        #scale orient in z
        ModFunc._scaleOrient(self.C.ctls,s=(1,1,-1))

        mc.parent(self.C.ctlGrp,self.F.ctl)

    def teethTongue01(self):
        #teeth ctrls
        jawTipList = [self.F.jawTipBind, self.F.jawTipBind]
        ModFunc._createCtlGrp(jawTipList,self.T.teethCtls,self.F.ctl,
           size=.7, shape='semiCircle')
        for i,ctl in enumerate(self.T.teethCtls):
            val=1
            if i==1: val=-1
            ModFunc._offsetCtls(ctl,s=(2,val,1))
            mc.rotate(0,0,0,ctl+'_nul')
            mc.move(7,val*.7,0,ctl+'_nul',r=True)
            
            #tongue ctrls
        ModFunc._createCtlGrp(self.T.tongueBinds,self.T.tongueCtls,self.F.ctl,
          ori=False, size=1, shape='circle')
        ModFunc._offsetCtls(self.T.tongueCtls,r=(0,90,0),s=(1,1,1))
        for i in range(len(self.T.tongueCtls)-1):
            mc.parent(self.T.tongueCtls[i+1]+'_nul',self.T.tongueCtls[i]) #child, parent /1,0 /2,1 /3,2 /4,3 /5,4 /6,5


        
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
        ModFunc._aimConstIterate(self.L.rBinds,self.E.socBinds[0])
        ModFunc._aimConstIterate(self.L.lBinds,self.E.socBinds[1])

        for i in range(4):
            #3: Create Lid Driver Curve
            LidFunc._createDrivCrv(self.L.drivCrvs[i],self.L.crvs[i])
            #4: Create Blink Driver Joints
            LidFunc._createBlinkDrivers(self.L.drivs[i],self.L.drivCrvs[i],self.L.drivGrp)
    
            #5: Create Lid tweak Ctls
            ModFunc._createCtlGrp(self.L.drivs[i], self.L.microCtls[i], self.L.microCtlGrp, ori=False, opm=True, size=.3)
            ModFunc._offsetCtls(self.L.microCtls[i], t=(0,0,.7))
            
            #5: Create Lid Driver Joints
            LidFunc._createlidDrivers(self.L.lidDrivs[i],self.L.drivs[i],self.L.microCtls[i],self.L.lidDrivGrp)
            
            #6: Skin Driver joints to lid curves
            ModFunc._bindSkin(self.L.lidDrivs[i],self.L.crvs[i]) #0,1,2,3,4
        
        #7: parent lid ctl grp to face upper ctl
        mc.parent(self.L.microCtlGrp,self.F.upCtl)
        
        #4: Create blink Ctls
        socketBinds = [self.E.socBinds[0], self.E.socBinds[0], self.E.socBinds[1], self.E.socBinds[1]]
        ModFunc._createCtlGrp(socketBinds, self.L.ctls, self.L.ctlGrp, size=1, shape='arch')
        ModFunc._offsetCtls(self.L.ctls[:2], t=(0,0,7), s=(1.2,-.7,1)) #r
        ModFunc._offsetCtls(self.L.ctls[2:], t=(0,0,7), s=(1.2,.7,1)) #l
        mc.scale(1,-1,1,self.L.ctls[0]+'_orient') #lower_r
        mc.scale(1,-1,1,self.L.ctls[3]+'_orient') #upper_l
        mc.parent(self.L.ctlGrp,self.F.upCtl)
        #5: Create handle toggle attribute
        for ctl in self.L.ctls: ModFunc._handleToggle(ctl)
        
            ###lid crv blendshapes
        #1: Duplicate orig curve
        LidFunc._createBsCrv(self.L.crvs[:2], self.L.rBlendCrvs, self.L.rBlendCrvGrp)
        LidFunc._createBsCrv(self.L.crvs[2:], self.L.lBlendCrvs, self.L.lBlendCrvGrp)
        
        
    def eye01(self):
        #4: Create Eye Ctls
            #eye_rot_ctl
        ModFunc._createCtlGrp(self.E.socBinds[1], self.E.rotCtl, self.F.upCtl, 
         ori=False,  mid=True, size=1, shape='triangle' )
        ModFunc._offsetCtls(self.E.rotCtl, t=(0,0,7.5), r=(90,0,0))       
            #eye_R_ctl, eye_L_ctl
        ModFunc._createCtlGrp(self.E.binds, self.E.ctls, self.F.upCtl, 
          size=.7 )
        ModFunc._offsetCtls(self.E.ctls, t=(0,0,6))        
            #eye aim macro ctl
        ModFunc._createCtlGrp(self.E.socBinds[1], self.E.aimCtl, self.F.upCtl, 
         ori=False,  mid=True, size=1, shape='square' )
        ModFunc._offsetCtls(self.E.aimCtl,s=(7,1,1))
            #eye aim micro ctls LR
        targList = [self.E.aimCtl, self.E.aimCtl]
        ModFunc._createCtlGrp(targList, self.E.aimMicroCtls, self.E.aimCtl, 
         ori=False,  mid=True, size=1 )
        
            ###initial offset
        mc.move(0,0,20,self.E.aimCtl+'_nul',r=True)
        mc.move(-3,0,0,self.E.aimMicroCtls[0]+'_nul',r=True)
        mc.move(3,0,0,self.E.aimMicroCtls[1]+'_nul',r=True)

        
    def brow01(self):
        #2: Create Brow Ctls
            #brow_ctl
        ModFunc._createCtlGrp(self.B.bigBinds, self.B.bigCtls, self.B.ctlGrp, ori=False, size=.7, shape='square' )
        ModFunc._offsetCtls(self.B.bigCtls[0], t=(-2,0,0), s=(3,1.2,1))
        ModFunc._offsetCtls(self.B.bigCtls[1], t=(2,0,0), s=(3,1.2,1))
            #brow_inner_ctl
        ModFunc._createCtlGrp(self.B.inBinds, self.B.inCtls, self.B.bigCtls, ori=False, size=.4, shape='circle' )
             #brow_cor_ctl
        ModFunc._createCtlGrp(self.B.corBinds, self.B.corCtls, self.B.inCtls, ori=False, size=.6, shape='triangle' )
        ModFunc._offsetCtls(self.B.corCtls,t=(0,1,0), r=(0,0,180), s=(.4,1,1) )
            #brow_peak_ctl
        ModFunc._createCtlGrp(self.B.peakBinds, self.B.peakCtls, self.B.bigCtls, ori=False, size=.4, shape='circle' )
        
        ModFunc._offsetCtls(self.B.inCtls+self.B.corCtls+self.B.peakCtls, t=(0,0,.5))
        mc.parent(self.B.ctlGrp, self.F.upCtl)

        
    def nose01(self):
        #0: Create Nose Bridge Ctls
        ModFunc._createCtlGrp(self.N.bridgeBind,self.N.bridgeCtl,self.F.upCtl,
          size=.8, shape='square', ori=False)
        ModFunc._offsetCtls(self.N.bridgeCtl,t=(0,0,2), s=(1,2,2))
        
        #0: Create Nose Ctls
        ModFunc._createCtlGrp(self.N.tipBind,self.N.ctl, self.N.bridgeCtl,
           size=.8, shape='square')
        ModFunc._offsetCtls(self.N.ctl,t=(0,0,2))
         
        ModFunc._createCtlGrp(self.N.sneerBinds,self.N.sneerCtls, self.N.ctl,
           size=.5, shape='arch')
        ModFunc._offsetCtls(self.N.sneerCtls, t=(0,0,1.7))
    
    def createGrps(self):
        mc.group(n=self.faceRoot, em=True)
        mc.group(n=self.animGrp, em=True)
        mc.group(n=self.rigGrp, em=True)
        mc.group(n=self.bindGrp, em=True)

    def colorCtls(self):
        red=(1,0,0)
        blue=(0,0,1)
        lightBlue = (.4,1.2,8.6)
        pink=(2.4,.6,.57)
        yellow=(1,1,0)
        purple=(.3,0,.7)
        
        ModFunc._overrideColor([self.F.upCtl, self.F.jawCtl]+self.T.teethCtls+self.T.tongueCtls, color=yellow)
        ModFunc._overrideColor([self.E.rotCtl,self.E.aimCtl]+self.E.ctls+self.E.aimMicroCtls, color=yellow)
        ModFunc._overrideColor([self.F.loCtl,self.M.ctl,self.N.ctl,self.N.bridgeCtl], color=purple)
        
        list1 = self.C.ctls+self.M.cornerCtls+self.L.ctls+self.B.bigCtls+self.B.inCtls+self.B.corCtls+self.B.peakCtls
        ModFunc._overrideColor([d for d in list1 if '_r_' in d], color=red)
        ModFunc._overrideColor([d for d in list1 if '_l_' in d], color=blue)
        
        list2 = self.M.lipCtls+sum(self.L.microCtls,[])+self.N.sneerCtls
        ModFunc._overrideColor([d for d in list2 if '_r_' in d], color=pink)
        ModFunc._overrideColor([d for d in list2 if '_l_' in d], color=lightBlue)
        ModFunc._overrideColor([d for d in list2 if '_m_' in d], color=yellow)


class ConnectCtls():
    def __init__(self):
        pass
    
    def buildRig02(self,_):
        self.face02()
        self.mouth02()
        self.cheek02()
        self.teethTongue02()
        self.lid02()
        self.eye02()
        self.brow02()
        self.nose02()
        self.arrangeGrps()

    
    def face02(self):
        for bind in self.allBinds: opmBaker.bake_transform_to_offset_parent_matrix(bind)
        #1: connect face upper bind
        ModFunc._connectTransform(self.F.upCtl,self.F.upBind)
        #1: Parent constraint face lower bind
        ModFunc._connectTransform(self.F.loCtl,self.F.loBind)
        #1: Parent constraint jaw bind
        ModFunc._connectTransform(self.F.jawCtl,self.F.jawBind)
        
        
    def mouth02(self):
        P1=self.F.upCtl
        P2=self.F.jawCtl
        P3=self.M.ctl
        #3: Create Bindmeshes on driver
        MouthFunc._createBindmeshesOnJnts(self.M.bindmeshes,self.M.drivs,self.M.bindmeshesGrp)
        #4: Create uvPin on Bindmeshes
        MouthFunc._createUvPin(self.M.uvPins,self.M.bindmeshes)
        
        #1: Create Clusters on Bindmeshes
            #big clus
        MouthFunc._createClsGrp(self.M.clus, self.F.loBind, self.M.bindmeshes, self.M.clusGrp)
            #jaw clus
        upWeights = [.6,.8,1,.8,.6]
        MouthFunc._createClsGrp(self.M.jawClus[0], self.F.upBind, self.M.bindmeshes[1:6], self.M.clusGrp, weights=upWeights) #upper
        loWeights = [.6,.8,1,.8,.6]
        MouthFunc._createClsGrp(self.M.jawClus[1], self.F.jawBind, self.M.bindmeshes[7:], self.M.clusGrp, weights=loWeights) #lower
            #corner clus
        MouthFunc._createClsGrp(self.M.cornerClus[0],self.M.ctl,self.M.bindmeshes[0], self.M.clusGrp)
        MouthFunc._createClsGrp(self.M.cornerClus[1],self.M.ctl,self.M.bindmeshes[6], self.M.clusGrp)
        
        #2: Connect Ctls
            #big ctl
        MouthFunc._connectBigClus(self.M.clus+'_nul',P3,self.F.loCtl)
            #jaw ctl
        ModFunc._connectTransform(P1,self.M.jawClus[0]+'_nul')
        ModFunc._connectTransform(P2, self.M.jawClus[1]+'_nul')
            #corner ctl
        for clus,ctl in zip(self.M.cornerClus,self.M.cornerCtls):
            ModFunc._createAutoGrp(ctl+'_nul',P3,name=ctl+'_auto')
            MouthFunc._cornerCtls(ctl,clus,P1,P2)
        
        #1: Create&connect lip drivers&lip ctls to uvPins
        MouthFunc._lipDrivers(self.M.lipDrivs, self.M.uvPins, self.M.lipCtls, self.M.lipDrivGrp)
        #2: Skin lip driver joints to lip curves
        ModFunc._bindSkin(self.M.lipDrivs[0:7],self.M.upCrv) #0,1,2,3,4,5,6
        ModFunc._bindSkin(self.M.lipDrivs[6:]+[self.M.lipDrivs[0]],self.M.loCrv) #6,7,8,9,10,11,0
        #1: Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectBs(self.M.cornerCtls, self.M.blendCrvs, self.M.bsNode)
    
    def cheek02(self):
        #1: Cheek ctls follow mCorner ctls
        CheekFunc._createDrv(self.C.drvs,self.M.cornerCtls,self.F.ctl)
        #2: Create Auto grp
        for ctl in self.C.ctls: ModFunc._createAutoGrp(ctl,ctl+'_orient')
        #3: Connect Auto grp
        CheekFunc._connectCtls(self.C.ctls[0:2],self.C.drvs,(-.2,.5,.1)) #upper
        CheekFunc._connectCtls(self.C.ctls[2:4],self.C.drvs,(-.5,.7,.5)) #mid
        CheekFunc._connectCtls(self.C.ctls[4:6],self.C.drvs,(-.5,1.4,.2)) #low
        #2: Cheek binds follow mCorner ctls
        CheekFunc._connectBinds(self.C.ctls,self.C.binds)

        
    def teethTongue02(self):
        P1 = self.F.upBind
        P2 = self.F.jawBind
        '''
        #6: Connect Teeth Ctrl
        mc.parentConstraint(P1,self.T.teethCtls[0]+'_nul',mo=True)
        mc.parentConstraint(P2,self.T.teethCtls[1]+'_nul',mo=True)
        ModFunc._parentConstIterate(self.T.teethCtls, self.T.teethBinds)
        
        #7: Connect Tongue Ctrl
        ModFunc._parentConstIterate(self.T.tongueCtls, self.T.tongueBinds)
        '''
        mc.parent(self.T.tongueCtls[0]+'_nul',self.F.jawCtl)
        
        
    def lid02(self):
        #2: Create Blendshape Node
        LidFunc._createBsNode(self.L.rBsNodes, self.L.drivCrvs[:2], self.L.rBlendCrvs)
        LidFunc._createBsNode(self.L.lBsNodes, self.L.drivCrvs[2:], self.L.lBlendCrvs)
        
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        LidFunc._connectBs(self.L.ctls[:2], self.L.rBlendCrvs, self.L.rBsNodes) # first two elements (right ctrls)
        LidFunc._connectBs(self.L.ctls[2:], self.L.lBlendCrvs, self.L.lBsNodes) #last two elements (left ctrls)
    
    def eye02(self):
        #5: Connect Eye Ctls
        EyeFunc._connectEyeCtls(self.E.ctls, self.E.rotCtl, self.E.aimCtl, self.E.aimMicroCtls, self.E.binds)
        
        
    def brow02(self):
        for ctl,bind in zip(self.B.ctls,self.B.binds):
            ModFunc._connectTransform(ctl,bind)

    
    def nose02(self):
        P1=self.F.loCtl
        #2: Attach nose ctl
        #1: Create Nose Follow Driver
        ModFunc._createAutoGrp(self.N.bridgeCtl,self.N.bridgeCtl+'_nul')
        
        #noseFollow attribute
        mc.addAttr(self.N.bridgeCtl,shortName='noseFollow', keyable=True, defaultValue=.5, minValue=0, maxValue=1)
        
        ctl=self.N.bridgeCtl
        bind=self.N.bridgeBind
        
        mult1=mc.createNode('multiplyDivide')
        mc.connectAttr(P1+'.r',mult1+'.input1')
        mc.connectAttr(ctl+'.noseFollow',mult1+'.input2X')
        mc.connectAttr(ctl+'.noseFollow',mult1+'.input2Y')
        mc.connectAttr(ctl+'.noseFollow',mult1+'.input2Z')
        col1=mc.createNode('colorMath')
        mc.connectAttr(ctl+'.r',col1+'.colorA')
        mc.connectAttr(mult1+'.output',col1+'.colorB')
        mc.connectAttr(col1+'.outColor',bind+'.r')
        
        ###You would create another blend color node to connect translate

        
    def arrangeGrps(self):
        #these are rather simple parent commands, we keep going even if there's an error.
        try:
            mc.parent(self.animGrp,self.rigGrp,self.bindGrp,self.faceRoot)
        except: print('face_grp parent skipped')
        
        try:
            mc.parent(self.F.bind,
            self.L.rBindGrp,self.L.lBindGrp, 
            self.M.upBindGrp,self.M.loBindGrp,
            self.C.bindGrp, self.bindGrp)
        except: print('bind_grp parent skipped')
        
        try:
            mc.parent(
                    self.M.upCrv, self.M.loCrv,self.M.crv,
                    self.M.bindmeshesGrp, self.M.clusGrp,
                    self.M.drivGrp,self.M.lipDrivGrp,
                    self.M.blendCrvGrp, 
                    self.L.crvs,self.L.drivCrvs,
                    self.L.drivGrp,self.L.lidDrivGrp,
                    self.L.rBlendCrvGrp, self.L.lBlendCrvGrp,
                    self.rigGrp)
        except: print('rig_grp parent skipped')

        
class BindGeo():
    def __init__(self):
        pass
    
    def buildRig03(self,_):
        for geoKey,geos in self.data['geo'].items():
            for jntKey,jnts in self.bindSets.items():
                if jntKey in ['eyeR','eyeL','extra']: x=1
                else: x=4
                if geoKey==jntKey: ModFunc._bindSkin(jnts,geos,maxi=x)
                
    def selectGeo(self,x):
        mc.select(self.data['geo'][x])
            
    def selectBinds(self,x,_):
        for bind in self.bindSets[x]:
            try: mc.select(bind, add=True)
            except: print(bind,'doesn\'t exist. Select skipped')

#-----------------------------------------------------EXECUTE---------------------------------------------------------------

