import maya.cmds as cmds
from functools import partial

###------------------------------------------Global Variables-------------------------------------------------



###---------------------------------------------Function------------------------------------------------------
class createUI():
    def __init__(self):
        pass
        
    def createWindow(self):
        grey = (.4,.4,.4)
        red = (.9,.65,.65)
        orange = (1,.8,.6)
        yellow = (1,1,.8)
        green = (.6,.8,.6)
        blue = (.5,.7,.8)
        
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
        
        cmds.rowLayout( numberOfColumns=2)
        cmds.button( l='Import Data', c=self.importData,w=150,h=30,bgc=green)
        cmds.button( l='Export Data', c=self.exportData,w=150,h=30,bgc=green)
        cmds.setParent('..')
        
        #
        cmds.frameLayout( l='Geo', collapsable=True, collapse=False )
        cmds.rowLayout(numberOfColumns=2,bgc=grey)
        
        cmds.gridLayout(numberOfColumns=1,cellWidthHeight=(120, 20))
        cmds.text(l='Head')
        cmds.text( l='Brows')
        cmds.text( l='Lashes')
        cmds.text( l='Eye R')
        cmds.text( l='Eye L')
        cmds.text( l='Upper Teeth')
        cmds.text( l='Lower Teeth')
        cmds.text( l='Toungue')
        cmds.text( l='Extra')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        cmds.button( l='assign', c=lambda _:self.assignGeo('head','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('head','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('brows','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('brows','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('lashes','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('lashes','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('eyeR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('eyeR','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('eyeL','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('eyeL','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('upTeeth','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('upTeeth','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('loTeeth','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('loTeeth','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('toungue','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('toungue','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignGeo('extra','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignGeo('extra','sel'),bgc=green )
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
        cmds.button( l='assign', c=lambda _:self.assignVerts('lipUpper','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignVerts('lipUpper','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignVerts('lipLower','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignVerts('lipLower','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignVerts('lidUpperR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignVerts('lidUpperR','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignVerts('lidLowerR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignVerts('lidLowerR','sel'),bgc=green )
        cmds.button( l='assign', c=lambda _:self.assignVerts('browR','ass'),bgc=blue )
        cmds.button( l='select', c=lambda _:self.assignVerts('browR','sel'),bgc=green )
        cmds.setParent('..')
        
        cmds.setParent('..')
        cmds.setParent('..')
        #
        
        cmds.rowLayout(numberOfColumns=2)
        
        cmds.gridLayout(numberOfColumns=1,cellWidthHeight=(120, 20))
        cmds.text( l='Ctrl Orient: ')
        cmds.text( l='BlendShape Curves: ')
        cmds.text( l='Custom Attribute: ')
        cmds.setParent('..')
        
        cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        cmds.button( l='store', c=lambda _:self.orientData('save'),bgc=green)
        cmds.button( l='apply', c=lambda _:self.orientData('load'),bgc=green)
        cmds.button( l='store', c=lambda _:self.blendCrvData('save'),bgc=green)
        cmds.button( l='apply', c=lambda _:self.blendCrvData('load'),bgc=green)
        cmds.button( l='store', c=lambda _:self.attrData('save'),bgc=green)
        cmds.button( l='apply', c=lambda _:self.attrData('load'),bgc=green)
        
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')
        
        ###
        cmds.frameLayout( l='Name', collapsable=True, collapse=False, mw=10, mh=5)
        cmds.button(l='0. Set Rig Names',c=self.names,bgc=blue)
        cmds.setParent('..')
        
        ###
        cmds.frameLayout( l='Build', collapsable=True, collapse=False, mw=10, mh=5)
        cmds.columnLayout()
        #1
        cmds.columnLayout()
        cmds.rowLayout(numberOfColumns=2)
        buildBut1 = cmds.button(l='1. Build Ctls',c=self.buildRig01,w=250,h=30,bgc=blue)
        revertBut1 = cmds.button(l='Revert',w=50,h=30,bgc=red)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2)
        buildBut2 = cmds.button(l='2. Connect Ctls',c=self.buildRig02,w=250,h=30,bgc=blue)
        revertBut2 = cmds.button(l='Revert',w=50,h=30,bgc=red)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2)
        buildBut3 = cmds.button(l='3. Bind Geo',c=self.buildRig03,w=250,h=30,bgc=blue)
        revertBut3 = cmds.button(l='Revert',c=self.deleteRig03,w=50,h=30,bgc=red)
        cmds.setParent('..')
        cmds.setParent('..')

        #2
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(l='Helper: ')
        cmds.columnLayout()
        cmds.button( l='Mirror ctl orient R to L', c=lambda _:self.orientData('mirror'),w=230,bgc=green)
        cmds.button(l='Normalize ctl',w=230,bgc=green)
        cmds.button( l='mirror Mouth BS curve', c=self.mirrorBlendCrvMouth,w=230,bgc=green)
        cmds.button( l='mirror Eyes BS curve', c=self.mirrorBlendCrvEyes,w=230,bgc=green)
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
        cmds.button( l='+ select', c=lambda _:self.selectBinds('face','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('brow','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('lash','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('eyeR','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('eyeL','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('upTeeth','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('loTeeth','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('tongue','sel'),bgc=green )
        cmds.button( l='+ select', c=lambda _:self.selectBinds('extra','sel'),bgc=green )
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
        
###---------------------------------------------------------------------------
