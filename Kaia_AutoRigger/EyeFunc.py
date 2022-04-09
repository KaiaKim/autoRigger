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
    
def _createBlendshapeCrv(orig):
    outList = []
    grp = cmds.group(em=True,n=grpName)
    suffixList = ['_wide','_small','_smile','_frown']
    for i in suffixList:
        crv1 = cmds.duplicate(orig, n=orig+i)[0]
        outList.append(crv1)
        cmds.parent(crv1,crv2,grp)
    return outList
        
def _createLoftBall():
    pass
    
def _SlideOnSurface():
    pass