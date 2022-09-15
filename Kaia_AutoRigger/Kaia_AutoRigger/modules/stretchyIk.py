import maya.cmds as mc
import importlib

from Kaia_AutoRigger.modules import util
importlib.reload(util)
###------------------------------CLASS---------------------------------
class stretchyIKMaker():
    def __init__(self, object, section=1, degree=3):
        self.chain = object.binds
        self.start = object.binds[0]
        self.end = object.binds[-1]
        self.span = section + 1
        self.degree = degree
        
        self.crv = 
        self.ikHand = 
        self.ikEff = 
        
        self.clsGrp = 
        self.clsNodes = 
        self.clsHandles = 
        
        self.ctlGrp = 
        self.FKCtls = 
        self.IKCtls = 
        
        ###
        self.createCrv()
        self.rebuildCrv()
        self.createIKHandle()
        self.clsOnCrv()
        self.ctlOnCls()
        self.connectCtl()

    
    def createCrv(self):
        posList = []
        for i in self.chain:
            pos= mc.xform(i, q=True, ws=True, t=True)
            posList.append(pos)
            
        mc.curve(p=posList, n=self.crv, d=self.degree)
    
    def rebuildCrv(self):
        mc.rebuildCurve(self.crv, ch=0, rpo=1, rt=0, end=1,
                        kr=2, kcp=0, kep=0, kt=0,
                        s=self.span, d=3, tol=0.01
                        )
                        
    def createIKHandle(self):
        ikNode = mc.ikHandle(sj=self.start, ee=self.end, c=self.crv, ccv=False,
                    sol='ikSplineSolver', s='sticky', 
                    )
        mc.rename(ikNode[0],self.ikHand)
        mc.rename(ikNode[1],self.ikEff)
        
    def clsOnCrv(self):
        CVs = mc.ls(self.crv + '.cv[*]', fl=1)

        clsTarget = [CVs[0:2]] + [c for c in CVs[2:-2]] + [CVs[-2],CVs[-1]]
    
        for cv, clus in zip(clsTarget, self.clsNodes):
            mc.cluster(cv, n=clus, rel=True)

        
        mc.group(self.clsHandles,n=self.clsGrp)
    
    def ctlOnCls(self):
        
        util.createCtlGrp(self.IKCtls, self.clsHandles, shape='square', size=8)
        util.createCtlGrp(self.FKCtls, self.clsHandles, shape='circle', size=4)
        
        util.overrideColor(self.IKCtls, color='yellow')
        util.overrideColor(self.FKCtls, color='magenta')
        
        FKNul=[d+'_nul' for d in self.FKCtls]
        util.parentIterate(self.IKCtls, FKNul)
        
        IKNul=[d+'_nul' for d in self.IKCtls]

        for i,nul in enumerate(IKNul):
            print(nul)
            ori = mc.orientConstraint(self.start,self.end,nul,mo=False)[0]
            val = i /(len(IKNul)-1)
            mc.setAttr( '%s.%sW0'%(ori,self.start), 1-val )
            mc.setAttr( '%s.%sW1'%(ori,self.end), val )
            mc.delete(ori)

        
        for i in range(len(IKNul)-1):
            mc.parent(IKNul[i+1], self.IKCtls[i])

        
    def connectCtl(self):
        util.parentConstIterate(self.FKCtls, self.clsHandles)


###------------------------------EXECUTE---------------------------------
if __name__ == "__main__":
    sel=mc.ls(sl=True)
    run01=stretchyIKMaker(sel,section=2,prefix='tongue_',degree=3,softCorner=True)

