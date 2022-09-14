import maya.cmds as mc
import importlib

from Kaia_AutoRigger.modules import util
from Kaia_AutoRigger.modules import getset
from Kaia_AutoRigger.modules import mouth
from Kaia_AutoRigger.modules import lid
from Kaia_AutoRigger.modules import eye
from Kaia_AutoRigger.modules import nose
from Kaia_AutoRigger.modules import cheek
from Kaia_AutoRigger.modules import opm_baker

importlib.reload(util)
importlib.reload(getset)
importlib.reload(mouth)
importlib.reload(lid)
importlib.reload(nose)
importlib.reload(cheek)
importlib.reload(opm_baker)

###-----------------------------------------------------CLASS---------------------------------------------------
class BuildRig():
    def __init__(self):
        pass
        
    def buildRig01(self,_):
        self.createGrps()
        self.face01()
        self.mouth01()
        self.cheek01()
        #self.teethTongue01()
        self.lid01()
        #self.eye01()
        self.brow01()
        self.nose01()
        
        
        self.face02()
        self.mouth02()
        self.cheek02()
        #self.teethTongue02()
        self.lid02()
        #self.eye02()
        self.brow02()
        self.nose02()
        self.arrangeGrps()
        
        self.colorCtls()
        
        getset.applyTransform(self.data['orients'])
        getset.applyTransform(self.data['bsCrv'], os=True)


    def face01(self):
        #0: Create Face Ctls
        mc.group(em=True,n=self.F.root)
        
        mc.connectAttr(
                self.F.bind+'.worldMatrix', self.F.root+'.offsetParentMatrix'
                )
        mc.disconnectAttr(
                self.F.bind+'.worldMatrix', self.F.root+'.offsetParentMatrix'
                )
        
        #0: Create Upper Face Ctls
        util.createCtlGrp(
            self.F.upBind, self.F.upCtl, self.F.root,
            ori=False, size=1, shape='triangle'
            )
        util.offsetCtls(self.F.upCtl, t=(0,-1.5,12), s=(1,.4,1))
        
        #0: Create Lower Face Ctls
        util.createCtlGrp(
            self.F.loBind, self.F.loCtl, self.F.root,
            ori=False, size=12, shape='semiCircle'
            )
        util.offsetCtls(self.F.loCtl, t=(0,-6,0), r=(180,0,0))
        
        #0: Create Jaw Ctls
        util.createCtlGrp(
            self.F.jawBind, self.F.jawCtl, self.F.loCtl,
            size=1, shape='triangle'
            )
        util.offsetCtls(self.F.jawCtl, t=(0,-6,10), r=(180,0,0), s=(1,.6,1))
   
    
    def mouth01(self):
        #1: Generate mouth_curve from lip_curves
        mouth.createMouthCrv(self.M.crv, self.M.upCrv, self.M.loCrv)

        #1: Create lip binds
        upperPos = util.getPosListFromVerts(self.data['verts']['lipUpper'])
        util.createBindsOnCrv(
            self.M.upBinds, upperPos, self.M.upCrv, self.F.loBind
            )
        lowerPos = util.getPosListFromVerts(self.data['verts']['lipLower'])
        util.createBindsOnCrv(
            self.M.loBinds, lowerPos, self.M.loCrv, self.F.loBind
            )
    
        for bind in self.M.binds:
            mc.connectAttr(
                self.F.loBind+'.worldInverseMatrix', bind+'.offsetParentMatrix'
                )
            mc.disconnectAttr(
                self.F.loBind+'.worldInverseMatrix', bind+'.offsetParentMatrix'
                )
        
        ###temp: aim constraint lip binds
        util.aimConstIterate(self.M.binds, self.F.loBind)
        
        #2: Create mouth drivers
        mouth.createMouthDrivers(self.M.drivs, self.M.crv,self.M.drivGrp)

        #4: Create Ctrls
            #lip micro ctrls
        util.createCtlGrp(
            self.M.drivs,self.M.lipCtls,self.M.lipCtlGrp,
            size=.3, opm=True
            )
        util.offsetCtls(self.M.lipCtls, t=(0,0,1))
            #big ctl
        util.createCtlGrp(
            self.F.loBind,self.M.ctl, self.F.loCtl,
            ori=False, size=4, shape='square')
        util.offsetCtls(self.M.ctl, t=(0,-4.5,12), s=(1,.5,1))
            #corner ctrls
        util.createCtlGrp(
            [self.M.drivs[0],self.M.drivs[6]], self.M.cornerCtls, self.M.ctl,
            size=.5, shape='triangle')
        util.offsetCtls(self.M.cornerCtls, t=(0,0,1.2), r=(0,0,-30))

        util.scaleOrient(self.M.lipCtls+self.M.cornerCtls)
        mc.parent(self.M.lipCtlGrp, self.F.root)
        
        #5: Add handle toggle attribute on corner ctl
        for ctl in self.M.cornerCtls: util.handleToggle(ctl)
        
        #6: Normalize Corner Ctls
        util.normalizeCtls(self.M.cornerCtls,val=(2,2,2))
        
            ###Mouth crv blendshapes
        #1: Duplicate orig curve
        mouth.createBsCrv(self.M.crv,self.M.blendCrvs,self.M.blendCrvGrp)
        #2: Create Blendshape Node
        mouth.createBsNode(self.M.bsNode, self.M.crv, self.M.blendCrvs)
        #3: Set blendshape cv weight(sepereate left & right weight)
        mouth.setBsCvWeight(self.M.bsNode)
        
    def cheek01(self):
        #0: Create Cheek Ctls
        util.createCtlGrp(self.C.binds, self.C.ctls, self.C.ctlGrp, size=.5)
        util.offsetCtls(self.C.ctls,t=(0,0,.5),reverseZ=True)
        
        #scale orient in z
        util.scaleOrient(self.C.ctls,s=(1,1,-1))

        mc.parent(self.C.ctlGrp,self.F.root)

    def teethTongue01(self):
        #teeth ctrls
        jawTipList = [self.F.jawTipBind, self.F.jawTipBind]
        util.createCtlGrp(jawTipList, self.T.teethCtls, self.F.root,
           size=.7, shape='semiCircle')
        for i,ctl in enumerate(self.T.teethCtls):
            val=1
            if i==1: val=-1
            util.offsetCtls(ctl,s=(2,val,1))
            mc.rotate(0,0,0,ctl+'_nul')
            mc.move(7,val*.7,0,ctl+'_nul',r=True)
            
        #tongue ctrls
        util.createCtlGrp(self.T.tongueBinds, self.T.tongueCtls, self.F.root,
          ori=False, size=1, shape='circle')
        util.offsetCtls(self.T.tongueCtls,r=(0,90,0),s=(1,1,1))
        for i in range(len(self.T.tongueCtls)-1):
            mc.parent(self.T.tongueCtls[i+1]+'_nul',self.T.tongueCtls[i])
            #child, parent /1,0 /2,1 /3,2 /4,3 /5,4 /6,5


        
    def lid01(self):
        #1: Mirror Lid Curves
        getset.mirrorObj(self.L.crvs[2], self.L.crvs[0])
        getset.mirrorObj(self.L.crvs[3], self.L.crvs[1])
        
        #2: Create lid Binds on lid verts & connect to lid curves
        upperRPos = util.getPosListFromVerts(self.data['verts']['lidUpperR'])
        util.createBindsOnCrv(self.L.upperRBinds, upperRPos, self.L.crvs[0], self.E.socBinds[0])
        
        upperLPos = getset.mirrorPosX(upperRPos)
        util.createBindsOnCrv(self.L.upperLBinds, upperLPos, self.L.crvs[2], self.E.socBinds[1])
        
        lowerRPos = util.getPosListFromVerts(self.data['verts']['lidLowerR'])
        util.createBindsOnCrv(self.L.lowerRBinds, lowerRPos, self.L.crvs[1], self.E.socBinds[0])
        
        lowerLPos = getset.mirrorPosX(lowerRPos)
        util.createBindsOnCrv(self.L.lowerLBinds, lowerLPos, self.L.crvs[3], self.E.socBinds[1])
        
        #3: set world inverse matrix for lids
        for bind in self.L.rBinds:
            mc.connectAttr(
                self.E.socBinds[0]+'.worldInverseMatrix', bind+'.offsetParentMatrix'
                )
            mc.disconnectAttr(
                self.E.socBinds[0]+'.worldInverseMatrix', bind+'.offsetParentMatrix'
                )        

        for bind in self.L.lBinds:
            mc.connectAttr(
                self.E.socBinds[1]+'.worldInverseMatrix', bind+'.offsetParentMatrix'
                )
            mc.disconnectAttr(
                self.E.socBinds[1]+'.worldInverseMatrix', bind+'.offsetParentMatrix'
                ) 

        #3: Aim constraint lid binds to eye socket bind
        util.aimConstIterate(self.L.rBinds, self.E.socBinds[0])
        util.aimConstIterate(self.L.lBinds, self.E.socBinds[1])

        for i in range(4):
            #3: Create Lid Driver Curve
            lid.createDrivCrv(self.L.drivCrvs[i], self.L.crvs[i])
            #4: Create Blink Driver Joints
            lid.createBlinkDrivers(self.L.drivs[i], self.L.drivCrvs[i], self.L.drivGrp)
    
            #5: Create Lid tweak Ctls
            util.createCtlGrp(
                self.L.drivs[i], self.L.microCtls[i], self.L.microCtlGrp,
                ori=False, opm=True, size=.3
            )
            util.offsetCtls(self.L.microCtls[i], t=(0,0,.7))
            
            #5: Create Lid Driver Joints
            lid.createlidDrivers(self.L.lidDrivs[i], self.L.drivs[i], self.L.microCtls[i], self.L.lidDrivGrp)
            
            #6: Skin Driver joints to lid curves
            util.bindSkin(self.L.lidDrivs[i], self.L.crvs[i]) #0,1,2,3,4
        
        #7: parent lid ctl grp to face upper ctl
        mc.parent(self.L.microCtlGrp, self.F.upCtl)
        
        #4: Create blink Ctls
        socketBinds = [self.E.socBinds[0], self.E.socBinds[0], self.E.socBinds[1], self.E.socBinds[1]]
        util.createCtlGrp(socketBinds, self.L.ctls, self.L.ctlGrp, size=1, shape='arch')
        util.offsetCtls(self.L.ctls[:2], t=(0,0,7), s=(1.2,-.7,1)) #r
        util.offsetCtls(self.L.ctls[2:], t=(0,0,7), s=(1.2,.7,1)) #l
        mc.scale(1,-1,1, self.L.ctls[1]+'_orient') #lower_r
        mc.scale(1,-1,1, self.L.ctls[2]+'_orient') #upper_l
        mc.parent(self.L.ctlGrp, self.F.upCtl)
        
        #5: Create handle toggle attribute
        for ctl in self.L.ctls:
            util.handleToggle(ctl)
        
        #6: Offset Handle
        mc.setAttr(self.L.ctls[0]+'.selectHandleY', .5)
        mc.setAttr(self.L.ctls[1]+'.selectHandleY', .5)
        mc.setAttr(self.L.ctls[2]+'.selectHandleY', -.5)
        mc.setAttr(self.L.ctls[3]+'.selectHandleY', -.5)

        
            ###lid crv blendshapes
        #1: Duplicate orig curve
        lid.createBsCrv(self.L.crvs[:2], self.L.rBlendCrvs, self.L.rBlendCrvGrp)
        lid.createBsCrv(self.L.crvs[2:], self.L.lBlendCrvs, self.L.lBlendCrvGrp)
        
        
    def eye01(self):
        #4: Create Eye Ctls
        #eye_rot_ctl
        util.createCtlGrp(
            self.E.socBinds[1], self.E.rotCtl, self.F.upCtl,
            ori=False, mid=True, size=1, shape='triangle'
        )
        util.offsetCtls(self.E.rotCtl, t=(0,0,7.5), r=(90,0,0))
        
        #eye_R_ctl, eye_L_ctl
        util.createCtlGrp(
            self.E.binds, self.E.ctls, self.F.upCtl, 
            size=.7
        )
        util.offsetCtls(self.E.ctls, t=(0,0,6))        
        
        #eye aim macro ctl
        util.createCtlGrp(
            self.E.socBinds[1], self.E.aimCtl, self.F.upCtl,
            ori=False, mid=True, size=1, shape='square'
        )
        util.offsetCtls(self.E.aimCtl,s=(7,1,1))
        
        #eye aim micro ctls LR
        targList = [self.E.aimCtl, self.E.aimCtl]
        util.createCtlGrp(
            targList, self.E.aimMicroCtls, self.E.aimCtl,
            ori=False, mid=True, size=1
        )
        
            ###initial offset
        mc.move(0,0,20,self.E.aimCtl+'_nul',r=True)
        mc.move(-3,0,0,self.E.aimMicroCtls[0]+'_nul',r=True)
        mc.move(3,0,0,self.E.aimMicroCtls[1]+'_nul',r=True)

        
    def brow01(self):
        #2: Create Brow Ctls
        #brow_ctl
        util.createCtlGrp(
            self.B.bigBinds, self.B.bigCtls, self.B.ctlGrp, size=.7, shape='square'
            )
        util.offsetCtls(self.B.bigCtls, s=(2,1,1))
        util.scaleOrient(self.B.bigCtls,s=(1,1,-1))
        
        #brow_inner_ctl
        util.createCtlGrp(
            self.B.inBinds, self.B.inCtls, self.B.bigCtls, size=.4, shape='circle'
            )
        util.scaleOrient(self.B.inCtls,s=(1,1,-1))
        
        #brow_cor_ctl
        util.createCtlGrp(
            self.B.corBinds, self.B.corCtls, self.B.inCtls, size=.6, shape='triangle'
            )
        util.offsetCtls(self.B.corCtls,t=(0,1,0), r=(0,0,180), s=(.4,1,1) )
        util.scaleOrient(self.B.corCtls,s=(1,1,-1))
        
        #brow_peak_ctl
        util.createCtlGrp(
            self.B.peakBinds, self.B.peakCtls, self.B.bigCtls, size=.4, shape='circle'
            )
        util.scaleOrient(self.B.peakCtls,s=(1,1,-1))

        util.offsetCtls(self.B.ctls, t=(0,0,.5))
        
        mc.parent(self.B.ctlGrp, self.F.upCtl)

        
    def nose01(self):
        #0: Create Nose Bridge Ctls
        util.createCtlGrp(self.N.bridgeBind,self.N.bridgeCtl,self.F.upCtl,
          size=.8, shape='square', ori=False
          )
        util.offsetCtls(self.N.bridgeCtl,t=(0,0,2), s=(1,2,2))
        
        #0: Create Nose Ctls
        util.createCtlGrp(self.N.tipBind,self.N.ctl, self.N.bridgeCtl,
           size=.8, shape='square'
           )
        util.offsetCtls(self.N.ctl,t=(0,0,2))
         
        util.createCtlGrp(self.N.sneerBinds,self.N.sneerCtls, self.N.ctl,
           size=.5, shape='arch'
           )
        util.offsetCtls(self.N.sneerCtls, t=(0,0,1.7))
    
    def createGrps(self):
        mc.group(n=self.NTGrp, em=True)


    def colorCtls(self):
        red=(1,0,0)
        blue=(0,0,1)
        lightBlue = (.4,1.2,8.6)
        pink=(2.4,.6,.57)
        yellow=(1,1,0)
        purple=(.3,0,.7)
        
        util.overrideColor(
            [self.F.upCtl, self.F.jawCtl]
            + self.T.teethCtls
            + self.T.tongueCtls,
            color=yellow
            )
        util.overrideColor(
            [self.E.rotCtl,self.E.aimCtl]
            + self.E.ctls
            + self.E.aimMicroCtls,
            color=yellow
            )
        util.overrideColor(
            [self.F.loCtl,self.M.ctl,self.N.ctl,self.N.bridgeCtl],
            color=purple
            )
        
        list1 = self.C.ctls + self.M.cornerCtls + self.L.ctls + self.B.bigCtls + self.B.inCtls + self.B.corCtls + self.B.peakCtls
        util.overrideColor([d for d in list1 if '_r_' in d], color=red)
        util.overrideColor([d for d in list1 if '_l_' in d], color=blue)
        
        list2 = self.M.lipCtls+sum(self.L.microCtls,[])+self.N.sneerCtls
        util.overrideColor([d for d in list2 if '_r_' in d], color=pink)
        util.overrideColor([d for d in list2 if '_l_' in d], color=lightBlue)
        util.overrideColor([d for d in list2 if '_m_' in d], color=yellow)
    
    def face02(self):
        for bind in self.allBinds:
            opm_baker.bake_transform_to_offset_parent_matrix(bind)
        #1: connect face upper bind
        util.connectTransform(self.F.upCtl, self.F.upBind)
        #1: Parent constraint face lower bind
        util.connectTransform(self.F.loCtl, self.F.loBind)
        #1: Parent constraint jaw bind
        util.connectTransform(self.F.jawCtl, self.F.jawBind)
        
        
    def mouth02(self):
        P1=self.F.upCtl
        P2=self.F.jawCtl
        P3=self.M.ctl
        #1: Create Bindmeshes
        mouth.createBindmeshes(
            self.M.bindmeshes, self.M.drivs, self.M.bindmeshesGrp
            )

        #2: Create Clusters on Bindmeshes
            #big clus
        mouth.createClsGrp(
            self.M.clus, self.F.loBind, self.M.bindmeshes, self.M.clusGrp
            )
            #jaw clus
                #upper
        upWeights = [.6,.8,1,.8,.6]
        mouth.createClsGrp(
            self.M.jawClus[0], self.F.upBind, self.M.bindmeshes[1:6],
            self.M.clusGrp, weights=upWeights
            )
                #lower
        loWeights = [.6,.8,1,.8,.6]
        mouth.createClsGrp(
            self.M.jawClus[1], self.F.jawBind, self.M.bindmeshes[7:],
            self.M.clusGrp, weights=loWeights
            )
            #corner clus
        mouth.createClsGrp(
            self.M.cornerClus[0], self.M.ctl,
            self.M.bindmeshes[0], self.M.clusGrp
            )
        mouth.createClsGrp(
            self.M.cornerClus[1], self.M.ctl,
            self.M.bindmeshes[6], self.M.clusGrp
            )
            
        #3: Skin bindmeshes with driver
        mouth.skinBindmeshes(self.M.bindmeshes, self.M.drivs)

        #4: Connect Ctls
            #big ctl
        mouth.connectBigClus(self.M.clus+'_nul', P3, self.F.loCtl)
            #jaw ctl
        util.connectTransform(P1, self.M.jawClus[0]+'_nul')
        util.connectTransform(P2, self.M.jawClus[1]+'_nul')
        
            #corner ctl
        for clus, ctl in zip(self.M.cornerClus, self.M.cornerCtls):
            util.createAutoGrp(ctl+'_nul', P3, name=ctl+'_auto')
            mouth.cornerCtls(ctl, clus, P1, P2)

        #5: Create uvPin on Bindmeshes
        mouth.createUvPin(self.M.uvPins, self.M.bindmeshes)
        
        #6: Create&connect lip drivers&lip ctls to uvPins
        mouth.lipDrivers(
            self.M.lipDrivs, self.M.uvPins, self.M.lipCtls, self.M.lipDrivGrp
            )
        #7: Skin lip driver joints to lip curves
         #0,1,2,3,4,5,6
        util.bindSkin(self.M.lipDrivs[0:7], self.M.upCrv)
         #6,7,8,9,10,11,0
        util.bindSkin(self.M.lipDrivs[6:]+[self.M.lipDrivs[0]], self.M.loCrv)
        #1: Connect Blendshape weight to translate value of mouth corner ctrls
        mouth.connectBs(self.M.cornerCtls, self.M.blendCrvs, self.M.bsNode)
    
    def cheek02(self):
        #1: Cheek ctls follow mCorner ctls
        cheek.createDrv(self.C.drvs,self.M.cornerCtls,self.F.root)
        #2: Create Auto grp
        for ctl in self.C.ctls: util.createAutoGrp(ctl, ctl+'_orient')
        #3: Connect Auto grp
        cheek.connectCtls(self.C.ctls[0:2], self.C.drvs, (.2,.5,.1)) #upper
        cheek.connectCtls(self.C.ctls[2:4], self.C.drvs, (.5,.7,.5)) #mid
        cheek.connectCtls(self.C.ctls[4:6], self.C.drvs, (.5,1.4,.2)) #low
        #2: Cheek binds follow mCorner ctls
        cheek.connectBinds(self.C.ctls, self.C.binds)
        
    def teethTongue02(self):
        P1 = self.F.upBind
        P2 = self.F.jawBind
        '''
        #6: Connect Teeth Ctrl
        mc.parentConstraint(P1,self.T.teethCtls[0]+'_nul',mo=True)
        mc.parentConstraint(P2,self.T.teethCtls[1]+'_nul',mo=True)
        util.parentConstIterate(self.T.teethCtls, self.T.teethBinds)
        
        #7: Connect Tongue Ctrl
        util.parentConstIterate(self.T.tongueCtls, self.T.tongueBinds)
        '''
        mc.parent(self.T.tongueCtls[0]+'_nul', self.F.jawCtl)
        
        
    def lid02(self):
        #2: Create Blendshape Node
        lid.createBsNode(
            self.L.rBsNodes, self.L.drivCrvs[:2], self.L.rBlendCrvs
            )
        lid.createBsNode(
            self.L.lBsNodes, self.L.drivCrvs[2:], self.L.lBlendCrvs
            )
        
        #3: Connect Blendshape weight to translate value of mouth corner ctrls
        #first two elements (right ctrls)
        #last two elements (left ctrls)
        lid.connectBs(
            self.L.ctls[:2], self.L.rBlendCrvs, self.L.rBsNodes
            ) 
        lid.connectBs(
            self.L.ctls[2:], self.L.lBlendCrvs, self.L.lBsNodes
            ) 
    
    def eye02(self):
        #5: Connect Eye Ctls
        eye.connectEyeCtls(
            self.E.ctls, self.E.rotCtl, self.E.aimCtl,
            self.E.aimMicroCtls, self.E.binds
            )
        
        
    def brow02(self):
        for ctl,bind in zip(self.B.ctls, self.B.binds):
            util.connectTransform(ctl, bind, reverseZ=True)

    
    def nose02(self):
        util.createAutoGrp(self.N.bridgeCtl, self.N.bridgeCtl+'_nul')
        
        nose.connectNoseFollow(
            self.N.bridgeCtl, self.N.bridgeBind, self.F.loCtl
            )

        
    def arrangeGrps(self):
        #these are rather simple parent commands,
        #we keep going even if there's an error.
        try:
            mc.parent(
                    self.M.upCrv, self.M.loCrv,self.M.crv,
                    self.M.bindmeshesGrp, self.M.clusGrp,
                    self.M.drivGrp,self.M.lipDrivGrp,
                    self.M.blendCrvGrp, 
                    self.L.crvs,self.L.drivCrvs,
                    self.L.drivGrp,self.L.lidDrivGrp,
                    self.L.rBlendCrvGrp, self.L.lBlendCrvGrp,
                    self.NTGrp)
        except: print('rig_grp parent skipped')

#-----------------------------------------------------EXECUTE---------------------------------------------------------------

###mouth left driver scale orient x -1
###new hierarchy

###need to fix eyes