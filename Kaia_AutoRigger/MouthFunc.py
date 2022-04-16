import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

def _createMouthCrv(name, upperCrv, lowerCrv):
    upperCVs = ModFunc._getCVs(upperCrv)
    lowerCVs = ModFunc._getCVs(lowerCrv)
    lowerCVs.reverse() #reverse list order so that it comes back to the start, as a circle

    cvList = upperCVs + lowerCVs

    sectionCount = len(cvList)-2
    mouthCrv = cmds.circle(n=name, s=sectionCount )[0] #create a new curve
    
    cmds.makeIdentity(mouthCrv, apply=True) #freeze transformation
    cmds.xform(mouthCrv, piv=(0,0,0), ws=True) #set pivot to 0,0,0
    cmds.delete(mouthCrv,constructionHistory=True)
    
    counter = 0 #this is a counter
    for i in range(sectionCount): #We're going to iterate through mouth curv(CVs)
        pos=cmds.xform(cvList[counter], q=True, t=True, ws=True) #get world position from the CV
        if counter==sectionCount/2: #there's two cvs overlapping on the corner. sectionCount/2 is the right corner CV.
            counter+=1 #We skip the overlapping cv by adding 1 to the counter
               
        mouthCV = mouthCrv + '.cv[%d]'%i #get mouth CV
        cmds.move(pos[0],pos[1],pos[2],mouthCV) #snap mouth CV to the position

        counter+=1 #increase counter
    
    return mouthCrv

def _lipLocsNamer(inList, prefix=''):
    outList = []
    for i in range(len(inList)):
        name = prefix
        if i==((len(inList)-1)/2):
            name += '_m_'
        elif i<((len(inList)-1)/2):
            name += '_r_%02d'%i #result: 'lip_lower_l_00_loc'
        elif i>((len(inList)-1)/2):
            name += '_l_%02d'%( (len(inList)-1)-i ) #result: 'lip_lower_r_00_loc'
        name += '_loc'
        
        outList.append(name) #append the loc name to self.lipLocs list
    return outList
    



def _2CurvCvCls(names,upCurv,loCurv):
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
    
    for cv,name in zip(cvList,names):
        clus = cmds.cluster(cv, n=name)[1] #[1] gets trans node #lipCv_lower_r_00_clsHandle
        clsList.append(name)
        offGrp = cmds.group(clus,n=name+'_offset')

        cmds.parent(offGrp, ctl) #(child, parent)
    
    return clsList

def constMicroToMacro(inList):
    for i in inList:
        if '_m_' in i:
            nul2 = cmds.group(i+'_orient',n=i+'_nul2') #create nul2 grp
            macro = i.replace('lip','mouth') #micro_mouth_lower_m_ctl
            cmds.parentConstraint(macro,nul2,mo=True)

def attachJawCls(jawCls, mouthCtls, faceLowerBind, jawBind):
    #We're gonna parent constraint jawClusters to the mouth macro controllers
    for clus in jawCls:
        if '0' not in clus: #corner or mid
            parent1=faceLowerBind
            parent2=jawBind
        
        elif '0' in clus: #inbetween
            if 'upper' in clus:
                parent1=mouthCtls[0] #macro_mouth_upper_ctl
            elif 'lower' in clus:
                parent1=mouthCtls[1] #macro_mouth_lower_ctl
            
            if '_r_' in clus:
                parent2=jawCls[0] #mouth_corner_r_cls
            if '_l_' in clus:
                parent2=jawCls[len(jawCls)//2] #mouth_corner_l_cls
            
        cmds.parentConstraint(parent1,parent2,clus,mo=True)
        #set mouth constraint weight value
        _setWeightVal(clus, parent1,parent2)

def _setWeightVal(child, parent00, parent01):
    #should I hard coad weight values? maybe I could set up a set driven key
    constraint = child + '_parentConstraint1'
    W0 = 1 #Face Lower Bind W0
    if '_corner_' in child:
        W0=.5
    elif '_upper_' in child:
        W0=1
    elif '_lower_' in child:
        W0=0

    W1 = 1-W0 #Jaw Bind W1
    
    cmds.setAttr(constraint+'.'+parent00+'W0', W0)
    cmds.setAttr(constraint+'.'+parent01+'W1',W1)
    cmds.setAttr(constraint+'.interpType',2) #Interpolation Type: Shortest


def setMouthCornerCtls(mCornerCtls, mouthCtls, jawCls, faceLowerBind,jawBind):
    cornerCls = [d for d in jawCls if '_corner_' in d] #left, right
    inbetweenCls = [d for d in jawCls if '0' in d ]
    #inbetweenCls = [d for d in jawCls if re.findall('[0-9]+',d)!=[] ]
    
    #set corner pin
    _setCornerPin(cornerCtl[0], cornerCls[0], faceLowerBind,jawBind)
    _setCornerPin(cornerCtl[1], cornerCls[1], faceLowerBind,jawBind)

    #add attribute
    for ctl in mcornerCtls:
        cmds.addAttr(ctl, shortName='lipOnePull', defaultValue=0, minValue=0, maxValue=1)
        cmds.addAttr(ctl, shortName='lipTwoPull', defaultValue=0, minValue=0, maxValue=1)
    
    ###--------------------MouthFunc._setLipPull()
    _connectLipPull(mcornerCtls,inbetweenCls,mouthCtls,cornerCls)


def _setCornerPin(ctl,clus,parent1,parent2):
    #ctl='mouth_corner_r_ctl'
    #clus='mouth_corner_r_cls'
    #parent1='face_lower_bind'
    #parent2='jaw_bind'
    
    #Add Attribute: cornerPin min -1, max 1, default 0
    cmds.addAttr(ctl, shortName='cornerPin', defaultValue=0, minValue=-1, maxValue=1)
    
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
    cmds.connectAttr(setRanNode+'.outValueX',clus+'_parentConstraint1.'+parent1+'W0')
    
    #reverse node
    revNode = cmds.createNode('reverse')
    #outValueX >> inputX, outputX >> jaw_bindW1
    cmds.connectAttr(setRanNode+'.outValueX',revNode+'.inputX')
    cmds.connectAttr(revNode+'.outputX',clus+'_parentConstraint1.'+parent2+'W1')
    

def _connectLipPull(cornerCtl,clsList,midCtl,cornerCls):
    #upperLip01Rcls = 'mouth_upper_r_01_cls'
    #lowerLip01Rcls = 'mouth_lower_r_01_cls'
    #parent3 = 'mouth_upper_m_ctl' #upper lower
    #parent4 = 'mouth_corner_r_cls' #left right
    
    # connect to upper_lip_01_l_cls_parentConstraint1, lower_lip_01_l_cls_parentConstraint1
    # either follow the upper lip or the lip corner
    for clus in clsList:
        if '_00_' in clus: 
            attr='.lipOnePull'
        elif '_01_' in clus:
            attr='.lipTwoPull'
        
        if '_upper_' in clus:
            parent3 = midCtl[0]
        elif '_lower_' in clus:
            parent3 = midCtl[1]
        
        if '_r_' in clus:
            ctl = cornerCtl[0]
            parent4 = cornerCls[0]
        elif '_l_' in clus:
            ctl = cornerCtl[1]
            parent4 = cornerCls[1]
            
        #print('ctl:',ctl,'clus:',clus, 'attr:',attr, 'p3:', parent3, 'p4:', parent4)
        #lipOnePull >> lower_lip_ctlW0
        cmds.connectAttr(ctl+attr,clus+'_parentConstraint1.'+parent3+'W0' )
        
        #reverse node
        revNode2 = cmds.createNode('reverse')
        #lipOnePull >> inputX, outputX >> lip_corner_l_clsW1
        cmds.connectAttr(ctl+attr,revNode2+'.inputX')
        cmds.connectAttr(revNode2+'.outputX',clus+'_parentConstraint1.'+parent4+'W1')
        
def _createBsCrv(orig,nameList,grpName):
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
        posList = ModFunc._getTransformData(CVs, t=True, r=False, os=True)
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
    for ctl,i in enumerate(mCornerCtls):
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