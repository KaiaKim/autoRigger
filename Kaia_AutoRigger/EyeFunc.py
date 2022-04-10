import maya.cmds as cmds

def _eyeLocsNamer(locs, side='', prefix=''):
    outList = []
    for i,loc in enumerate(locs):
        name = prefix
        name += '_%02d' %i #'lower_lid_00_l_loc'
        name += '_loc'
        cmds.rename(loc,name)
        
        outList.append(name) #append the loc name to self.lipLocs list
    return outList
    
def _createBlendshapeCrv(orig,grpName,newGrp=True):
    outList = []
    if newGrp==True:
        grp = cmds.group(em=True,n=grpName)
    else:
        grp = grpName
    suffixList = ['_open','_closed'] #['_open','_neutral','_mid','_closed']
    for i in suffixList:
        crv1 = cmds.duplicate(orig, n=orig+i)[0]
        outList.append(crv1)
        cmds.parent(crv1,grp)
        
    for num,targ in enumerate(outList):
            bls = cmds.blendShape(orig, n='blend%d'%num, o='local')
            cmds.blendShape(bls, e=True, t=(orig, num, targ, 1.0))
    return outList

def _matchCloseCrv(posList):
    outList = []
    upper = [d for d in posList if 'upper' in d['name'] and '_closed' in d['name']] 
    lower = [d for d in posList if 'lower' in d['name'] and '_closed' in d['name']] 
    for u,l in zip(upper,lower):
        l['pos'] = u['pos']
    outList = upper+lower
    return outList

def _mirrorCVs(posList):
    rPos = [d for d in posList if '_r_' in d['name']]
    lPos = [d for d in posList if '_l_' in d['name']]
    for r,l in zip(rPos,lPos):
        x,y,z = r['pos']
        l['pos']=(-x,y,z)
    outList = rPos+lPos
    return outList

def _createLoftBall():
    pass
    
def _SlideOnSurface():
    pass