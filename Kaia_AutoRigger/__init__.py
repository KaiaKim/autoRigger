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
class AutoRigFace():
    def __init__(self):
        self.usd = cmds.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
        self.mayascripts = '%s/%s' % (self.usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts
        
        self.winTitle = 'Kaia\'s auto rigger' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigFace' #this needs to be ac word that has no spaces or it won't work! #node name
        
        ###
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
        self.mouthCrv = None
        
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
        
    def quickTestData(self,_):
        #some hard coded data for quick testing
        self.lipUpperVerts=['forBody.vtx[3314]', 'forBody.vtx[3315]', 'forBody.vtx[3317]', 'forBody.vtx[3320]', 'forBody.vtx[3321]', 'forBody.vtx[3322]', 'forBody.vtx[3325]', 'forBody.vtx[3326]', 'forBody.vtx[3327]', 'forBody.vtx[3331]', 'forBody.vtx[3332]', 'forBody.vtx[3335]', 'forBody.vtx[3337]', 'forBody.vtx[3495]', 'forBody.vtx[3818]', 'forBody.vtx[4010]', 'forBody.vtx[4200]', 'forBody.vtx[4386]', 'forBody.vtx[4574]', 'forBody.vtx[4751]', 'forBody.vtx[4918]', 'forBody.vtx[5079]', 'forBody.vtx[5215]', 'forBody.vtx[5350]', 'forBody.vtx[5485]', 'forBody.vtx[5620]', 'forBody.vtx[5741]']

        self.lipLowerVerts=['forBody.vtx[3313]', 'forBody.vtx[3316]', 'forBody.vtx[3318]', 'forBody.vtx[3319]', 'forBody.vtx[3323]', 'forBody.vtx[3324]', 'forBody.vtx[3327]', 'forBody.vtx[3328]', 'forBody.vtx[3329]', 'forBody.vtx[3330]', 'forBody.vtx[3333]', 'forBody.vtx[3334]', 'forBody.vtx[3336]', 'forBody.vtx[3494]', 'forBody.vtx[3729]', 'forBody.vtx[3950]', 'forBody.vtx[4144]', 'forBody.vtx[4334]', 'forBody.vtx[4526]', 'forBody.vtx[4707]', 'forBody.vtx[4878]', 'forBody.vtx[5043]', 'forBody.vtx[5183]', 'forBody.vtx[5322]', 'forBody.vtx[5461]', 'forBody.vtx[5600]', 'forBody.vtx[5741]']

        self.lidUpperRVerts=['forBody.vtx[6251]', 'forBody.vtx[6252]', 'forBody.vtx[6253]', 'forBody.vtx[6254]', 'forBody.vtx[6255]', 'forBody.vtx[6256]', 'forBody.vtx[6257]', 'forBody.vtx[6258]', 'forBody.vtx[6259]', 'forBody.vtx[6260]', 'forBody.vtx[6261]', 'forBody.vtx[6262]', 'forBody.vtx[6263]', 'forBody.vtx[6264]', 'forBody.vtx[6266]', 'forBody.vtx[6306]', 'forBody.vtx[6347]']

        self.lidLowerRVerts=['forBody.vtx[6239]', 'forBody.vtx[6240]', 'forBody.vtx[6241]', 'forBody.vtx[6242]', 'forBody.vtx[6243]', 'forBody.vtx[6244]', 'forBody.vtx[6245]', 'forBody.vtx[6246]', 'forBody.vtx[6247]', 'forBody.vtx[6248]', 'forBody.vtx[6249]', 'forBody.vtx[6250]', 'forBody.vtx[6251]', 'forBody.vtx[6277]', 'forBody.vtx[6313]', 'forBody.vtx[6347]', 'forBody.vtx[6348]']

    def assignDelete(self,data,flag):
        if flag=='ass':
            data=cmds.ls(sl=True,fl=True)
            print(data)
        elif flag=='del':
            data=None
    
    def orientData(self,flag=''):
        if flag=='load':
            #read json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/ctlOrient.json',"r") as rfile:
                data = json.load(rfile)
        
        if flag=='mirror' or flag=='save':
            #get transform
            allCtls = self.lipCtls + self.mouthCtls + self.mCornerCtls
            orients = [d['ori'] for d in allCtls]
            data = ModFunc._getTransformData(orients, t=False, r=True)
        
        if flag=='mirror':
            #modify data
            rightData = [d for d in data if '_r_' in d['name']]
            mirrorData = rightData
            for i in mirrorData:
                i['name'] = i['name'].replace('_r_','_l_')
                (rx,ry,rz) = i['rot']
                i['rot'] = (rx,-ry,-rz)
            ModFunc._applyTransformData(mirrorData)
        
        if flag=='load':
            #apply transform
            ModFunc._applyTransformData(data)
        
        if flag=='save':
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/ctlOrient.json', "w") as wfile:
                json.dump(data, wfile)


    def latticeData(self,flag=''): #mirror lattice point pos
        if flag=='load':
            #read json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/latticePtPos.json',"r") as rfile:
                ptPos = json.load(rfile)
        
        if flag=='mirror' or flag=='save':
            #get transform
            ltsPt = cmds.ls(self.eyeballRLtc + 'Lattice' + '.pt[*][*][*]', fl=1)
            ptPos = ModFunc._getTransformData(ltsPt, t=True, r=False, ws=True)
        
        if flag=='mirror':
            #modify data
            mirrorPos = ptPos
            for i in mirrorPos:
                i['name'] = i['name'].replace('_r_','_l_')
                x,y,z = i['pos']
                i['pos'] = (-x,y,z)
            ModFunc._applyTransformData(mirrorPos)
        
        if flag=='load':
            #apply transform
            ModFunc._applyTransformData(ptPos, ws=True)
        
        if flag=='save':    
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/latticePtPos.json', "w") as wfile:
                json.dump(ptPos, wfile)
                
    def blendCrvData(self,flag=''):
        if flag=='load':
            #read json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/blendCrv.json',"r") as rfile:
                cvPos = json.load(rfile)
        
        if flag=='save':
            #get transform
            allCrv = self.mouthBlendCrvs + self.eyeBlendCrvs
            allCVs = []
            for i in allCrv:
                CVs = ModFunc._getCVs(i)
                allCVs += CVs
            cvPos = ModFunc._getTransformData(allCVs, t=True, r=False, os=True)

        if flag=='load':
            #apply transform
            ModFunc._applyTransformData(cvPos, os=True)
        
        if flag=='save':    
            #write json file
            with open(self.mayascripts+'/Kaia_AutoRigger/json/blendCrv.json', "w") as wfile:
                json.dump(cvPos, wfile)
                
    def mirrorBlendCrvMouth(self,_):
        #modify data mouth
        cvPos2 = MouthFunc._symmetricMouthCrv(self.mouthBlendCrvs)
        ModFunc._applyTransformData(cvPos2, os=True)
        cvPos3 = MouthFunc._matchCrvRtoL(cvPos2)
        ModFunc._applyTransformData(cvPos3, os=True)
        
    def mirrorBlendCrvEyes(self,_):
        #modify data eyes
        allCVs = []
        for i in self.eyeBlendCrvs:
            CVs = ModFunc._getCVs(i)
            allCVs += CVs
            
        cvPos = ModFunc._getTransformData(allCVs, t=True, r=False, os=True)
        cvPos5 = EyeFunc._mirrorCVs(cvPos)
        ModFunc._applyTransformData(cvPos5, os=True)
        
        cvPos = ModFunc._getTransformData(allCVs, t=True, r=False, os=True)
        cvPos4 = EyeFunc._matchCloseCrv(cvPos)
        ModFunc._applyTransformData(cvPos4, os=True)
        
    
    def buildMouthRig01(self,_):
        #0:Create Groups
        self.createGrps() 
        
        #1: Generate mouth_curve from lip_curves
        self.mouthCrv = MouthFunc._createMouthCrv(self.lipUpperCrv, self.lipLowerCrv)
        
        #1: Create lip_locs on lip verts & connect to lip_curves
        upperPos = ModFunc._getPosListFromVerts(self.lipUpperVerts)
        upperLocs = ModFunc._createLocsOnCurve(self.lipUpperCrv,upperPos,self.lipUpperLocGrp)
        upperLocs = MouthFunc._lipLocsNamer(upperLocs, prefix='lip_upper')
        
        lowerPos = ModFunc._getPosListFromVerts(self.lipLowerVerts)
        lowerLocs = ModFunc._createLocsOnCurve(self.lipLowerCrv,lowerPos,self.lipLowerLocGrp)
        lowerLocs = MouthFunc._lipLocsNamer(lowerLocs, prefix='lip_lower')
        
        self.lipLocs = upperLocs + lowerLocs
        
        #2: Aim constraint lip_locs to jaw_bind
        ModFunc._aimConstLocs(self.lipLocs, self.jawBind, upObj=self.faceLowerBind)
        
        #2: Create lip_bind_jnts && constraint to lip_locs
        self.lipBinds = ModFunc._createJntsOnLocs(self.lipLocs,self.faceLowerBind)
        
        #2: Create mouth drivers
        driverList = ModFunc._createJntsOnCVs(self.mouthCrv,self.mouthDriverGrp) 
        driverList = driverList[-1:] + driverList[:-1] #param 0 attachs to cv[1] for somehow, so I shifted last element to first position in list.
        self.mouthDrivers = MouthFunc._mouthRigNamer(driverList, prefix='mouth',suffix='_driver')
        
        #3: Create Bindmeshes on driver
        self.mouthBindmeshes = ModFunc._createBindmeshesOnJnts(self.mouthDrivers,self.mouthBindmeshesGrp)
        
        #4: Create Follicles on Bindmeshes
        self.mouthFols = ModFunc._createFolsOnBindmeshes(self.mouthBindmeshes,self.mouthFolGrp)
        
        #4: Create Clusters on Bindmeshes
        self.jawCls = ModFunc._createClsOnBindmeshes(self.mouthBindmeshes,self.jawClsGrp)
        
        #4: Create Ctrls
            #lip ctrls
        microNames = [d.replace('fol','ctl').replace('mouth','lip') for d in self.mouthFols]
        
        self.lipCtls = ModFunc._createCtrlGrp(self.mouthFols,microNames,self.lipCtlGrp)
        ModFunc._setOffset(self.lipCtls, t=(0,0,1), r=(90,0,0))
        MouthFunc._scaleOrient(self.lipCtls)
        ModFunc._overrideColor(microNames, color=(1,1,0))
            
            #mouth ctrls
        macroFols = [d for d in self.mouthFols if '_m_' in d] #'mouth_upper_m_fol','mouth_lower_m_fol'
        macroNames = [d.replace('fol','ctl') for d in macroFols]
        
        self.mouthCtls = ModFunc._createCtrlGrp(macroFols, macroNames, self.mouthCtlGrp, shape='square')
        ModFunc._setOffset(self.mouthCtls, t=(0,0,1.5), r=(90,0,0))
        MouthFunc._scaleOrient(self.mouthCtls)
        ModFunc._overrideColor(macroNames, color=(1,1,0))
        
            #corner ctrls
        cornerFols = [d for d in self.mouthFols if '_corner_' in d]
        cornerNames = [d.replace('fol','ctl') for d in cornerFols]
        
        self.mCornerCtls = ModFunc._createCtrlGrp(cornerFols, cornerNames, self.mCornerCtlGrp, shape='triangle')
        ModFunc._setOffset(self.mCornerCtls, t=(0,0,1), r=(90,0,0))
        MouthFunc._scaleOrient(self.mCornerCtls)
        ModFunc._overrideColor(cornerNames, color=(1,0,0))
        
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
        self.lidRBinds = ModFunc._createJntsOnLocs(self.lidRLocs,self.eyeSocketBindR)
        self.lidRBinds = ModFunc._createJntsOnLocs(self.lidLLocs,self.eyeSocketBindL)
        #5: Constraint to lid locs
        ModFunc._parentConstIterate(self.lidRLocs,self.lidRBinds)
        ModFunc._parentConstIterate(self.lidLLocs,self.lidLBinds)
        
        #4: Create Ctrls
            #blink ctrls
        blinkNames = []
        
        self.blinkCtls = EyeFunc._createBlinkCtrl(blinkNames,self.blinkCtlGrp)
        #EyeFunc._scaleOrient(self.blinkCtls)
        #ModFunc._overrideColor(microNames, color=(1,0,0))
        '''
        ModFunc._createClsOn2Curv()
        ModFunc._createCtrlGrp()
        
        EyeFunc._createLoftBall()
        EyeFunc._SlideOnSurface()
        '''
        
    def BuildMouthBlendshapes01(self,_):
        #Duplicate orig curve
        self.mouthBlendCrvs = MouthFunc._createBsCrv(self.mouthCrv,self.mouthBlendCrvGrp)
        #Create Blendshape Node
        bsNode = MouthFunc._createBsNode(self.mouthCrv, self.mouthBlendCrvs)
        #Set blendshape cv weight(sepereate left & right weight)
        MouthFunc._setBsCvWeight(bsNode)
        #Connect Blendshape weight to translate value of mouth corner ctrls
        MouthFunc._connectCornerCtrl(self.mCornerCtls, self.mouthBlendCrvs, bsNode)
        
        
            
            
    def BuildEyeBlendshapes01(self,_):
        ###right
        upperR = EyeFunc._createBsCrv(self.lidUpperRCrv,self.eyeBlendCrvGrp)
        lowerR = EyeFunc._createBsCrv(self.lidLowerRCrv,self.eyeBlendCrvGrp,newGrp=False)
        ###left
        upperL = EyeFunc._createBsCrv(self.lidUpperLCrv,self.eyeBlendCrvGrp,newGrp=False)
        lowerL = EyeFunc._createBsCrv(self.lidLowerLCrv,self.eyeBlendCrvGrp,newGrp=False)
        
        self.eyeBlendCrvs = upperR+lowerR+upperL+lowerL

    
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
        
    def enterOrientEdit(self,_):
        print('### enter orient edit mode ###')
        ###lip ctrl
        #unparent lipCvClsoffset from lip ctrl
        for j in self.lipCvCls:
            offGrp = j+'_offset'
            cmds.parent(offGrp, w=True) #parent to world

        ###mouth ctrl
        #delete parent constraint of jaw clusters
        #delete parent constraint of lip ctrl nuls
        
        ###mCorner ctrl
        #don't need anything

    
    def exitOrientEdit(self,_):
        print('### exit orient edit mode ###')
        for i,j in zip(self.lipCtls,self.lipCvCls):
            ctl = i['ctl']
            offGrp = j+'_offset'
            cmds.parent(offGrp,ctl)


    def changeCornerN(self,x,y,z):
        ModFunc._normalizeCtls(self.mCornerCtls,val=(x,y,z))
        
    def changeLipPull(self,one,two):
        for i in self.mCornerCtls:
            cmds.setAttr(i['ctl']+'.lipOnePull', one)
            cmds.setAttr(i['ctl']+'.lipTwoPull', two)
        
        
        
    
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run01=AutoRigFace()
UI.createWindow(run01)
### 3. orient edit mode (unparent the clusters - edit orient - reparent the clusters)


###DQ skin > attibute editor > support Non-rigid transformation ON

#mouth corner ctl > (translate x, y) > (input R, input G) > clamp node 
#multDoubleLinear
#> weight-(mouth wide curve, mouth small curve ) mouth curve blend