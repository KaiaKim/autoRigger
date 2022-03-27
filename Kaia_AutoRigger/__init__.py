import maya.cmds as cmds
from functools import partial
import importlib

from Kaia_AutoRigger import ModFunc

importlib.reload(ModFunc)


class AutoRigMouth():
    def __init__(self):
        self.winTitle = 'Kaia\'s auto rigger_mouth' #this is the title of the window #display name
        self.winName = 'kaiaAutoRigMouth' #this needs to be ac word that has no spaces or it won't work! #node name

        ###
        self.faceLowerBind = 'face_lower_bind' #This name is from the template file. No change this!
        self.jawBind = 'jaw_bind' #This name is from the template file. No change this!
        
        self.upperCurv = 'lip_upper_curve' #This name is from the template file. No change this!
        self.lowerCurv = 'lip_lower_curve' #This name is from the template file. No change this!
        self.lipCVList = []
        self.mouthCurv = None
        
        self.upperVerts = None
        self.lowerVerts = None
        
        self.lipUpperLocGrp = 'lip_upper_loc_grp' #Grp means group name. I will use these strings when I create the node.
        self.lipLowerLocGrp = 'lip_lower_loc_grp'
        self.lipLocs = []
        
        self.lipJnts = []
        
        self.mouthDriversGrp = 'mouth_driver_jnt_grp'
        self.mouthDrivers = []
        
        self.mouthBindmeshesGrp = 'mouth_bindmesh_grp'
        self.mouthBindmeshes = []
        
        self.mouthClsGrp = 'mouth_cls_grp'
        self.mouthCls = []
        
        self.mouthFolGrp = 'mouth_fol_grp'
        self.mouthFols = []
        
        self.lipMicroCtlGrp = 'mouth_ctl_grp'
        self.lipMicroCtls = []
        
        self.jawClsGrp = 'jaw_Cls_grp'
        self.jawCls = []

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
        cmds.button(label='1: Generate mouth_curve from lip_curves',c=self._createMouthCurv)
        cmds.button(label='1: Create lip_locs on lip verts && connect to lip_curves', c=self._createLipLocs)
        cmds.button(label='2: Aim constraint lip_locs to jaw_bind', c=self._aimConstMouthLocs)
        cmds.button(label='2: Create lip_bind_jnts && constraint to lip_locs',c=self._createJntsOnMouthLocs)
        cmds.button(label='2: Create drivers && connect to mouth CVs',c=self._createMouthDrivers)
        cmds.button(label='3: Create Bindmeshes on drivers',c=self._createBindmeshesOnMouthDrivers)
        cmds.button(label='4: Create Follicles on Bindmeshes',c=self._createFolsOnMouthBindmeshes)
        cmds.button(label='4: Create Clusters on Bindmeshes',c=self._createClsOnMouthBindmeshes)
        cmds.button(label='4: Create Lip Micro Controllers',c=self._createMouthCtrls)
        cmds.button(label='5: Finish Adjusting Orient', enable=False)
        cmds.button(label='6: Attach Lip Micro Controllers to Follicles',c=self._attachLipMicroCtls)
        cmds.button(label='7: Attach Mouth Clusters to Jaw',c=self._attachMouthClsToJaw)
        cmds.button(label='8: Create Jaw Clusters on lip_curves',c=self._createJawClsOnLipCurv)
        cmds.button(label='9: Attach Lip Controllers on Jaw Clusters',c=self._attachLipCtlsOnJawCls)
        
        cmds.setParent('..')
        cmds.setParent('..')
        ###
        cmds.frameLayout( label='Blendshapes', collapsable=True, collapse=False)
        cmds.columnLayout( rowSpacing = 10 )

        cmds.text(label='Create duplicate curves for blendshapes?')

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
    
    def _createMouthCurv(self,_):
        upperCVs = cmds.ls(self.upperCurv+'.cv[*]',fl=True) #get list of CVs from lip curves
        lowerCVs = cmds.ls(self.lowerCurv+'.cv[*]',fl=True)
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
            
        #Do I have to return mouthCV data?
        
    def _createLipLocs(self,_):
        #specific(higher) functions has _
        upperLocs = ModFunc._createLocsOnCurve(self.upperCurv,self.upperVerts,self.lipUpperLocGrp)
        for loc in upperLocs: #loc[0] is the loc name, loc[1] is the X position of the loc
            cmds.reorder( loc[0], back=True )
            if upperLocs.index(loc)==( (len(upperLocs)-1)/2 ): #if the item is in the middle of the list
                name='upper_lip_loc'
            elif loc[1]<0:
                name='upper_lip_%02d_l_loc'%upperLocs.index(loc) #result: 'upper_lip_00_l_loc'
            elif loc[1]>0:
                name='upper_lip_%02d_r_loc'%( (len(upperLocs)-1)-(upperLocs.index(loc)) ) #result: 'upper_lip_00_r_loc'
            cmds.rename(loc[0],name) #Rename the locs in right order
            self.lipLocs.append(name) #append the loc name to self.lipLocs list
            
        lowerLocs = ModFunc._createLocsOnCurve(self.lowerCurv,self.lowerVerts,self.lipLowerLocGrp)
        for loc in lowerLocs:
            cmds.reorder( loc[0], back=True )
            if lowerLocs.index(loc)==( (len(lowerLocs)-1)/2 ):
                name='lower_lip_loc'
            elif loc[1]<0:
                name='lower_lip_%02d_l_loc'%lowerLocs.index(loc) #result: 'lower_lip_00_l_loc'
            elif loc[1]>0:
                name='lower_lip_%02d_r_loc'%( (len(lowerLocs)-1)-(lowerLocs.index(loc)) ) #result: 'lower_lip_00_r_loc'
            cmds.rename(loc[0],name)
            self.lipLocs.append(name) #append the loc name to self.lipLocs list
    
    def _aimConstMouthLocs(self,_):
        ModFunc._aimConstLocs(self.lipLocs, self.jawBind, self.faceLowerBind)
    
    def _createJntsOnMouthLocs(self,_):
        self.lipJnts = ModFunc._createJntsOnLocs(self.lipLocs,self.faceLowerBind)
        
    def _createMouthDrivers(self,_):
        ###change the code to put group name! ###put them in the class variable list! self.mouthDrivers??
        driverList = ModFunc._createJntsOnCVs(self.mouthCurv,self.mouthDriversGrp) 
        driverList = driverList[-1:] + driverList[:-1] #param 0 attachs to cv[1] for somehow, so I shifted last element to first position in list.

        
        if len(driverList)%4 != 0:
            print('Error: number of the drivers are not multiple of 4.')

        c = 0 #c is a counter for list index
        for driver in driverList:
            name = 'lip'
            if c == 0 or c==len(driverList)/2: #on the corner
                name += '_corner'
            elif c>0 and c<len(driverList)/2: 
                name += '_upper'
            elif c>len(driverList)/2:
                name += '_lower'
                
            if c != len(driverList)/4 and c != len(driverList)*3/4: #not in the middle        
                if c < len(driverList)/4 or c > len(driverList)*3/4: #on the right
                    name += '_r'
                else:
                    name += '_l'
                
                if '_corner' in name:
                    numUp = 0 #numUp is a counter for rename 
                    numDown = (len(driverList)-4)//4 -1 #numDown is a counter that goes reverse direction. It decreases from the maximum number
                else:
                    if '_upper_r' in name or 'lower_l' in name:
                        name += ('_%02d'%numUp)
                        numUp+=1
                    elif '_upper_l' in name or 'lower_r' in name:
                        name += ('_%02d'%numDown)
                        numDown-=1
                                  
            name += '_driver'
            cmds.rename(driver,name)
            self.mouthDrivers.append(name) #put the driver joint name to the list
            c+=1 #increase the counter
                            
    def _createBindmeshesOnMouthDrivers(self,_):
        self.mouthBindmeshes = ModFunc._createBindmeshesOnJnts(self.mouthDrivers,self.mouthBindmeshesGrp)
    
    def _createClsOnMouthBindmeshes(self,_):
        self.mouthCls = ModFunc._createClsOnBindmeshes(self.mouthBindmeshes,self.mouthClsGrp)
        
    def _createFolsOnMouthBindmeshes(self,_):
        self.mouthFols = ModFunc._createFolsOnBindmeshes(self.mouthBindmeshes,self.mouthFolGrp)
        
    def _createMouthCtrls(self,_):
        #micro ctrls
        self.lipMicroCtls = ModFunc._createCtrlGrp(self.mouthFols,self.lipMicroCtlGrp,offset=(0,0,1))
        
        for ctl in self.lipMicroCtls:
            ModFunc._overrideColor(ctl, color=(1,1,0))
            
        #macro ctrls
            
    def _attachLipMicroCtls(self,_):
        #Parent constraint the Controllers(nul group) to the follicles.
        #(Options:rotate and translate, maintain offset off. We do the offset manually with orient groups)
        #When the follicle moves with jaw movement, the controllers follow the follicle.
        #Then, animators can do macro & micro movement with those controllers.
        ModFunc._parentConstIterate(self.mouthFols,self.lipMicroCtls)
        
    def _attachMouthClsToJaw(self,_):
        for clus in self.mouthCls:
            cmds.parentConstraint(self.faceLowerBind,self.jawBind,clus,mo=True)
            constraint = clus + '_parentConstraint1'
            
            #should I hard coad weight values? maybe I could set up a set driven key
            W0 = 1 #Face Lower Bind W0
            if '_corner_' in clus:
                W0=.5
            elif '_upper_' in clus:
                W0=1
                if '_00_' in clus:
                    W0=.7
                elif '_01_' in clus:
                    W0=.9
            elif '_lower_' in clus:
                W0=0
                if '_00_' in clus:
                    W0=.3
                elif '_01_' in clus:
                    W0=.1
            W1 = 1-W0 #Jaw Bind W1
            
            cmds.setAttr(constraint+'.'+self.faceLowerBind+'W0', W0)
            cmds.setAttr(constraint+'.'+self.jawBind+'W1',W1)
            cmds.setAttr(constraint+'.interpType',2) #Interpolation Type: Shortest

            #cmds.select(self.jawBind) #temp
    
    def _createJawClsOnLipCurv(self,_):
        #WIP
        pass

    def _attachLipCtlsOnJawCls(self,_):
        ModFunc._parentConstIterate() #WIP
        pass
###-----------------------------------------------------EXECUTE---------------------------------------------------------------
letsgo=AutoRigMouth()