import maya.cmds as mc
import importlib

from Kaia_AutoRigger.modules import util
importlib.reload(util)
###------------------------------CLASS---------------------------------
class stretchyIKMaker():
    def __init__(self, obj, section=2, degree=3):
        self.chain = obj.binds
        self.start = obj.binds[0]
        self.end = obj.binds[-1]
        self.span = section + 1
        self.degree = degree
        
        self.crv = obj.crv
        self.ikHand = obj.ikHand
        self.ikEff = obj.ikEff
        
        self.upObj = obj.upObj
        
        self.clsGrp = obj.clsGrp
        self.clsNodes = obj.clsNodes
        self.clsHandles = obj.clsHandles
        
        self.FKCtls = obj.fkCtls
        self.IKCtls = obj.ikCtls
        
        ###
        self.createCrv()
        self.rebuildCrv()
        self.createIKHandle()
        self.clsOnCrv()
        self.ctlOnCls()
        self.connectCtl()
        self.ikTwist()

    
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

        targs = (
            [CVs[0:2]]
            +[c for c in CVs[2:-2]]
            +[[CVs[-2],CVs[-1]]]
        )

        for targ, clus in zip(targs, self.clsNodes):
            mc.cluster(targ, n=clus, rel=True)

        
        mc.group(self.clsHandles,n=self.clsGrp)
    
    def ctlOnCls(self):
        
        util.createCtlGrp(self.clsHandles, self.IKCtls, None, shape='square', size=1)
        util.createCtlGrp(self.clsHandles, self.FKCtls, None, shape='circle', size=.7)
        util.offsetCtls(self.IKCtls+self.FKCtls, r=(0,90,0), s=(1.5,1.5,2))
        
        FKNul=[d+'_nul' for d in self.FKCtls]
        IKNul=[d+'_nul' for d in self.IKCtls]
        
        util.parentIterate(self.FKCtls, IKNul)

        for i,nul in enumerate(FKNul):
            ori = mc.orientConstraint(self.start,self.end,nul,mo=False)[0]
            val = i /(len(FKNul)-1)
            mc.setAttr( '%s.%sW0'%(ori,self.start), 1-val )
            mc.setAttr( '%s.%sW1'%(ori,self.end), val )
            mc.delete(ori)

        
        for i in range(len(FKNul)-1):
            mc.parent(FKNul[i+1], self.FKCtls[i])

        
    def connectCtl(self):
        util.parentConstIterate(self.IKCtls, self.clsHandles)
        
    def ikTwist(self):
        mc.spaceLocator(n=self.upObj)
        mc.parent(self.upObj,self.FKCtls[0]+'_orient', r=True)
        mc.move(0,100,0,'tongue_upObj', ls=True)
        mc.hide(self.upObj)
        
        mc.setAttr(self.ikHand+'.dTwistControlEnable', 1)
        mc.setAttr(self.ikHand+'.dWorldUpType', 1)
        mc.connectAttr(self.upObj+'.worldMatrix', self.ikHand+'.dWorldUpMatrix')


###------------------------------EXECUTE---------------------------------
if __name__ == "__main__":
    sel=mc.ls(sl=True)
    run01=stretchyIKMaker(sel,section=2,prefix='tongue_',degree=3,softCorner=True)
