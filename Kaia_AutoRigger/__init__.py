import maya.cmds as cmds
from functools import partial
import importlib
import json

from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import MouthFunc
from Kaia_AutoRigger import EyeFunc
importlib.reload(ModFunc)
importlib.reload(MouthFunc)
importlib.reload(EyeFunc)

###-----------------------------------------------------FILE PATH---------------------------------------------------
usd = cmds.internalVar(usd=True) #result: C:/Users/user/Documents/maya/2022/scripts/
mayascripts = '%s/%s' % (usd.rsplit('/', 3)[0], 'scripts') #result: C:/Users/user/Documents/maya/scripts

###-----------------------------------------------------CLASS---------------------------------------------------
class AutoRigFace():
    def __init__(self):
        self.winTitle = 'Kaia\'s auto rigger' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigFace' #this needs to be ac word that has no spaces or it won't work! #node name
        
        ###orient data
        self.orientJsonPath = mayascripts+'/Kaia_AutoRigger/data/'
        self.orientData = None
        
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
        
        self.lidUpperRCurv = 'upper_lid_r_curve' #No change this!
        self.lidLowerRCurv = 'lower_lid_r_curve' #No change this!
        
        self.lipUpperCurv = 'lip_upper_curve' #No change this!
        self.lipLowerCurv = 'lip_lower_curve' #No change this!
        self.lipCVList = []
        self.mouthCurv = None
        
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
        self.lipCvCls = [] #we need offset groups & hard parenting under lip Ctrl curv
        
        self.eyeLoft = None
        
        
        self.createWindow()

    def createWindow(self):
        #test to see if the window exists
        if cmds.window(self.winName, exists=True):
            cmds.deleteUI(self.winName) #we don't want to create extra windows

        cmds.window(self.winName, title=self.winTitle) #create a new window
        cmds.scrollLayout( 'scorllLayout', width=320) #makes your entire layout scrollable #first - main layout
        cmds.columnLayout( adjustableColumn=True ) #second layout - attaches to the main layout
        ###
        cmds.frameLayout( l='Template', collapsable=True, collapse=False )
        cmds.columnLayout()
        cmds.text(l='Load template files')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(150, 20))
        cmds.text( l='Face Bind Joints')
        cmds.button( l='Import',c=lambda x:cmds.file(mayascripts+'/Kaia_AutoRigger/templateFiles/faceBindJoints.ma',i=True))
        cmds.text( l='Lip Curves')
        cmds.button( l='Import',c=lambda x:cmds.file(mayascripts+'/Kaia_AutoRigger/templateFiles/lipCurves.ma',i=True))
        cmds.text( l='Eye Curves')
        cmds.button( l='Import',c=lambda x:cmds.file(mayascripts+'/Kaia_AutoRigger/templateFiles/eyeCurves.ma',i=True))

        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( l='Assign', collapsable=True, collapse=False )

        cmds.columnLayout()
        cmds.text(l='Assign vertices from selection')
        cmds.button(l='Quick Test Data',c=self.quickTestData )

        cmds.setParent('..')

        cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(100, 20) ) #fourth layout - frame layout

        cmds.text( l='Upper Lip Verts')
        cmds.button( l='assign', c=lambda _:self.assignDelete('self.lipUpperVerts','ass') )
        cmds.button( l='delete', c=lambda _:self.assignDelete('self.lipUpperVerts','del') )

        cmds.text( l='Lower Lip Verts')
        cmds.button( l='assign', c=lambda _:self.assignDelete('self.lipLowerVerts','ass') )
        cmds.button( l='delete', c=lambda _:self.assignDelete('self.lipLowerVerts','del') )

        cmds.text( l='Upper Eye Verts R')
        cmds.button( l='assign', c=lambda _:self.assignDelete('self.lidUpperRVerts','ass') )
        cmds.button( l='delete', c=lambda _:self.assignDelete('self.lidUpperRVerts','del') )

        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( l='Helper', collapsable=True, collapse=True)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text( l='! eye cluster name: eye_r_cls')
        cmds.text( l='! eye lattice name: eye_r_ffd1')
        
        cmds.rowLayout(numberOfColumns=4)
        cmds.text(l='eye lattice points: ')
        cmds.button( l='mirror R to L', c=self.mirrorLattice)
        cmds.button( l='save', c=self.saveLattice )
        cmds.button( l='load', c=self.loadLattice )
        cmds.setParent('..')
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( l='Build', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )
        
        cmds.button(l='Build Mouth Rig 01',c=self.buildMouthRig01)
        cmds.button(l='Build Eye Rig 01',c=self.buildEyeRig01)
        
        cmds.rowLayout(numberOfColumns=4)
        cmds.text( l='Ctrl orients: ')
        cmds.button( l='mirror R to L', c=self.mirrorOrient)
        cmds.button( l='save', c=self.saveOrient )
        cmds.button( l='load', c=self.loadOrient )
        cmds.setParent('..')
        
        cmds.button(l='Build Mouth Rig 02',c=self.buildMouthRig02)
        cmds.button(l='Build Eye Rig 02')

        
        cmds.button(l='000: Arrange Groups',c=self.arrangeGrps)
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( l='Blendshapes', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text(l='Create duplicate curves for blendshapes?')
        cmds.button(l='1: Duplicate Mouth Curve', c=self._duplicateMouthCurves)
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( l='Extra', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )
        
        cmds.button(l='select Jaw Bind',c=lambda _:cmds.select(self.jawBind))

        cmds.showWindow()
        
    
    def quickTestData(self,_):
        #some hard coded data for quick testing
        self.lipUpperVerts=['baseBody.vtx[7885]', 'baseBody.vtx[7886]', 'baseBody.vtx[7888]', 'baseBody.vtx[7891]', 'baseBody.vtx[7892]', 'baseBody.vtx[7893]', 'baseBody.vtx[7896]', 'baseBody.vtx[7897]', 'baseBody.vtx[7898]', 'baseBody.vtx[7902]', 'baseBody.vtx[7903]', 'baseBody.vtx[7906]', 'baseBody.vtx[7908]', 'baseBody.vtx[8066]', 'baseBody.vtx[8571]', 'baseBody.vtx[8850]', 'baseBody.vtx[9135]', 'baseBody.vtx[9424]', 'baseBody.vtx[9723]', 'baseBody.vtx[9999]', 'baseBody.vtx[10166]', 'baseBody.vtx[10327]', 'baseBody.vtx[10463]', 'baseBody.vtx[10598]', 'baseBody.vtx[10733]', 'baseBody.vtx[10868]', 'baseBody.vtx[10989]']
        self.lipLowerVerts=['baseBody.vtx[7884]', 'baseBody.vtx[7887]', 'baseBody.vtx[7889]', 'baseBody.vtx[7890]', 'baseBody.vtx[7894]', 'baseBody.vtx[7895]', 'baseBody.vtx[7898]', 'baseBody.vtx[7899]', 'baseBody.vtx[7900]', 'baseBody.vtx[7901]', 'baseBody.vtx[7904]', 'baseBody.vtx[7905]', 'baseBody.vtx[7907]', 'baseBody.vtx[8065]', 'baseBody.vtx[8482]', 'baseBody.vtx[8790]', 'baseBody.vtx[9079]', 'baseBody.vtx[9372]', 'baseBody.vtx[9675]', 'baseBody.vtx[9955]', 'baseBody.vtx[10126]', 'baseBody.vtx[10291]', 'baseBody.vtx[10431]', 'baseBody.vtx[10570]', 'baseBody.vtx[10709]', 'baseBody.vtx[10848]', 'baseBody.vtx[10989]']
        self.lidUpperRVerts=['baseBody.vtx[11499]', 'baseBody.vtx[11500]', 'baseBody.vtx[11501]', 'baseBody.vtx[11502]', 'baseBody.vtx[11503]', 'baseBody.vtx[11504]', 'baseBody.vtx[11505]', 'baseBody.vtx[11506]', 'baseBody.vtx[11507]', 'baseBody.vtx[11508]', 'baseBody.vtx[11509]', 'baseBody.vtx[11510]', 'baseBody.vtx[11511]', 'baseBody.vtx[11512]', 'baseBody.vtx[11514]', 'baseBody.vtx[11554]', 'baseBody.vtx[11595]']
        self.lidLowerRVerts=['baseBody.vtx[11487]', 'baseBody.vtx[11488]', 'baseBody.vtx[11489]', 'baseBody.vtx[11490]', 'baseBody.vtx[11491]', 'baseBody.vtx[11492]', 'baseBody.vtx[11493]', 'baseBody.vtx[11494]', 'baseBody.vtx[11495]', 'baseBody.vtx[11496]', 'baseBody.vtx[11497]', 'baseBody.vtx[11498]', 'baseBody.vtx[11499]', 'baseBody.vtx[11525]', 'baseBody.vtx[11561]', 'baseBody.vtx[11595]', 'baseBody.vtx[11596]']
        
    def assignDelete(self,data,flag):
        if flag=='ass':
            data=cmds.ls(sl=True,fl=True)
            print(data)
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
        orientData = ModFunc._getTransformData(orients, r=True)
        
        #write json file
        with open(self.orientJsonPath+'ctlOrient.json', "w") as outfile:
            json.dump(orientData, outfile)

    def loadOrient(self,_):
        #read json file
        with open(self.orientJsonPath+'ctlOrient.json',"r") as read_file:
            orientData = json.load(read_file)
            
        #apply transform
        ModFunc._applyTransformData(orientData, r=True)

    def mirrorLattice(self,_): #mirror lattice point pos
        #get pos
        ltsPt = cmds.ls(self.eyeballRLtc + 'Lattice' + '.pt[*][*][*]', fl=1)
        ptPos = ModFunc._getTransformData(ltsPt, wpos=True)
        
        #modify data
        mirrorPos = ptPos
        for i in mirrorPos:
            i['name'] = i['name'].replace('_r_','_l_')
            x,y,z = i['pos']
            i['pos'] = (-x,y,z)
            
        #apply transform
        ModFunc._applyTransformData(mirrorPos, wpos=True, opos=False)
        pass
        
    def saveLattice(self,_): #save lattice point pos
        #get transform
        
        ltsPt = cmds.ls(self.eyeballRLtc + 'Lattice' + '.pt[*][*][*]', fl=1)
        ptPos = ModFunc._getTransformData(ltsPt, wpos=True)
            
        #write json file
        with open(self.orientJsonPath+'latticePtPos.json', "w") as outfile:
            json.dump(ptPos, outfile)

    def loadLattice(self,_): #load lattice point pos
        #read json file
        with open(self.orientJsonPath+'latticePtPos.json',"r") as read_file:
            ptPos = json.load(read_file)
            
        #apply transform
        ModFunc._applyTransformData(ptPos, wpos=True, opos=False)
        
    def buildMouthRig01(self,_):
        #0:Create Groups
        self.createGrps()  
        #1: Generate mouth_curve from lip_curves
        self._createMouthCurv()
        #1: Create lip_locs on lip verts & connect to lip_curves
        self._createLipLocs()
        #2: Aim constraint lip_locs to jaw_bind
        ModFunc._aimConstLocs(self.lipLocs, self.jawBind, upObj=self.faceLowerBind)
        #2: Create lip_bind_jnts && constraint to lip_locs
        self.lipBinds = ModFunc._createJntsOnLocs(self.lipLocs,self.faceLowerBind)
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
        self._createLipCvCls()
        #10: Corner pin, Lip pull
        self._setMouthCornerCtls()
    
        
    def buildEyeRig01(self,_):
        #1: Mirror Lid Curves
        self.lidUpperLCurv = ModFunc._mirrorObjRtoL(self.lidUpperRCurv)
        self.lidLowerLCurv = ModFunc._mirrorObjRtoL(self.lidLowerRCurv)
        #2: Create lid locs on lid verts & connect to lid curves
        self._createLidLocs()
        #3: Aim constraint lid locs to eye socket bind
        ModFunc._aimConstLocs(self.lidRLocs,self.eyeSocketBindR)
        ModFunc._aimConstLocs(self.lidLLocs,self.eyeSocketBindL)
        #4: Create lid bind jnts
        self.lidRBinds = ModFunc._createJntsOnLocs(self.lidRLocs,self.eyeSocketBindR)
        self.lidRBinds = ModFunc._createJntsOnLocs(self.lidLLocs,self.eyeSocketBindL)
        #5: Constraint to lid locs
        ModFunc._parentConstIterate(self.lidRLocs,self.lidRBinds)
        ModFunc._parentConstIterate(self.lidLLocs,self.lidLBinds)
        '''
        ModFunc._createClsOn2Curv()
        ModFunc._createCtrlGrp()
        
        EyeFunc._createLoftBall()
        EyeFunc._SlideOnSurface()
        '''
        
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
                self.mouthDriverGrp,
                self.rigGrp)
        except: print('rig_grp parent skipped')
        
        try:
            cmds.parent(
                self.lipCtlGrp, self.mouthCtlGrp,
                self.animGrp)
        except: print('anim_grp parent skipped')

        
    def _createMouthCurv(self):
        upperCVs = ModFunc._getCVs(self.lipUpperCurv)
        lowerCVs = ModFunc._getCVs(self.lipLowerCurv)
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
        upperPos = ModFunc._getPosListFromVerts(self.lipUpperVerts)###if I rearrange the list according to xpos in the first place
        upperLocs = ModFunc._createLocsOnCurve(self.lipUpperCurv,upperPos,self.lipUpperLocGrp)###I don't have to use stupid dicList
        upperLocs = MouthFunc._lipLocsNamer(upperLocs, prefix='lip_upper')###But I also have to fix this
        
        lowerPos = ModFunc._getPosListFromVerts(self.lipLowerVerts)
        lowerLocs = ModFunc._createLocsOnCurve(self.lipLowerCurv,lowerPos,self.lipLowerLocGrp)
        lowerLocs = MouthFunc._lipLocsNamer(lowerLocs, prefix='lip_lower')
        
        self.lipLocs = upperLocs + lowerLocs
    
    
    def _createLidLocs(self):
        upperRPos = ModFunc._getPosListFromVerts(self.lidUpperRVerts)
        upperRLocs = ModFunc._createLocsOnCurve(self.lidUpperRCurv, upperRPos, self.lidRLocGrp)
        upperRLocs = EyeFunc._eyeLocsNamer(upperRLocs, prefix='lid_upper_r')
        
        upperLPos = ModFunc._mirrorPosX(upperRPos)
        upperLLocs = ModFunc._createLocsOnCurve(self.lidUpperLCurv, upperLPos, self.lidLLocGrp)
        upperLLocs = EyeFunc._eyeLocsNamer(upperLLocs, prefix='lid_upper_l')
        
        lowerRPos = ModFunc._getPosListFromVerts(self.lidLowerRVerts)
        lowerRLocs = ModFunc._createLocsOnCurve(self.lidLowerRCurv, lowerRPos, self.lidRLocGrp, newGrp=False)
        lowerRLocs = EyeFunc._eyeLocsNamer(lowerRLocs, prefix='lid_lower_r')
        
        lowerLPos = ModFunc._mirrorPosX(lowerRPos)
        lowerLLocs = ModFunc._createLocsOnCurve(self.lidLowerLCurv, lowerLPos, self.lidLLocGrp, newGrp=False)
        lowerLLocs = EyeFunc._eyeLocsNamer(lowerLLocs, prefix='lid_lower_l')
        
        self.lidRLocs = upperRLocs + lowerRLocs
        self.lidLLocs = upperLLocs + lowerLLocs
             
        
    def _createMouthDrivers(self):
        driverList = ModFunc._createJntsOnCVs(self.mouthCurv,self.mouthDriverGrp) 
        driverList = driverList[-1:] + driverList[:-1] #param 0 attachs to cv[1] for somehow, so I shifted last element to first position in list.
        
        self.mouthDrivers = MouthFunc._mouthRigNamer(driverList, prefix='mouth',suffix='_driver')

        
    def _createMouthCtls(self):
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
            MouthFunc._setWeightVal(clus, parent1,parent2)
    
    def _createLipCvCls(self):
        ctlList = [d['ctl'] for d in self.lipCtls]
        self.lipCvCls = MouthFunc._2CurvCvCls(self.lipUpperCurv, self.lipLowerCurv, ctlList)

    
    def _setMouthCornerCtls(self):
        cornerCtl = [d['ctl'] for d in self.mCornerCtls]
        cornerCls = [d for d in self.jawCls if '_corner_' in d] #left, right
        midCtl = [d['ctl'] for d in self.mouthCtls] #upper, lower
        inbetweenCls = [d for d in self.jawCls if re.findall('[0-9]+',d)!=[] ]
        
        #set corner pin
        MouthFunc._setCornerPin(cornerCtl[0], cornerCls[0], self.faceLowerBind,self.jawBind)
        MouthFunc._setCornerPin(cornerCtl[1], cornerCls[1], self.faceLowerBind,self.jawBind)

        #add attribute
        for ctl in cornerCtl:
            cmds.addAttr(ctl, shortName='lipOnePull', defaultValue=0, minValue=0, maxValue=1)
            cmds.addAttr(ctl, shortName='lipTwoPull', defaultValue=0, minValue=0, maxValue=1)
        
        ###--------------------MouthFunc._setLipPull()
        MouthFunc._connectLipPull(cornerCtl,inbetweenCls,midCtl,cornerCls)
        
        #set lip pull attribute
        for ctl in cornerCtl:
            cmds.setAttr(ctl+'.lipOnePull', 0.7)
            cmds.setAttr(ctl+'.lipTwoPull', 0.95)
        
        

    def _duplicateMouthCurves(self,_):
        newCurv=cmds.duplicate(self.mouthCurv)
        cmds.select(newCurv)
        

###-----------------------------------------------------EXECUTE---------------------------------------------------------------
run=AutoRigFace()

### 3. orient edit mode (unparent the clusters - edit orient - reparent the clusters)


###DQ skin > attibute editor > support Non-rigid transformation ON