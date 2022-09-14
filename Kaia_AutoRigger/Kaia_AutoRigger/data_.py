import maya.cmds as mc
import importlib
import json

from Kaia_AutoRigger.modules import getset
from Kaia_AutoRigger.modules import util

importlib.reload(getset)
importlib.reload(util)
###-----------------------------------------------------CLASS---------------------------------------------------
class ImportExport():
    def setDir(self,_):
        #get file path
        self.dir = mc.fileDialog2(
            fileFilter="*.json", dialogStyle=1, fm=3, caption='Set character data directory'
            )[0]

    def getOrientsData(self):
        #get ctrl orient data
        orients = [d+'_orient' for d in self.allCtls]
        self.data['orients'] = getset.getTransform(orients, t=False, r=True)
    
    def getBsCrvData(self):
        #get blendshape crv data
        allCVs = []
        for i in self.allCrv:
            CVs = getset.getCVs(i)
            allCVs += CVs
        self.data['bsCrv'] = getset.getTransform(allCVs, t=True, r=False, os=True)

    def importData(self):
        if self.dir == None:
            print('please set directory first')
            return
        
        #read json files
        with open(self.dir + '/geoNames.json', "r") as rfile:
            self.data['geo'] = json.load(rfile)
        with open(self.dir + '/vertIndices.json', "r") as rfile:
            self.data['verts'] = json.load(rfile)
        with open(self.dir + '/ctlOrient.json', "r") as rfile:
            self.data['orients'] = json.load(rfile)
        with open(self.dir + '/blendshapeCrv.json', "r") as rfile:
            self.data['bsCrv'] = json.load(rfile)
    
    def exportData(self,_):
        if self.dir == None:
            print('please set directory first')
            return

        #write json files
        with open(self.dir+'/geoNames.json', "w") as wfile:
            json.dump(self.data['geo'], wfile)
        with open(self.dir+'/vertIndices.json',"w") as wfile:
            json.dump(self.data['verts'], wfile)
        with open(self.dir+'/ctlOrient.json',"w") as wfile:
            json.dump(self.data['orients'], wfile)
        with open(self.dir+'/blendshapeCrv.json',"w") as wfile:
            json.dump(self.data['bsCrv'], wfile)
    
    def assignGeo(self,x,flag):
        if flag=='ass':
            self.data['geo'][x]=mc.ls(sl=True)
        if flag=='sel':
            mc.select(self.data['geo'][x])
        
    def assignVerts(self,x,flag):
        if flag=='ass':
            self.data['verts'][x]=mc.ls(sl=True,fl=True)
        elif flag=='sel':
            mc.select(self.data['verts'][x])
    