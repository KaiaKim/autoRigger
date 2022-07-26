import maya.cmds as mc
import importlib

from Kaia_AutoRigger.modules import util
from Kaia_AutoRigger.modules import getset

importlib.reload(util)
importlib.reload(getset)

class BindGeo():
    def __init__(self):
        pass
    
    def bindGeo01(self,_):
        for geoKey,geos in self.data['geo'].items():
            for jntKey,jnts in self.bindSets.items():
                
                if jntKey in ['eyeR','eyeL','extra']: x=1
                else: x=4
                
                if geoKey==jntKey:
                    util.bindSkin(jnts,geos,mi=x)
                
    def selectGeo(self,x):
        mc.select(self.data['geo'][x])
            
    def selectBinds(self,x,_):
        for bind in self.bindSets[x]:
            try: mc.select(bind, add=True)
            except: print(bind,'doesn\'t exist. Select skipped')