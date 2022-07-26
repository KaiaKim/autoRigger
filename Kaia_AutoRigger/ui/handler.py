import maya.cmds as mc

###------------------------------------------Global Variables-------------------------------------------------
grey = (.3,.3,.3)
red = (.9,.65,.65)
orange = (1,.8,.6)
yellow = (1,1,.8)
green = (.6,.8,.6)
blue = (.5,.7,.8)

###---------------------------------------------Function------------------------------------------------------
class ButtonHandler():
    def __init__(self):
        pass

    def handler01(self,x,flag,_):
        self.assignVerts(x,flag)
        
        checker=True
        for val in self.data['verts'].items():
            if val==None: checker=False
        mc.frameLayout(self.frame01,e=True,enable=checker)
        for but in self.blueButs01:
            mc.button(but,e=True,bgc=blue)
        
    def handler02(self,_):
        self.names()
        mc.frameLayout(self.frame02,e=True,enable=True)
        for but in self.blueButs02:
            mc.button(but,e=True,bgc=blue)
        for but in self.redButs01:
            mc.button(but,e=True,bgc=red)
        for but in self.greenButs01:
            mc.button(but,e=True,bgc=green)
    
    def handler03(self,_):
        self.importData()
        
        checker=True
        for val in self.data['verts'].items():
            if val==None: checker=False
        mc.frameLayout(self.frame01,e=True,enable=checker)
        for but in self.blueButs01:
            mc.button(but,e=True,bgc=blue)