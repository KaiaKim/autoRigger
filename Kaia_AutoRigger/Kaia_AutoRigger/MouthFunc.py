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
    mouthCrv = cmds.circle(n=name, s=sectionCount, d=1)[0] #create a new curve #cv 0~11
    cmds.delete(mouthCrv,constructionHistory=True)

    counter = 0 #this is a counter
    for i in range(12): #We're going to iterate through mouth curv(CVs)
        pos=cmds.xform(cvList[counter], q=True, t=True, ws=True) #get world position from the CV
        if counter==6: #there's two cvs overlapping on the corner. 6 is the right corner CV.
            counter+=1 #We skip the overlapping cv by adding 1 to the counter
               
        mouthCV = mouthCrv + '.cv[%d]'%i #get mouth CV
        cmds.move(pos[0],pos[1],pos[2],mouthCV) #snap mouth CV to the position

        counter+=1 #increase counter

def _createBindmeshesOnJnts(names,jnts,grpName):
    grp = cmds.group(em=True,n=grpName)
    for jnt,name in zip(jnts,names):
        pos=cmds.xform(jnt,q=True,ws=True,t=True)
        bindmesh = cmds.polyPlane(w=.3,h=.3,sw=1,sh=1,n=name)[0]
        cmds.move(pos[0],pos[1],pos[2],bindmesh)
        cmds.makeIdentity(bindmesh, apply=True) #freeze transformation. If I don't do this, follicles won't attach
        cmds.delete(bindmesh,constructionHistory=True)
        cmds.skinCluster(jnt,bindmesh,n='bindMesh_skinCluster',tsb=True)#tsb means toSelectedBones
        
        cmds.parent(bindmesh,grp)

    
def _createFolsOnBindmeshes(names,bindmeshes,grpName):
    grp = cmds.group(em=True, n=grpName)
    for bindmesh,name in zip(bindmeshes,names):
        folShape = cmds.createNode('follicle', n=name+'_shape' )
        folTrans = cmds.listRelatives(folShape, p=1)[0]
        folTrans = cmds.rename(folTrans, name)
        bmShape = cmds.listRelatives(bindmesh, type='mesh')[0]

        cmds.connectAttr(bmShape+'.worldMesh', folShape+'.inputMesh')
        cmds.connectAttr(folShape+'.outTranslate', folTrans+'.t')
        cmds.connectAttr(folShape+'.outRotate', folTrans+'.r')
        cmds.setAttr(folShape+'.parameterU', .5)
        cmds.setAttr(folShape+'.parameterV', .5)
        
        cmds.parent(folTrans, grp)

def _createMouthDrivers(names,curv,grpName):
    cmds.group(em=True, n=grpName)
    curvShape = ModFunc._getCrvShape(curv)
    cvs = ModFunc._getCVs(curv)

    for num,cv in enumerate(cvs):
        cmds.select(cl=True)
        poc1 = cmds.createNode('pointOnCurveInfo')
        cmds.connectAttr(curvShape+'.worldSpace[0]', poc1+'.inputCurve', f=True)
        cmds.setAttr(poc1+'.turnOnPercentage',1)
        cmds.setAttr(poc1 + '.parameter', num/11)
        jnt= cmds.joint(rad=.5,n=names[num])
        cmds.connectAttr(poc1+'.position', jnt+'.t')
        cmds.parent(jnt,grpName)

def _createLipDrivers(names,fols,ctls,grpName):
    cmds.group(em=True,n=grpName)

    for name,fol,ctl in zip(names,fols,ctls):  
        cmds.select(cl=True)
        jnt = cmds.joint(n=name,rad=.3)#create joint
        nul = cmds.group(jnt,n=name+'_nul')
        cmds.connectAttr(fol+'.xformMatrix',nul+'.offsetParentMatrix')
        cmds.connectAttr(ctl+'_orient'+'.r',nul+'.r')
        ModFunc._connectTransform(ctl,jnt)
        cmds.parent(nul,grpName)

###
def constMicroToMacro(inList):
    pass
    '''
    for i in inList:
        if '_m_' in i:
            nul2 = cmds.group(i+'_orient',n=i+'_nul2') #create nul2 grp
            macro = i.replace('lip','mouth') #micro_mouth_lower_m_ctl
            cmds.parentConstraint(macro,nul2,mo=True)
    '''       

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
    cmds.spaceLocator(n=name)#create driver
    cmds.group(name,n=name+'_nul')#create driver nul
    cmds.parent(name+'_nul',ctl,r=True) #match jaw ctl
    cmds.parent(name+'_nul',grp)#parent to anim grp
    ModFunc._connectTransform(ctl,name)#connect translate, rotate
    cmds.parentConstraint(name,clus,mo=True)
    

def attachCorner(ctl,clus,P1,P2):
    '''
    ###parent const clus to p1,p2
    clsConst = cmds.parentConstraint(P1, P2, clus,mo=True)[0]
    cmds.setAttr(clsConst+'.interpType',2)
    '''
    ###parent const nul to p1,p2
    blend1 = cmds.createNode('blendMatrix')
    nul = ctl+'_nul'
    cmds.connectAttr(P1+'.xformMatrix',blend1+'.inputMatrix')
    cmds.connectAttr(P2+'.xformMatrix',blend1+'.target[0].targetMatrix')
    cmds.setAttr(blend1+'.target[0].weight',0.5)
    cmds.connectAttr(blend1+'.outputMatrix',nul+'.offsetParentMatrix')


    
    '''
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
    '''
    pass
       
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