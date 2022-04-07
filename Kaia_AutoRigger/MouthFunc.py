import maya.cmds as cmds

def _lipLocsNamer(locs, prefix=''):
    outList = []
    for i,loc in enumerate(locs):
        name = prefix
        if i==((len(locs)-1)/2):
            name += '_m_'
        elif i<((len(locs)-1)/2):
            name += '_l_%02d'%i #result: 'lip_lower_l_00_loc'
        elif i>((len(locs)-1)/2):
            name += '_r_%02d'%( (len(locs)-1)-i ) #result: 'lip_lower_r_00_loc'
        name += '_loc'
        cmds.rename(loc,name)
        
        outList.append(name) #append the loc name to self.lipLocs list
    return outList
    
    
def _mouthRigNamer(inList, prefix='',suffix=''):
    if len(inList)%4 != 0:
        print('Error: number of the list elements are not multiple of 4.')
        
    outList = []
    c = 0 #c is a counter for list index
    for i in inList:
        name = prefix
        if c == 0 or c==len(inList)/2: #on the corner
            name += '_corner'
        elif c>0 and c<len(inList)/2: 
            name += '_upper'
        elif c>len(inList)/2:
            name += '_lower'
        
        if c == len(inList)/4 or c == len(inList)*3/4: #in the middle    
            name += '_m'
        elif c != len(inList)/4 and c != len(inList)*3/4: #not in the middle        
            if c < len(inList)/4 or c > len(inList)*3/4: #on the right
                name += '_r'
            else:
                name += '_l'
            
            if '_corner' in name:
                numUp = 0 #numUp is a counter for rename 
                numDown = (len(inList)-4)//4 -1 #numDown is a counter that goes reverse direction. It decreases from the maximum number
            else:
                if '_upper_r' in name or 'lower_l' in name:
                    name += ('_%02d'%numUp)
                    numUp+=1
                elif '_upper_l' in name or 'lower_r' in name:
                    name += ('_%02d'%numDown)
                    numDown-=1
                              
        name += suffix
        
        cmds.rename(i,name)
        outList.append(name) #put the driver joint name to the list
        c+=1 #increase the counter
    return outList

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
    

def _scaleOrient(ctlDicList):
    for i in ctlDicList:    
        scaleVal = [1,1,1]
        if '_lower_' in i['ctl']:
            scaleVal[2] = -1 #Z value is -1 
        if '_l_' in i['ctl']:
            scaleVal[0] = -1 #X value is -1
        
        cmds.scale(scaleVal[0],scaleVal[1],scaleVal[2],i['ori'])


def _setCornerPin(ctl,clus,parent1,parent2):
    '''
    ctl='mouth_corner_r_ctl'
    clus='mouth_corner_r_cls'
    parent1='face_lower_bind'
    parent2='jaw_bind'
    '''
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
    '''
    upperLip01Rcls = 'mouth_upper_r_01_cls'
    lowerLip01Rcls = 'mouth_lower_r_01_cls'
    parent3 = 'mouth_upper_m_ctl' #upper lower
    parent4 = 'mouth_corner_r_cls' #left right
    '''
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
            
        print('ctl:',ctl,'clus:',clus, 'attr:',attr, 'p3:', parent3, 'p4:', parent4)
        
        #lipOnePull >> lower_lip_ctlW0
        cmds.connectAttr(ctl+attr,clus+'_parentConstraint1.'+parent3+'W0' )
        
        #reverse node
        revNode2 = cmds.createNode('reverse')
        #lipOnePull >> inputX, outputX >> lip_corner_l_clsW1
        cmds.connectAttr(ctl+attr,revNode2+'.inputX')
        cmds.connectAttr(revNode2+'.outputX',clus+'_parentConstraint1.'+parent4+'W1')
        
        


