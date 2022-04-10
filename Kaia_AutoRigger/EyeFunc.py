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
        
def _createLoftBall():
    pass
    
def _SlideOnSurface():
    pass