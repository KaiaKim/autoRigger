import maya.cmds as cmds
from functools import partial

###------------------------------------------Global Variables-------------------------------------------------
grey = (.4,.4,.4)
red = (.9,.65,.65)
orange = (1,.8,.6)
yellow = (1,1,.8)
green = (.6,.8,.6)
blue = (.5,.7,.8)


###---------------------------------------------Function------------------------------------------------------
class createUI():
    def __init__(self):
        pass
        
    def createWindow(self):
        #test to see if the window exists
        if cmds.window(self.winName, exists=True):
            cmds.deleteUI(self.winName) #we don't want to create extra windows

        cmds.window(self.winName, title=self.winTitle) #create a new window
        cmds.scrollLayout( 'scorllLayout', width=330) #makes your entire layout scrollable #first - main layout
        cmds.columnLayout( adjustableColumn=True ) #second layout - attaches to the main layout

        ###
        cmds.frameLayout( l='Prepare', collapsable=True, collapse=False , mw=10, mh=5)
        cmds.button( l='Import Face Skeleton',c=lambda x:cmds.file(self.mayascripts+'/Kaia_AutoRigger/templateFiles/faceBindJoints.ma',i=True),bgc=blue)
        cmds.setParent('..')
        ###
        cmds.frameLayout( l='Data', collapsable=True, collapse=False, mw=10, mh=5 )
        cmds.button(l='Set character data directory',c=self.setDir ,bgc=orange)
        
        cmds.rowLayout( numberOfColumns=2)
        cmds.button( l='Import All Data', c=self.handler03,w=150,h=30,bgc=orange)
        cmds.button( l='Export All Data', c=self.exportData,w=150,h=30,bgc=orange)
        cmds.setParent('..')
        '''
        cmds.columnLayout(rs=5)
        cmds.checkBox(l='All Data',cc=lambda _:print('good'),v=True,enable=True)
        cmds.rowColumnLayout(numberOfColumns=2)
        cmds.checkBox( l='Geo Names',v=True,enable=False)
        cmds.checkBox( l='Vertex indices',v=True,enable=False)
        cmds.checkBox( l='Ctrl Orient',v=True,enable=False)
        cmds.checkBox( l='Blend Shape Curves',v=True,enable=False)
        cmds.checkBox( l='Custom Attribute',v=True,enable=False)
        cmds.checkBox( l='PSDBS',v=True,enable=False)
        cmds.setParent('..')
        cmds.setParent('..')
        '''
        #
        cmds.frameLayout( l='Geo', collapsable=True, collapse=False )
        cmds.rowLayout(numberOfColumns=2,bgc=grey)
        
        cmds.gridLayout(numberOfColumns=1,cellWidthHeight=(120, 20))
        cmds.text(l='Face')
        cmds.text( l='Brow')
        cmds.text( l='Lash')
        cmds.text( l='Eye R')
        cmds.text( l='Eye L')
        cmds.text( l='Upper Teeth')
        cmds.text( l='Lower Teeth')
        cmds.text( l='tongue')
        cmds.text( l='Extra')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        gBut01 = cmds.button( l='assign', c=lambda _:self.assignGeo('face','ass'),bgc=blue )
        gBut02 = cmds.button( l='select', c=lambda _:self.assignGeo('face','sel'),bgc=green )
        gBut03 = cmds.button( l='assign', c=lambda _:self.assignGeo('brow','ass'),bgc=blue )
        gBut04 = cmds.button( l='select', c=lambda _:self.assignGeo('brow','sel'),bgc=green )
        gBut05 = cmds.button( l='assign', c=lambda _:self.assignGeo('lash','ass'),bgc=blue )
        gBut06 = cmds.button( l='select', c=lambda _:self.assignGeo('lash','sel'),bgc=green )
        gBut07 = cmds.button( l='assign', c=lambda _:self.assignGeo('eyeR','ass'),bgc=blue )
        gBut08 = cmds.button( l='select', c=lambda _:self.assignGeo('eyeR','sel'),bgc=green )
        gBut09 = cmds.button( l='assign', c=lambda _:self.assignGeo('eyeL','ass'),bgc=blue )
        gBut10 = cmds.button( l='select', c=lambda _:self.assignGeo('eyeL','sel'),bgc=green )
        gBut11 = cmds.button( l='assign', c=lambda _:self.assignGeo('upTeeth','ass'),bgc=blue )
        gBut12 = cmds.button( l='select', c=lambda _:self.assignGeo('upTeeth','sel'),bgc=green )
        gBut13 = cmds.button( l='assign', c=lambda _:self.assignGeo('loTeeth','ass'),bgc=blue )
        gBut14 = cmds.button( l='select', c=lambda _:self.assignGeo('loTeeth','sel'),bgc=green )
        gBut15 = cmds.button( l='assign', c=lambda _:self.assignGeo('tongue','ass'),bgc=blue )
        gBut16 = cmds.button( l='select', c=lambda _:self.assignGeo('tongue','sel'),bgc=green )
        gBut17 = cmds.button( l='assign', c=lambda _:self.assignGeo('extra','ass'),bgc=blue )
        gBut18 = cmds.button( l='select', c=lambda _:self.assignGeo('extra','sel'),bgc=green )
        cmds.setParent('..')
        
        cmds.setParent('..')
        cmds.setParent('..')
        #
        
        #
        cmds.frameLayout( l='Vertices', collapsable=True, collapse=False )
        cmds.rowLayout(numberOfColumns=2,bgc=grey)
        
        cmds.gridLayout(numberOfColumns=1,cellWidthHeight=(120, 20))
        cmds.text( l='Upper Lip Verts')
        cmds.text( l='Lower Lip Verts')
        cmds.text( l='Upper R Eye Verts')
        cmds.text( l='Lower R Eye Verts')
        cmds.text( l='R Brow Vert')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        cmds.button( l='assign', c=lambda _:self.handler01('lipUpper','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.handler01('lipUpper','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.handler01('lipLower','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.handler01('lipLower','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.handler01('lidUpperR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.handler01('lidUpperR','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.handler01('lidLowerR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.handler01('lidLowerR','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.handler01('browR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.handler01('browR','sel'),bgc=green )
        cmds.setParent('..')
        
        cmds.setParent('..')
        cmds.setParent('..')
        #

        cmds.setParent('..')
        
        ###
        self.frame01 = cmds.frameLayout( l='Name', collapsable=True, collapse=False, mw=10, mh=5, enable=False)
        nBut01 = cmds.button(l='0. Set Rig Names',c=self.handler02)
        cmds.setParent('..')
        
        ###
        self.frame02 = cmds.frameLayout( l='Build', collapsable=True, collapse=False, mw=10, mh=5, enable=False)
        cmds.columnLayout()
        #1
        cmds.columnLayout()
        cmds.rowLayout(numberOfColumns=2)
        but01 = cmds.button(l='1. Build Ctls',c=self.buildRig01,w=250,h=30)
        but02 = cmds.button(l='Revert',w=50,h=30)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2)
        but03 = cmds.button(l='2. Connect Ctls',c=self.buildRig02,w=250,h=30)
        but04 = cmds.button(l='Revert',w=50,h=30)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2)
        but05 = cmds.button(l='3. Bind Geo',c=self.buildRig03,w=250,h=30)
        but06 = cmds.button(l='Revert',c=self.deleteRig03,w=50,h=30)
        cmds.setParent('..')
        cmds.setParent('..')
        
        #2
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(l='Helper: ')
        cmds.columnLayout()
        hBut01 = cmds.button( l='Mirror ctl orient R to L', c=lambda _:self.orientData('mirror'),w=230)
        hBut02 = cmds.button(l='Normalize ctl',w=230)
        hBut03 = cmds.button( l='mirror Mouth BS curve', c=self.mirrorBlendCrvMouth,w=230)
        hBut04 = cmds.button( l='mirror Eyes BS curve', c=self.mirrorBlendCrvEyes,w=230)
        cmds.setParent('..')
        cmds.setParent('..')
        
        #3
        cmds.frameLayout( l='Bind Geo Manually', collapsable=True, collapse=True , w=220 )
        cmds.rowLayout(numberOfColumns=2,bgc=grey)
        
        cmds.gridLayout(numberOfColumns=1,cellWidthHeight=(120, 20))
        cmds.text(l='Face Binds')
        cmds.text( l='Brow Binds')
        cmds.text( l='Lash Binds')
        cmds.text( l='Eye R Binds')
        cmds.text( l='Eye L Binds')
        cmds.text( l='Upper Teeth Binds')
        cmds.text( l='Lower Teeth Binds')
        cmds.text( l='Tongue Binds')
        cmds.text( l='Extra Binds')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=1, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        bBut01 = cmds.button( l='+ select', c=lambda _:self.selectBinds('face','sel') )
        bBut02 = cmds.button( l='+ select', c=lambda _:self.selectBinds('brow','sel') )
        bBut03 = cmds.button( l='+ select', c=lambda _:self.selectBinds('lash','sel') )
        bBut04 = cmds.button( l='+ select', c=lambda _:self.selectBinds('eyeR','sel') )
        bBut05 = cmds.button( l='+ select', c=lambda _:self.selectBinds('eyeL','sel') )
        bBut06 = cmds.button( l='+ select', c=lambda _:self.selectBinds('upTeeth','sel') )
        bBut07 = cmds.button( l='+ select', c=lambda _:self.selectBinds('loTeeth','sel') )
        bBut08 = cmds.button( l='+ select', c=lambda _:self.selectBinds('tongue','sel') )
        bBut09 = cmds.button( l='+ select', c=lambda _:self.selectBinds('extra','sel') )
        cmds.setParent('..')
        
        
        cmds.setParent('..')
        cmds.setParent('..')
        #
        cmds.setParent('..')
        cmds.setParent('..')
        
        cmds.frameLayout( l='Danger Zone', collapsable=True, collapse=True, mw=10, mh=5)
        #3
        cmds.button(l='Delete Rig',w=300,bgc=red)
        
        cmds.setParent('..')

        cmds.showWindow()
        
        self.blueButs01 = [gBut01,gBut03,gBut05,gBut07,gBut09,gBut11,gBut13,gBut15,gBut17]
        self.blueButs01 = [nBut01]
        self.blueButs02 = [but01,but03,but05]
        self.redButs01 = [but02,but04,but06]
        self.greenButs01 = [hBut01,hBut02,hBut03,hBut04, bBut01,bBut02,bBut03,bBut04,bBut05,bBut06,bBut07,bBut08,bBut09]
    
    def handler01(self,x,flag,_):
        self.assignVerts(x,flag)
        
        checker=True
        for val in self.data['verts'].items():
            if val==None: checker=False
        cmds.frameLayout(self.frame01,e=True,enable=checker)
        for but in self.blueButs01:
            cmds.button(but,e=True,bgc=blue)
        
    def handler02(self,_):
        self.names()
        cmds.frameLayout(self.frame02,e=True,enable=True)
        for but in self.blueButs02:
            cmds.button(but,e=True,bgc=blue)
        for but in self.redButs01:
            cmds.button(but,e=True,bgc=red)
        for but in self.greenButs01:
            cmds.button(but,e=True,bgc=green)
    
    def handler03(self,_):
        self.importData()
        
        checker=True
        for val in self.data['verts'].items():
            if val==None: checker=False
        cmds.frameLayout(self.frame01,e=True,enable=checker)
        for but in self.blueButs01:
            cmds.button(but,e=True,bgc=blue)
###---------------------------------------------------------------------------
