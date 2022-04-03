import maya.cmds as cmds

def _lipLocsNamer(inList, prefix='', suffix=''): #this function takes a list with mini dics
    outList = []
    ###make function of this
    for i in inList: #i['loc'] is the loc trans, i['xpos'] is the X position of the loc
        name = prefix
        cmds.reorder( i['loc'], back=True )#reorder alphabetically in hierarchy
        if inList.index(i)==( (len(inList)-1)/2 ):
            pass #result: 'lower_lip_loc'
        elif i['xpos']<0:
            name += '_%02d_l'%inList.index(i) #result: 'lower_lip_00_l_loc'
        elif i['xpos']>0:
            name += '_%02d_r'%( (len(inList)-1)-(inList.index(i)) ) #result: 'lower_lip_00_r_loc'
        name += suffix
        cmds.rename(i['loc'],name)
        
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

def _setWeightVal(child, parent00, parent01, follow00=.9, follow01=.7):
    #should I hard coad weight values? maybe I could set up a set driven key
    constraint = child + '_parentConstraint1'
    W0 = 1 #Face Lower Bind W0
    if '_corner_' in child:
        W0=.5
    elif '_upper_' in child:
        W0=1
        if '_00_' in child:
            W0=follow00
        elif '_01_' in child:
            W0=follow01
    elif '_lower_' in child:
        W0=0
        if '_00_' in child:
            W0= follow00
        elif '_01_' in child:
            W0=follow01
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


def _setCornerPin():
    pass

def _setLipPull():
    pass