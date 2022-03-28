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
    
    
def _mouthDriverNamer(inList, prefix='',suffix='', doubleCorner=True):
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
            
        if c != len(inList)/4 and c != len(inList)*3/4: #not in the middle        
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

def _jawClsNamer(inList):
    #clsList: ['cluster1Handle_l_corner', 'cluster2Handle', 'cluster3Handle', 'cluster4Handle', 'cluster5Handle', 'cluster6Handle', 'cluster7Handle_r_corner', 'cluster8Handle', 'cluster9Handle', 'cluster10Handle', 'cluster11Handle', 'cluster12Handle']
    #result: ['lip_corner_l_cls','upper_lip_01_r_cls','lip_upper_cls',.....]
    #reference driver namer
    pass