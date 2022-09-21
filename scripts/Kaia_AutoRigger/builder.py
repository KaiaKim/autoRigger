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
from Kaia_AutoRigger.modules import stretchyIk

importlib.reload(util)
importlib.reload(getset)
importlib.reload(mouth)
importlib.reload(lid)
importlib.reload(nose)
importlib.reload(cheek)
importlib.reload(opm_baker)
importlib.reload(stretchyIk)

###-----------------------------------------------------CLASS---------------------------------------------------
class BuildRig():
    def __init__(self):
        pass

    def face01(self):
        #0: Import face binds if no face_BIND_Grp in scene
        if mc.ls(self.bindGrp) == []:
            mc.file(self.mayascripts+'/Kaia_AutoRigger/prepare/faceBinds.ma',i=True)
            
        #0: Match face skeleton to guide
        guides = [d.replace('_bind','_guide') for d in self.allBinds]
        util.matchTransformIterate(guides, self.allBinds) #match Transform
        

        for bind in self.allBinds:
            if mc.ls(bind) != []: #lid binds, lip binds doesn't exist yet, so they won't be affected
                opm_baker.bake_transform_to_offset_parent_matrix(bind) 
        
        #1: Create Face Ctls
        mc.group(em=True,n=self.F.root)
        
        mc.connectAttr(
                self.F.bind+'.worldMatrix', self.F.root+'.offsetParentMatrix'
                )
        mc.disconnectAttr(
                self.F.bind+'.worldMatrix', self.F.root+'.offsetParentMatrix'
                )
        
        #1: Create Upper Face Ctls
        util.createCtlGrp(
            self.F.upBind, self.F.upCtl, self.F.root,
            ori=False, size=1, shape='triangle'
            )
        util.offsetCtls(self.F.upCtl, t=(0,-1.5,12), s=(1,.4,1))
        
        #1: Create Lower Face Ctls
        util.createCtlGrp(
            self.F.loBind, self.F.loCtl, self.F.root,
            ori=False, size=12, shape='semiCircle'
            )
        util.offsetCtls(self.F.loCtl, t=(0,-6,0), r=(180,0,0))
        
        #1: Create Jaw Ctls
        util.createCtlGrp(
            self.F.jawBind, self.F.jawCtl, self.F.loCtl,
            size=1, shape='triangle'
            )
        util.offsetCtls(self.F.jawCtl, t=(0,-6,10), r=(180,0,0), s=(1,.6,1))
   
    
    def mouth01(self):
        #0: Duplicate lip curves
        mc.duplicate(self.M.upGuide, n=self.M.upCrv)
        mc.duplicate(self.M.loGuide, n=self.M.loCrv)
        
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
        #5: Lock Ctls
        for ctl in self.M.cornerCtls: 
            util.handleToggle(ctl)
            util.lockCtls(ctl, r=True)
            mc.setAttr(ctl+'.tz', lock=True, keyable=False, channelBox=False)

        util.lockCtls(self.M.lipCtls, r=True)

        #6: Normalize Corner Ctls
        util.normalizeCtls(self.M.cornerCtls,val=(2,2,2))
        
            ###Mouth crv blendshapes
        #1: Duplicate orig curve
        mouth.createBsCrv(self.M.blendGuides,self.M.rBlendCrvs,self.M.blendCrvGrp)
        mouth.createBsCrv(self.M.blendGuides,self.M.lBlendCrvs,self.M.blendCrvGrp)
        #2: Create Blendshape Node
        mouth.createBsNode(self.M.bsNode, self.M.crv, self.M.blendCrvs)
        #3: Set blendshape cv weight(sepereate left & right weight)
        mouth.setBsCvWeight(self.M.bsNode)
        

    def teethTongue01(self):
        #teeth ctrls
        util.createCtlGrp(self.TE.binds, self.TE.ctls, self.F.root,
           size=.7, shape='semiCircle')
        util.offsetCtls(self.TE.ctls,t=(6,0,3))
        util.offsetCtls(self.TE.ctls[1],s=(1,-1,1))

        #tongue ctrls
        stretchyIk.stretchyIKMaker(self.TO, section=2, degree=3)
        mc.parent(self.TO.fkCtls[0]+'_nul', self.F.root)

        
    def lid01(self):
        #0: Duplicate Lid R curves
        mc.duplicate(self.L.guides[0], n=self.L.crvs[0])
        mc.duplicate(self.L.guides[1], n=self.L.crvs[1])
        
        #1: Mirror Lid R Curves to L
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
            
            #6: Lock Ctls
            util.lockCtls(self.L.microCtls[i], r=True)

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
        lid.createBsCrv(self.L.blendGuides[0], self.L.blendCrvs[0], self.L.blendCrvGrp)
        lid.createBsCrv(self.L.blendGuides[1], self.L.blendCrvs[1], self.L.blendCrvGrp)
        
        for r,l in zip(self.L.blendCrvs[0], self.L.blendCrvs[2]):
            getset.mirrorObj(l,r)
            
        for r,l in zip(self.L.blendCrvs[1], self.L.blendCrvs[3]):
            getset.mirrorObj(l,r)
        
        
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


    
        
    def face02(self):
        #1: connect face root
        mc.parentConstraint(self.F.root, self.F.bind, mo=False)
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
        mouth.connectBs(self.M.cornerCtls[0], self.M.rBlendCrvs, self.M.bsNode)
        mouth.connectBs(self.M.cornerCtls[1], self.M.lBlendCrvs, self.M.bsNode)
        
    def teethTongue02(self):
        
        P1 = self.F.upCtl
        P2 = self.F.jawCtl

        #6: Connect Teeth Ctrl
        util.parentConstIterate(self.TE.ctls, self.TE.binds)
        
        mc.parentConstraint(P1, self.TE.ctls[0]+'_nul', mo=True)
        mc.parentConstraint(P2, self.TE.ctls[1]+'_nul', mo=True)
        
        #7: Connect Tongue Ctrl
        mc.parentConstraint(P2, self.TO.fkCtls[0]+'_nul', mo=True)

        
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
        #1: Nose Follow Auto
        util.createAutoGrp(self.N.bridgeCtl, self.N.bridgeCtl+'_nul')
        nose.connectNoseFollow(
            self.N.bridgeCtl, self.N.bridgeBind, self.F.loCtl
            )

        #2: Connect Ctls
        util.connectTransform(self.N.bridgeCtl, self.N.bridgeBind)
        util.connectTransform(self.N.ctl, self.N.tipBind)
        util.connectTransform(self.N.sneerCtls[0], self.N.sneerBinds[0])
        util.connectTransform(self.N.sneerCtls[1], self.N.sneerBinds[1])
        
        
    def arrangeGrps(self, clean=True):
        childs = [
                self.M.upCrv, self.M.loCrv,self.M.crv,
                self.M.bindmeshesGrp, self.M.clusGrp,
                self.M.drivGrp,self.M.lipDrivGrp,
                self.M.blendCrvGrp, 
                self.L.crvs,self.L.drivCrvs,
                self.L.drivGrp,self.L.lidDrivGrp,
                self.L.blendCrvGrp,
                self.TO.clsGrp, self.TO.ikHand, self.TO.crv
        ]
        
        for c in childs:
            try:
                mc.parent(c,self.NTGrp)
            except:
                mc.warning('parent '+c+' to '+self.NTGrp+' skipped')
        
        mc.sets(self.M.rBlendCrvs, self.L.blendCrvs[0][0], self.L.blendCrvs[1][0], n=self.BSCrvSet)
        
        mc.hide(self.guideGrp, self.NTGrp, self.bindGrp)
        if clean == True:
            mc.delete(self.guideGrp)
            mc.delete(self.noSelectLayer)
        
        ###temp
        util.lockCtls(self.allCtls, s=True)
        
    def colorCtls(self):
        red=(1,0,0)
        blue=(0,0,1)
        lightBlue = (.4,1.2,8.6)
        pink=(2.4,.6,.57)
        yellow=(1,1,0)
        purple=(.3,0,.7)
        lavender=(.6,.3,1)
        magenta=(1,0,1)
        
        util.overrideColor(
            [self.F.upCtl, self.F.jawCtl]
            + self.TO.ikCtls,
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
        util.overrideColor(self.TO.fkCtls, color=magenta)
        util.overrideColor(self.TE.ctls, color=lavender)

        
        list1 = self.M.cornerCtls + self.L.ctls + self.B.bigCtls + self.B.inCtls + self.B.corCtls + self.B.peakCtls
        util.overrideColor([d for d in list1 if '_r_' in d], color=red)
        util.overrideColor([d for d in list1 if '_l_' in d], color=blue)
        
        list2 = self.M.lipCtls+sum(self.L.microCtls,[])+self.N.sneerCtls
        util.overrideColor([d for d in list2 if '_r_' in d], color=pink)
        util.overrideColor([d for d in list2 if '_l_' in d], color=lightBlue)
        util.overrideColor([d for d in list2 if '_m_' in d], color=yellow)
#-----------------------------------------------------EXECUTE---------------------------------------------------------------

###mouth left driver scale orient x -1
###new hierarchy

###need to fix eyes