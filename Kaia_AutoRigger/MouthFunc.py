import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
from Kaia_AutoRigger import DataFunc
importlib.reload(ModFunc)
importlib.reload(DataFunc)

def _createMouthCrv(name, upperCrv, lowerCrv):
    upperCVs = ModFunc._getCVs(upperCrv)
    lowerCVs = ModFunc._getCVs(lowerCrv)
    lowerCVs.reverse() #reverse list order so that it comes back to the start, as a circle

    cvList = upperCVs + lowerCVs

    sectionCount = 11
    mouthCrv = cmds.circle(n=name, s=sectionCount, d=1)[0] #create a new curve #cv 0~12
    cmds.delete(mouthCrv,constructionHistory=True)

    counter = 0 #this is a counter
    for i in range(12): #We're going to iterate through mouth curv(CVs)
        pos=cmds.xform(cvList[counter], q=True, t=True, ws=True) #get world position from the CV
        if counter==6: #there's two cvs overlapping on the corner. 6 is the right corner CV.
            counter+=1 #We skip the overlapping cv by adding 1 to the counter
               
        mouthCV = mouthCrv + '.cv[%d]'%i #get mouth CV
        cmds.move(pos[0],pos[1],pos[2],mouthCV) #snap mouth CV to the position

        counter+=1 #increase counter



def _2CurvCvCls(names,ctls,upCurv,loCurv):
    #can use this for lip_upper_curve & lip_lower_curve, or eye_upper_curve & eye_lower_curve
    clsList = []
    
    upCurvShape = ModFunc._getCrvShape(upCurv)
    loCurvShape = ModFunc._getCrvShape(loCurv)
    
    upCVs = ModFunc._getCVs(upCurv)
    loCVs = ModFunc._getCVs(loCurv)
    leftCorner = (upCVs.pop(0) , loCVs.pop(0))
    rightCorner = (upCVs.pop(-1), loCVs.pop(-1))
    
    loCVs.reverse()

    cvList = [leftCorner]+upCVs+[rightCorner]+loCVs
    
    for cv,name,ctl in zip(cvList,names,ctls):
        clus = cmds.cluster(cv)
        clsTrans = clus[1]
        clsTrans = cmds.rename(clsTrans, name)
        
        offGrp = cmds.group(clsTrans,n=name+'_offset')
        cmds.parent(offGrp, ctl) #(child, parent)


def constMicroToMacro(inList):
    for i in inList:
        if '_m_' in i:
            nul2 = cmds.group(i+'_orient',n=i+'_nul2') #create nul2 grp
            macro = i.replace('lip','mouth') #micro_mouth_lower_m_ctl
            cmds.parentConstraint(macro,nul2,mo=True)
            

def _createClsOnEach(names,bindmeshes):
    for bindmesh,name in zip(bindmeshes,names):
        clus = cmds.cluster(bindmesh)
        clsTrans = clus[1]
        clsTrans = cmds.rename(clsTrans, name)
        
def _createClsOnAll(name, bindmeshes, weights=[]):
    clus = cmds.cluster(bindmeshes)
    clsTrans = clus[1]
    clsTrans = cmds.rename(clsTrans, name)
    
    if weights != []:
        for bm,val in zip(bindmeshes,weights):
            cmds.select(bm+'.vtx[*]') #select vertex
            cmds.percent( name+'Cluster', v=val ) # set percents on the selected items to each value
        
def constWithDriver(name,ctl,clus,grp):
    #create driver
    cmds.spaceLocator(n=name)
    #create driver nul
    cmds.group(name,n=name+'_nul')
    #match jaw ctl
    cmds.parent(name+'_nul',ctl,r=True) #or jaw ctl
    #parent to anim grp
    cmds.parent(name+'_nul',grp)
    #connect translate, rotate
    cmds.connectAttr(ctl+'.t',name+'.t')
    cmds.connectAttr(ctl+'.r',name+'.r')
    
    cmds.parentConstraint(name,clus,mo=True)
    

def attachCorner(ctl,clus,P1,P2,P3):
    ###parent const clus to p1,p2
    clsConst = cmds.parentConstraint(P1, P2, clus,mo=True)[0]
    cmds.setAttr(clsConst+'.interpType',2)
    ###parent const nul to p1,p2
    const1 = cmds.parentConstraint(P1,P2,ctl+'_nul',mo=True)[0]
    cmds.setAttr(const1+'.interpType',2) #Interpolation Type: Shortest
    ###parent const nul2 to p3
    const2 = cmds.parentConstraint(P3,ctl+'_nul2',mo=True)[0]
     ##break connection: constraint parent inverse matrix
    cmds.disconnectAttr(ctl+'_nul2'+'.parentInverseMatrix',const2+'.constraintParentInverseMatrix')
    cmds.setAttr(const2+'.interpType',2)

    #set range node
    setRanNode = cmds.createNode('setRange')
    #cornerPin >> valueX
    cmds.connectAttr(ctl+'.cornerPin',setRanNode+'.valueX')
    # minX 0 maxX 1, oldMinX -1 oldMaxX 1
    cmds.setAttr(setRanNode+'.minX',0)
    cmds.setAttr(setRanNode+'.maxX',1)
    cmds.setAttr(setRanNode+'.oldMinX',-1)
    cmds.setAttr(setRanNode+'.oldMaxX',1)
    
    #outValueX >> face_Lower_bindW0
    cmds.connectAttr(setRanNode+'.outValueX',const1+'.'+P1+'W0')
    cmds.connectAttr(setRanNode+'.outValueX',clsConst+'.'+P1+'W0')
    #outValueX >> inputX, outputX >> jaw_bindW1
    revNode = cmds.createNode('reverse') #reverse node
    cmds.connectAttr(setRanNode+'.outValueX',revNode+'.inputX')
    cmds.connectAttr(revNode+'.outputX',const1+'.'+P2+'W1')
    cmds.connectAttr(revNode+'.outputX',clsConst+'.'+P2+'W1')
    
       
def _createBsCrv(orig,names,grpName):
    grp = cmds.group(em=True,n=grpName)
    for name in names:
        crv = cmds.duplicate(orig, n=name)[0]
        cmds.parent(crv,grp)

def _createBsNode(name, orig, targList):
    bs = cmds.blendShape(orig, n=name, o='local')[0] #o is origin
    for num,targ in enumerate(targList):
        cmds.blendShape(bs, e=True, t=(orig, num, targ, 1.0) )

def _setBsCvWeight(bs):
    for i in range(8):
        for j in range(12):
            val=1
            if j in [3,9]: #middle vertex
                val=.5
            elif j in [0,1,2,10,11]: #left side vertex
                if i%2==1: #i is 1,3,5,7. left side target
                    val=0
            elif j in [4,5,6,7,8]: #right side vertex
                if i%2==0: #i is 0,2,4,6. right side target
                    val=0
            cmds.setAttr(bs+'.inputTarget[0].inputTargetGroup[%d].targetWeights[%d]'%(i,j), val)
            #myVal = cmds.getAttr('mouth_curve_blend.inputTarget[0].inputTargetGroup[%d].targetWeights[%d]'%(i,j))
            #print('targetGrp:',i, 'targetW:', j, myVal)
            
            
def _symmetricMouthCrv(crvList):
    outList = []
    for crv in crvList:
        CVs = ModFunc._getCVs(crv)
        posList = DataFunc._getTransform(CVs, t=True, r=False, os=True)
        for num,i in enumerate(posList):
            if num<len(CVs)/4:
                x,y,z = i['pos']
                posList[len(CVs)//2-num]['pos']=(-x,y,z)
            elif len(CVs)*3/4<num:
                x,y,z = i['pos']
                posList[len(CVs)*3//2-num]['pos']=(-x,y,z)
        outList += posList
    return outList

def _connectCornerCtrl(mCornerCtls, blendCrvs, bs):
    #rCtl = mCornerCtls[0]
    #lCtl = mCornerCtls[1]
    #blendCrvs = 
    #[ wideR wideL smallR smallL smileR smileL frownR frownL ]
    #[ 0     1     2      3      4      5      6      7      ]
    for num,ctl in enumerate(mCornerCtls):
        ###
        clp = cmds.createNode('clamp')
        cmds.setAttr(clp+'.maxR',10)
        cmds.setAttr(clp+'.minG',-10)
        cmds.connectAttr(ctl+'.tx',clp+'.inputR')
        cmds.connectAttr(ctl+'.tx',clp+'.inputG')
        cmds.connectAttr(clp+'.outputR',bs+'.'+blendCrvs[0+num]) #0 or 1
        
        mul = cmds.createNode('multDoubleLinear')
        cmds.setAttr(mul+'.input2',-1)
        cmds.connectAttr(clp+'.outputG',mul+'.input1')
        cmds.connectAttr(mul+'.output',bs+'.'+blendCrvs[2+num]) #2 or 3
        ###
        rng = cmds.createNode('setRange')
        cmds.setAttr(rng+'.minX',10)
        cmds.setAttr(rng+'.oldMinX',-10)
        cmds.setAttr(rng+'.maxY',10)
        cmds.setAttr(rng+'.oldMaxY',10)
        cmds.connectAttr(ctl+'.ty',rng+'.valueX')
        cmds.connectAttr(ctl+'.ty',rng+'.valueY')
        cmds.connectAttr(rng+'.outValueX',bs+'.'+blendCrvs[6+num]) #6 or 7
        cmds.connectAttr(rng+'.outValueY',bs+'.'+blendCrvs[4+num]) #4 or 5
        
    
def _matchCrvRtoL(posList):
    #actually, mouth_curve_r_wide & mouth_curve_l_wide are identical.
    #It doesn't mirror, it match CVs
    rPosList = [d for d in posList if '_r_' in d['name']]
    lPosList = [d for d in posList if '_l_' in d['name']]
    for r,l in zip(rPosList,lPosList):
        l['pos'] = r['pos']
    outList = rPosList+lPosList
    return outList