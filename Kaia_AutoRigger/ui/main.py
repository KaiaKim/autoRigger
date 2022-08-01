import maya.cmds as mc

###------------------------------------------Global Variables-------------------------------------------------
grey = (.3,.3,.3)
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
        if mc.window(self.winName, exists=True):
            mc.deleteUI(self.winName) #we don't want to create extra windows

        mc.window(self.winName, title=self.winTitle) #create a new window
        mc.scrollLayout( 'scorllLayout', width=330) #makes your entire layout scrollable #first - main layout
        mc.columnLayout( adjustableColumn=True ) #second layout - attaches to the main layout

        ###
        mc.frameLayout(l='Prepare', collapsable=True, collapse=False, mw=10, mh=5)
        mc.button(l='Import Face Skeleton',c=lambda x:mc.file(self.mayascripts+'/Kaia_AutoRigger/prepare/faceSkeleton.ma',i=True),bgc=blue)
        mc.setParent('..')
        ###
        mc.frameLayout(l='Data', collapsable=True, collapse=False, mw=10, mh=5)
        mc.button(l='Set character data directory',c=self.setDir ,bgc=orange)
        
        mc.rowLayout( numberOfColumns=2)
        mc.button(l='Import All Data', c=self.handler03, w=150, h=30, bgc=orange)
        mc.button(l='Export All Data', c=self.exportData, w=150, h=30, bgc=orange)
        mc.setParent('..')
        #
        mc.frameLayout( l='Geo', collapsable=True, collapse=False )
        mc.rowLayout(numberOfColumns=2,bgc=grey)
        
        mc.gridLayout(numberOfColumns=1, cellWidthHeight=(120,20))
        mc.text(l='Face')
        mc.text(l='Brow')
        mc.text(l='Lash')
        mc.text(l='Eye R')
        mc.text(l='Eye L')
        mc.text(l='Upper Teeth')
        mc.text(l='Lower Teeth')
        mc.text(l='tongue')
        mc.text(l='Extra')
        mc.setParent('..')
        
        mc.gridLayout(numberOfColumns=2, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        gBut01 = mc.button(l='assign', c=lambda _:self.assignGeo('face','ass'), bgc=blue)
        gBut02 = mc.button(l='select', c=lambda _:self.assignGeo('face','sel'), bgc=green)
        gBut03 = mc.button(l='assign', c=lambda _:self.assignGeo('brow','ass'), bgc=blue)
        gBut04 = mc.button(l='select', c=lambda _:self.assignGeo('brow','sel'), bgc=green)
        gBut05 = mc.button(l='assign', c=lambda _:self.assignGeo('lash','ass'), bgc=blue)
        gBut06 = mc.button(l='select', c=lambda _:self.assignGeo('lash','sel'), bgc=green)
        gBut07 = mc.button(l='assign', c=lambda _:self.assignGeo('eyeR','ass'), bgc=blue)
        gBut08 = mc.button(l='select', c=lambda _:self.assignGeo('eyeR','sel'), bgc=green)
        gBut09 = mc.button(l='assign', c=lambda _:self.assignGeo('eyeL','ass'), bgc=blue)
        gBut10 = mc.button(l='select', c=lambda _:self.assignGeo('eyeL','sel'), bgc=green)
        gBut11 = mc.button(l='assign', c=lambda _:self.assignGeo('upTeeth','ass'), bgc=blue)
        gBut12 = mc.button(l='select', c=lambda _:self.assignGeo('upTeeth','sel'), bgc=green)
        gBut13 = mc.button(l='assign', c=lambda _:self.assignGeo('loTeeth','ass'), bgc=blue)
        gBut14 = mc.button(l='select', c=lambda _:self.assignGeo('loTeeth','sel'), bgc=green)
        gBut15 = mc.button(l='assign', c=lambda _:self.assignGeo('tongue','ass'), bgc=blue)
        gBut16 = mc.button(l='select', c=lambda _:self.assignGeo('tongue','sel'), bgc=green)
        gBut17 = mc.button(l='assign', c=lambda _:self.assignGeo('extra','ass'), bgc=blue)
        gBut18 = mc.button(l='select', c=lambda _:self.assignGeo('extra','sel'), bgc=green)
        mc.setParent('..')
        
        mc.setParent('..')
        mc.setParent('..')
        #
        
        #
        mc.frameLayout(l='Vertices', collapsable=True, collapse=False)
        mc.rowLayout(numberOfColumns=2, bgc=grey)
        
        mc.gridLayout(numberOfColumns=1, cellWidthHeight=(120,20))
        mc.text(l='Upper Lip Verts')
        mc.text(l='Lower Lip Verts')
        mc.text(l='Upper R Eye Verts')
        mc.text(l='Lower R Eye Verts')
        mc.text(l='R Brow Vert')
        mc.setParent('..')
        
        mc.gridLayout( numberOfColumns=2, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        mc.button(l='assign', c=lambda _:self.handler01('lipUpper','ass'), bgc=blue)
        mc.button(l='select', c=lambda _:self.handler01('lipUpper','sel'), bgc=green)
        mc.button(l='assign', c=lambda _:self.handler01('lipLower','ass'), bgc=blue)
        mc.button(l='select', c=lambda _:self.handler01('lipLower','sel'), bgc=green)
        mc.button(l='assign', c=lambda _:self.handler01('lidUpperR','ass'), bgc=blue)
        mc.button(l='select', c=lambda _:self.handler01('lidUpperR','sel'), bgc=green)
        mc.button(l='assign', c=lambda _:self.handler01('lidLowerR','ass'), bgc=blue)
        mc.button(l='select', c=lambda _:self.handler01('lidLowerR','sel'), bgc=green)
        mc.button(l='assign', c=lambda _:self.handler01('browR','ass'), bgc=blue)
        mc.button(l='select', c=lambda _:self.handler01('browR','sel'), bgc=green)
        mc.setParent('..')
        
        mc.setParent('..')
        mc.setParent('..')
        #

        mc.setParent('..')
        
        ###
        self.frame01 = mc.frameLayout(l='Name', collapsable=True, collapse=False, mw=10, mh=5, enable=False)
        nBut01 = mc.button(l='1. Set Rig Names',c=self.handler02)
        mc.setParent('..')
        
        ###
        self.frame02 = mc.frameLayout(l='Build', collapsable=True, collapse=False, mw=10, mh=5, enable=False)
        but01 = mc.button(l='2. Build Rig', c=self.buildRig01)
        
        mc.columnLayout(bgc=grey, w=180)
        mc.checkBox(l='Build All')
        
        mc.frameLayout( l='Build Individual', collapsable=True, collapse=False )
        mc.gridLayout(numberOfColumns=3, cellWidthHeight=(90,20))
        mc.checkBox(l='Face')
        mc.checkBox(l='Mouth')
        mc.checkBox(l='Cheek')
        mc.checkBox(l='Teeth')
        mc.checkBox(l='Tongue')
        mc.checkBox(l='Lid')
        mc.checkBox(l='Eyes')
        mc.checkBox(l='Brows')
        mc.checkBox(l='Nose')
        mc.setParent('..')

        mc.setParent('..')
        mc.setParent('..')
        
        mc.setParent('..')
        
        ########
        mc.frameLayout(l='Helper', collapsable=True, collapse=True, w=220, mw=10, mh=5 )
        mc.columnLayout()
        hBut01 = mc.button(l='Mirror ctl orient R to L', c=self.mirrorCtlOrient, w=230)
        hBut03 = mc.button(l='mirror Mouth BS curve', c=self.mirrorBlendCrvMouth, w=230)
        hBut04 = mc.button(l='mirror Eyes BS curve', c=self.mirrorBlendCrvEyes, w=230)
        mc.setParent('..')
        mc.setParent('..')
        #########
        
        self.frame03 = mc.frameLayout(l='Bind', collapsable=True, collapse=False, mw=10, mh=5)
        but05 = mc.button(l='3. Bind Geo', c=self.bindGeo01)
        
        mc.columnLayout()
        ##
        mc.frameLayout(l='Bind Geo Manually', collapsable=True, collapse=True , w=220 )
        mc.rowLayout(numberOfColumns=2,bgc=grey)
        
        mc.gridLayout(numberOfColumns=1,cellWidthHeight=(120, 20))
        mc.text(l='Face Binds')
        mc.text(l='Brow Binds')
        mc.text(l='Lash Binds')
        mc.text(l='Eye R Binds')
        mc.text(l='Eye L Binds')
        mc.text(l='Upper Teeth Binds')
        mc.text(l='Lower Teeth Binds')
        mc.text(l='Tongue Binds')
        mc.text(l='Extra Binds')
        mc.setParent('..')
        mc.gridLayout( numberOfColumns=1, cellWidthHeight=(90, 20) ) #fourth layout - frame layout
        bBut01 = mc.button(l='+ select', c=lambda _:self.selectBinds('face','sel'))
        bBut02 = mc.button(l='+ select', c=lambda _:self.selectBinds('brow','sel'))
        bBut03 = mc.button(l='+ select', c=lambda _:self.selectBinds('lash','sel'))
        bBut04 = mc.button(l='+ select', c=lambda _:self.selectBinds('eyeR','sel'))
        bBut05 = mc.button(l='+ select', c=lambda _:self.selectBinds('eyeL','sel'))
        bBut06 = mc.button(l='+ select', c=lambda _:self.selectBinds('upTeeth','sel'))
        bBut07 = mc.button(l='+ select', c=lambda _:self.selectBinds('loTeeth','sel'))
        bBut08 = mc.button(l='+ select', c=lambda _:self.selectBinds('tongue','sel'))
        bBut09 = mc.button(l='+ select', c=lambda _:self.selectBinds('extra','sel'))
        mc.setParent('..')

        mc.setParent('..')
        mc.setParent('..')
        ##
        mc.setParent('..')
        mc.setParent('..')


        mc.showWindow()
        
        self.blueButs01 = [gBut01,gBut03,gBut05,gBut07,gBut09,gBut11,gBut13,gBut15,gBut17]
        self.blueButs01 = [nBut01]
        self.blueButs02 = [but01,but05]
        self.redButs01 = []
        self.greenButs01 = [hBut01,hBut03,hBut04, bBut01,bBut02,bBut03,bBut04,bBut05,bBut06,bBut07,bBut08,bBut09]
    

###---------------------------------------------------------------------------
