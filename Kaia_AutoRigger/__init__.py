import maya.cmds as cmds
from functools import partial
import importlib

from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
importlib.reload(ModFunc)
importlib.reload(MouthFunc)

class AutoRigMouth():
    def __init__(self):
        self.winTitle = 'Kaia\'s auto rigger_mouth' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigMouth' #this needs to be ac word that has no spaces or it won't work! #node name

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
        
        self.lipMicroCtlGrp = 'lip_micro_ctl_grp'
        self.lipMicroCtls = []
        self.lipMacroCtlGrp = 'lip_ctl_grp'
        self.lipMacroCtls = []
        
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
        cmds.button( label='Import',c=lambda x:cmds.file('D:/Thesis/Assets/Scripts/Rigging/Kaia_AutoRig_mouth_files/faceBindJoints.ma',i=True))
        cmds.text( label='Lip Curves')
        cmds.button( label='Import',c=lambda x:cmds.file('D:/Thesis/Assets/Scripts/Rigging/Kaia_AutoRig_mouth_files/mouthCurve.ma',i=True))

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
        cmds.button( label='assign', c=lambda x:self.assignDelete('self.upperVerts','ass') )
        cmds.button( label='delete', c=lambda x:self.assignDelete('self.upperVerts','del') )

        cmds.text( label='Lower Lip Verts')
        cmds.button( label='assign', c=lambda x:self.assignDelete('self.lowerVerts','ass') )
        cmds.button( label='delete', c=lambda x:self.assignDelete('self.lowerVerts','del') )

        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Functions', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text( label='It only works with template joint hierarchy.')
        cmds.text( label='Make sure you have everything assigned!')
        cmds.button(label='Build Mouth Rig 01',c=self.buildMouthRig01)
        cmds.button(label='5: Finish Adjusting Orient', enable=False)
        cmds.button(label='7: Attach Jaw Clusters to Jaw',c=self._attachJawCls)
        cmds.button(label='8: Create lipCV Clusters on lip_curves',c=self._createClsOnLipCurv)
        cmds.button(label='9: Attach Lip Controllers on lipCV', c=self._attachLipCtlsOnJawCls)
        cmds.button(label='00: Arrange Groups',c=self.arrangeGrps)
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Blendshapes', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text(label='Create duplicate curves for blendshapes?')
        
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
        
        #4: Create Lip Micro Controllers
        self._createMouthCtrls()
    
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
            cmds.parent(self.lipMicroCtlGrp, self.animGrp)
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

        
    def _createMouthCtrls(self):
        #micro ctrls
        self.lipMicroCtls = ModFunc._createCtrlGrp(self.mouthFols,self.lipMicroCtlGrp,offset=(0,0,1))
        
        for i in self.lipMicroCtls:
            ModFunc._overrideColor(i['ctl'], color=(1,1,0))
            
        #macro ctrls
        macroFols = [d for d in self.mouthFols if '_m_' in d] #'mouth_upper_m_fol','mouth_lower_m_fol'
        self.lipMacroCtls = ModFunc._createCtrlGrp(macroFols, self.lipMacroCtlGrp, offset=(0,0,1.5), prefix='MACRO_', shape='square')
        
        for i in self.lipMacroCtls:
            ModFunc._overrideColor(i['ctl'], color=(1,1,0))
        
    def _attachJawCls(self,_):
        TopBotMidCls = [d for d in self.jawCls if '0' not in d]
        for clus in TopBotMidCls:
            #We're gonna parent constraint jawClusters directly to the mouth macro controllers
            cmds.parentConstraint(self.faceLowerBind,self.jawBind,clus,mo=True)
            #set mouth constraint weight value
            MouthFunc.setMouthConstWeightVal(clus, self.faceLowerBind,self.jawBind,follow00=.8,follow01=.95) 
            
        inbetweenCls = [d for d in self.jawCls if '0' in d]
        for clus in inbetweenCls:
            if 'upper' in clus:
                parent1=self.lipMacroCtls[0]['ctl'] #macro_mouth_upper_ctl
            elif 'lower' in clus:
                parent1=self.lipMacroCtls[1]['ctl'] #macro_mouth_lower_ctl
            
            if '_r_' in clus:
                parent2=self.jawCls[0] #mouth_corner_r_cls
            if '_l_' in clus:
                parent2=self.jawCls[len(self.jawCls)//2] #mouth_corner_l_cls
                
            cmds.parentConstraint(parent1,parent2,clus,mo=True)
            #set mouth constraint weight value
            MouthFunc.setMouthConstWeightVal(clus, parent1,parent2,follow00=.8,follow01=.95) 
            
    
    def _createClsOnLipCurv(self,_):
        clsList = ModFunc._createClsOn2Curv(self.lipUpperCurv, self.lipLowerCurv, self.lipCvClsGrp)
        self.lipCvCls = MouthFunc._mouthRigNamer(clsList, prefix='lipCV',suffix='_cls')
        
    def _attachLipCtlsOnJawCls(self,_):
        nulList = [d['ctl'] for d in self.lipMicroCtls]
        ###not parent constraint? hard parenting under micro ctrls with offset group?
        ModFunc._parentConstIterate(nulList, self.lipCvCls)
        
        

###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run=AutoRigMouth()

###orient edit mode (unparent the clusters - edit orient(save/load orient data) - reparent the clusters)