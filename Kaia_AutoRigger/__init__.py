import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
importlib.reload(ModFunc)
importlib.reload(MouthFunc)

###-----------------------------------------------------FILE PATH---------------------------------------------------
usd = cmds.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
mayascripts = '%s/%s' % (usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts

###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigMouth():
    def __init__(self):
        self.winTitle = 'Kaia\'s auto rigger_mouth' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigMouth' #this needs to be ac word that has no spaces or it won't work! #node name
        
        ###orient data
        self.orientJsonPath = mayascripts+'/Kaia_AutoRigger/orientData/testData.json'
        self.orientData = None
        
        ###
        self.faceRoot = 'face_root'
        self.animGrp = 'anim_grp'
        self.rigGrp = 'rig_grp'
        self.bindGrp = 'bind_grp'
        
        self.faceBind = 'face_bind' #This name is from the template file. No change this!
        self.faceLowerBind = 'face_lower_bind' #This name is from the template file. No change this!
        self.jawBind = 'jaw_bind' #This name is from the template file. No change this!
        
        self.lipUpperCurv = 'lip_upper_curve' #This name is from the template file. No change this!
        self.lipLowerCurv = 'lip_lower_curve' #This name is from the template file. No change this!
        self.lipCVList = []
        self.mouthCurv = None
        
        self.upperVerts = None
        self.lowerVerts = None
        
        self.lipUpperLocGrp = 'lip_upper_loc_grp' #Grp means group name. I will use these strings when I create the node.
        self.lipLowerLocGrp = 'lip_lower_loc_grp'
        self.lipLocs = []
        
        self.lipJnts = []
        
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
        
        self.lipCvClsGrp = 'lipCV_cls_grp'
        self.lipCvCls = []
        
        
        
        self.createWindow()

    def createWindow(self):
        #test to see if the window exists
        if cmds.window(self.winName, exists=True):
            cmds.deleteUI(self.winName) #we don't want to create extra windows

        cmds.window(self.winName, title=self.winTitle) #create a new window
        cmds.scrollLayout( 'scorllLayout', width=320) #makes your entire layout scrollable #first - main layout
        cmds.columnLayout( adjustableColumn=True ) #second layout - attaches to the main layout
        ###
        cmds.frameLayout( label='Template', collapsable=True, collapse=False )
        cmds.columnLayout()
        cmds.text(label='Load template files')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(150, 20))
        cmds.text( label='Face Bind Joints')
        cmds.button( label='Import',c=lambda x:cmds.file(mayascripts+'/templateFiles/faceBindJoints.ma',i=True))
        cmds.text( label='Lip Curves')
        cmds.button( label='Import',c=lambda x:cmds.file(mayascripts+'/templateFiles/mouthCurve.ma',i=True))

        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Assign', collapsable=True, collapse=False )

        cmds.columnLayout()
        cmds.text(label='Assign vertices from selection')
        cmds.button(label='Quick Test Data',c=self.quickTestData )

        cmds.setParent('..')

        cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(100, 20) ) #fourth layout - frame layout

        cmds.text( label='Upper Lip Verts')
        cmds.button( label='assign', c=lambda _:self.assignDelete('self.upperVerts','ass') )
        cmds.button( label='delete', c=lambda _:self.assignDelete('self.upperVerts','del') )

        cmds.text( label='Lower Lip Verts')
        cmds.button( label='assign', c=lambda _:self.assignDelete('self.lowerVerts','ass') )
        cmds.button( label='delete', c=lambda _:self.assignDelete('self.lowerVerts','del') )

        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Functions', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text( label='It only works with template joint hierarchy.')
        cmds.text( label='Make sure you have everything assigned!')
        cmds.button(label='Build Mouth Rig 01',c=self.buildMouthRig01)
        
        cmds.rowLayout(numberOfColumns=3)
        cmds.button( label='mirror orient R to L', c=self.mirrorOrient)
        cmds.button( label='save orient', c=self.saveOrient )
        cmds.button( label='load orient', c=self.loadOrient )
        cmds.setParent('..')
        
        cmds.button(label='Build Mouth Rig 02',c=self.buildMouthRig02)
        cmds.button(label='000: Arrange Groups',c=self.arrangeGrps)
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Blendshapes', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text(label='Create duplicate curves for blendshapes?')
        cmds.button(label='1: Duplicate Mouth Curve', c=self._duplicateMouthCurves)
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Extra', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )
        
        cmds.button(label='select Jaw Bind',c=lambda _:cmds.select(self.jawBind))

        cmds.showWindow()
        
    
    def quickTestData(self,_):
        #some hard coded data for quick testing
        self.upperVerts=['baseBody.vtx[12501]', 'baseBody.vtx[12502]', 'baseBody.vtx[12504]', 'baseBody.vtx[12507]', 'baseBody.vtx[12508]', 'baseBody.vtx[12509]', 'baseBody.vtx[12512]', 'baseBody.vtx[12513]', 'baseBody.vtx[12514]', 'baseBody.vtx[12518]', 'baseBody.vtx[12519]', 'baseBody.vtx[12522]', 'baseBody.vtx[12524]', 'baseBody.vtx[12682]', 'baseBody.vtx[15942]', 'baseBody.vtx[15943]', 'baseBody.vtx[15945]', 'baseBody.vtx[15948]', 'baseBody.vtx[15949]', 'baseBody.vtx[15950]', 'baseBody.vtx[15953]', 'baseBody.vtx[15954]', 'baseBody.vtx[15955]', 'baseBody.vtx[15959]', 'baseBody.vtx[15960]', 'baseBody.vtx[15963]', 'baseBody.vtx[15965]']
        self.lowerVerts=['baseBody.vtx[12500]', 'baseBody.vtx[12503]', 'baseBody.vtx[12505]', 'baseBody.vtx[12506]', 'baseBody.vtx[12510]', 'baseBody.vtx[12511]', 'baseBody.vtx[12514]', 'baseBody.vtx[12515]', 'baseBody.vtx[12516]', 'baseBody.vtx[12517]', 'baseBody.vtx[12520]', 'baseBody.vtx[12521]', 'baseBody.vtx[12523]', 'baseBody.vtx[12681]', 'baseBody.vtx[15941]', 'baseBody.vtx[15944]', 'baseBody.vtx[15946]', 'baseBody.vtx[15947]', 'baseBody.vtx[15951]', 'baseBody.vtx[15952]', 'baseBody.vtx[15955]', 'baseBody.vtx[15956]', 'baseBody.vtx[15957]', 'baseBody.vtx[15958]', 'baseBody.vtx[15961]', 'baseBody.vtx[15962]', 'baseBody.vtx[15964]']
        
    def assignDelete(self,data,flag):
        if flag=='ass':
            data=cmds.ls(sl=True,fl=True)
        elif flag=='del':
            data=None
    
    def mirrorOrient(self,_):
        #get transform
        allCtls = self.lipCtls + self.mouthCtls + self.mCornerCtls
        orients = [d['ori'] for d in allCtls]
        orientData = ModFunc._getTransformData(orients)
        rightOrientData = [d for d in orientData if '_r_' in d['name']]
        
        #modify data
        mirrorData = rightOrientData
        for i in mirrorData:
            i['name'] = i['name'].replace('_r_','_l_')
            (rx,ry,rz) = i['rot']
            ry = -ry
            rz = -rz
            i['rot'] = (rx,ry,rz)
        
        #apply transform
        ModFunc._applyTransformData(mirrorData)
        
    def saveOrient(self,_):
        #get transform
        allCtls = self.lipCtls + self.mouthCtls + self.mCornerCtls
        orients = [d['ori'] for d in allCtls]
        orientData = ModFunc._getTransformData(orients)
        
        #write json file
        with open(self.orientJsonPath, "w") as outfile:
            json.dump(orientData, outfile)

    def loadOrient(self,_):
        #read json file
        with open(self.orientJsonPath,"r") as read_file:
            orientData = json.load(read_file)
            
        #apply transform
        ModFunc._applyTransformData(orientData)

        
    def buildMouthRig01(self,_):
        #0:Create Groups
        self.createGrps()  
        #1: Generate mouth_curve from lip_curves
        self._createMouthCurv()
        #1: Create lip_locs on lip verts && connect to lip_curves
        self._createLipLocs()
        #2: Aim constraint lip_locs to jaw_bind
        ModFunc._aimConstLocs(self.lipLocs, self.jawBind, self.faceLowerBind)
        #2: Create lip_bind_jnts && constraint to lip_locs
        self.lipJnts = ModFunc._createJntsOnLocs(self.lipLocs,self.faceLowerBind)
        #2: Create drivers && connect to mouth CVs
        self._createMouthDrivers()
        #3: Create Bindmeshes on driver
        self.mouthBindmeshes = ModFunc._createBindmeshesOnJnts(self.mouthDrivers,self.mouthBindmeshesGrp)
        #4: Create Follicles on Bindmeshes
        self.mouthFols = ModFunc._createFolsOnBindmeshes(self.mouthBindmeshes,self.mouthFolGrp)
        #4: Create Clusters on Bindmeshes
        self.jawCls = ModFunc._createClsOnBindmeshes(self.mouthBindmeshes,self.jawClsGrp)
        #4: Create Lip Micro Ctrls
        self._createMouthCtls()
    
    def buildMouthRig02(self,_):
        #7: Attach Jaw Clusters to Jaw
        self._attachJawCls()
        #8: Create lipCV Clusters on lip_curves
        self._createClsOnLipCurv()
        #9: Attach Lip Ctrls on lipCV
        self._attachLipCtlsOnJawCls()
        
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
                self.lipUpperCurv, self.lipLowerCurv,
                self.lipUpperLocGrp, self.lipLowerLocGrp,
                self.mouthCurv,
                self.mouthBindmeshesGrp,self.jawClsGrp, self.mouthFolGrp,
                self.mouthDriverGrp, self.lipCvClsGrp,
                self.rigGrp)
        except: print('rig_grp parent skipped')
        
        try:
            cmds.parent(
                self.lipCtlGrp, self.mouthCtlGrp,
                self.animGrp)
        except: print('anim_grp parent skipped')

        
    def _createMouthCurv(self):
        upperCVs = cmds.ls(self.lipUpperCurv+'.cv[*]',fl=True) #get list of CVs from lip curves
        lowerCVs = cmds.ls(self.lipLowerCurv+'.cv[*]',fl=True)
        lowerCVs.reverse() #reverse list order so that it comes back to the start, as a circle

        self.lipCVList = upperCVs + lowerCVs
        
        sectionCount = len(self.lipCVList)-2
        self.mouthCurv = cmds.circle(n='mouth_curve', s=sectionCount )[0] #create a new curve
        
        cmds.makeIdentity(self.mouthCurv, apply=True) #freeze transformation
        cmds.xform(self.mouthCurv, piv=(0,0,0), ws=True) #set pivot to 0,0,0
        
        counter = 0 #this is a counter
        for i in range(sectionCount): #We're going to iterate through mouth curv(CVs)
            pos=cmds.xform(self.lipCVList[counter], q=True, t=True, ws=True) #get world position from the CV
            if counter==sectionCount/2: #there's two cvs overlapping on the corner. sectionCount/2 is the right corner CV.
                counter+=1 #We skip the overlapping cv by adding 1 to the counter
                   
            mouthCV = self.mouthCurv + '.cv[%d]'%i #get mouth CV
            cmds.move(pos[0],pos[1],pos[2],mouthCV) #snap mouth CV to the position

            counter+=1 #increase counter

        
    def _createLipLocs(self):
        upperLocsPos = ModFunc._createLocsOnCurve(self.lipUpperCurv,self.upperVerts,self.lipUpperLocGrp)
        upperLocs = MouthFunc._lipLocsNamer(upperLocsPos, prefix='upper_lip', suffix='_loc')

        lowerLocsPos = ModFunc._createLocsOnCurve(self.lipLowerCurv,self.lowerVerts,self.lipLowerLocGrp)
        lowerLocs = MouthFunc._lipLocsNamer(lowerLocsPos, prefix='lower_lip', suffix='_loc')
        
        self.lipLocs = upperLocs + lowerLocs
        
        
    def _createMouthDrivers(self):
        driverList = ModFunc._createJntsOnCVs(self.mouthCurv,self.mouthDriverGrp) 
        driverList = driverList[-1:] + driverList[:-1] #param 0 attachs to cv[1] for somehow, so I shifted last element to first position in list.
        
        self.mouthDrivers = MouthFunc._mouthRigNamer(driverList, prefix='mouth',suffix='_driver')

        
    def _createMouthCtls(self):
        ###maybe I need an offset group??
        #lip ctrls
        microNames = [d.replace('fol','ctl').replace('mouth','lip') for d in self.mouthFols]
        
        self.lipCtls = ModFunc._createCtrlGrp(self.mouthFols,microNames,self.lipCtlGrp)
        ModFunc._moveOffset(self.lipCtls, offset=(0,0,1))
        MouthFunc._scaleOrient(self.lipCtls)
        ModFunc._overrideColor(microNames, color=(1,1,0))
            
        #mouth ctrls
        macroFols = [d for d in self.mouthFols if '_m_' in d] #'mouth_upper_m_fol','mouth_lower_m_fol'
        macroNames = [d.replace('fol','ctl') for d in macroFols]
        
        self.mouthCtls = ModFunc._createCtrlGrp(macroFols, macroNames, self.mouthCtlGrp, shape='square')
        ModFunc._moveOffset(self.mouthCtls, offset=(0,0,1.5))
        MouthFunc._scaleOrient(self.mouthCtls)
        ModFunc._overrideColor(macroNames, color=(1,1,0))
        
        #corner ctrls
        cornerFols = [d for d in self.mouthFols if '_corner_' in d]
        cornerNames = [d.replace('fol','ctl') for d in cornerFols]
        
        self.mCornerCtls = ModFunc._createCtrlGrp(cornerFols, cornerNames, self.mCornerCtlGrp, shape='triangle')
        ModFunc._moveOffset(self.mCornerCtls, offset=(0,0,1.5))
        MouthFunc._scaleOrient(self.mCornerCtls)
        ModFunc._overrideColor(cornerNames, color=(1,0,0))
        
        #parent constraint micro nul2 group to macro ctl
        for i in self.lipCtls:
            if '_m_' in i['ctl']:
                i['nul2'] = cmds.group(i['ori'],n=i['nul']+'2') #create nul2 grp
                macro = i['ctl'].replace('lip','mouth') #micro_mouth_lower_m_ctl
                cmds.parentConstraint(macro,i['nul2'],mo=True)
                
        
    def _attachJawCls(self):
        #We're gonna parent constraint jawClusters directly to the mouth macro controllers
        for clus in self.jawCls:
            if '0' not in clus: #corner or mid
                parent1=self.faceLowerBind
                parent2=self.jawBind
            
            elif '0' in clus: #inbetween
                if 'upper' in clus:
                    parent1=self.mouthCtls[0]['ctl'] #macro_mouth_upper_ctl
                elif 'lower' in clus:
                    parent1=self.mouthCtls[1]['ctl'] #macro_mouth_lower_ctl
                
                if '_r_' in clus:
                    parent2=self.jawCls[0] #mouth_corner_r_cls
                if '_l_' in clus:
                    parent2=self.jawCls[len(self.jawCls)//2] #mouth_corner_l_cls
                
            cmds.parentConstraint(parent1,parent2,clus,mo=True)
            #set mouth constraint weight value
            MouthFunc._setWeightVal(clus, parent1,parent2, follow00=.7,follow01=.95) 
            
    
    def _createClsOnLipCurv(self):
        clsList = ModFunc._createClsOn2Curv(self.lipUpperCurv, self.lipLowerCurv, self.lipCvClsGrp)
        self.lipCvCls = MouthFunc._mouthRigNamer(clsList, prefix='lipCV',suffix='_cls')
        
    def _attachLipCtlsOnJawCls(self):
        ctlList = [d['ctl'] for d in self.lipCtls]
        ###not parent constraint? hard parenting under micro ctrls with offset group?
        ModFunc._parentConstIterate(ctlList, self.lipCvCls)
    
    def _setMouthCornerCtls(self,_):
        ###MouthFunc._setCornerPin()
        #Add Attribute: cornerPin min -1, max 1, default 0
        #connect to jaw cls W0, W1
        
        #set range node
        #cornerPin >> valueX , cornerPin >> valueY
        # minX 0 maxX 1, oldMinX -1 oldMaxX 1
        #outValueX >> face_Lower_bindW0
        #reverse node
        #outValueX >> inputX, outputX >> jaw_bindW1
        pass
        
        ###MouthFunc._setLipPull()
        #Add Attribute: lipOnePull min 0 max 1 default 0
        # connect to upper_lip_01_l_cls_parentConstraint1, lower_lip_01_l_cls_parentConstraint1
        # either follow the upper lip or the lip corner
        #lipOnePull >> lower_lip_ctlW0
        #reverse node
        #lipOnePull >> inputX, outputX >> lip_corner_l_clsW1
        
        #Add Attribute: lipTwoPull min 0 max 1 default 0
        pass
        
        #Session 4 (1:26:47~)
        

    def _duplicateMouthCurves(self,_):
        newCurv=cmds.duplicate(self.mouthCurv)
        cmds.select(newCurv)
        

###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run=AutoRigMouth()

###Tomorrow
### 1. save/load orient data >> OK
### 2. mirror orient R to L 
### 3. orient edit mode (unparent the clusters - edit orient - reparent the clusters)


###DQ skin > attibute editor > support Non-rigid transformation ON