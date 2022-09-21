import maya.cmds as mc
import importlib
from Kaia_AutoRigger.modules import getset
importlib.reload(getset)

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

    def handler01(self,x,flag):
        self.assignVerts(x,flag)
        
        checker=True
        for val in self.data['verts'].items():
            if val==None: checker=False
        mc.frameLayout(self.frame01,e=True,enable=checker)
        for but in self.blueButs01:
            mc.button(but,e=True,bgc=blue)
    
    def setDirHandler(self,_):
        self.setDir()

        mc.button(self.importBut, e=True, enable=True, bgc=orange)
        


    def setNamesHandler(self,_):
        missingVerts = []
        
        for key in self.data['verts'].keys():
            if self.data['verts'][key] == None:
                missingVerts.append(key)
                
        if missingVerts != []:
            mc.warning(', '.join([x for x in missingVerts])+'Verts are not assigned!')
            
        elif missingVerts == []:
            self.setNames()

            mc.frameLayout(self.frame02, e=True, enable=True)
            mc.frameLayout(self.frame03, e=True, enable=True)
            
            mc.button(self.exportBut, e=True, enable=True, bgc=orange)
            
            for b in self.blueButs02:
                mc.button(b,e=True, bgc=blue)
            for b in self.redButs01:
                mc.button(b,e=True, bgc=red)
            for b in self.greenButs01:
                mc.button(b,e=True, bgc=green)
    
    
    def handler03(self,_):
        self.createDefaultData()
        self.importData()
        
        checker = True
        for val in self.data['verts'].items():
            if val == None: checker=False
        mc.frameLayout(self.frame01, e=True, enable=checker)
        for but in self.blueButs01:
            mc.button(but, e=True, bgc=blue)


    def handler04(self,_):
        self.getOrientsData()
        self.getBsCrvData()
        self.exportData()


    def buildRig(self,_):
        ###duplicate out the guide

        self.createGrps()
        self.face01()
        self.mouth01()
        self.teethTongue01()
        self.lid01()
        #self.eye01()
        self.brow01()
        self.nose01()
        
        self.face02()
        self.mouth02()
        self.teethTongue02()
        self.lid02()
        #self.eye02()
        self.brow02()
        self.nose02()

        self.arrangeGrps()
        self.colorCtls()

        if self.data['orients'] != []:
            getset.applyTransform(self.data['orients'])
        if self.data['bsCrv'] != []:
            getset.applyTransform(self.data['bsCrv'], os=True)
