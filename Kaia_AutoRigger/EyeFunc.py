import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

def _eyeLocsNamer(locs, side='', prefix=''):
    outList = []
    for i,loc in enumerate(locs):
        name = prefix
        name += '_%02d' %i #'lower_lid_00_l_loc'
        name += '_loc'
        cmds.rename(loc,name)
        
        outList.append(name) #append the loc name to self.lipLocs list
    return outList
    
def _createBsCrv(origList,suffixList,grpName):
    outList = []
    grp = cmds.group(em=True,n=grpName)
    for orig in origList:
        for suffix in suffixList:
            crv1 = cmds.duplicate(orig, n=orig+suffix)[0]
            cmds.parent(crv1,grp)
            outList.append(crv1)
    return outList
    

def _createBsNode(origList,suffixList):
    outList = []
    for orig in origList:
        bls = cmds.blendShape(orig, n=orig.replace('_curve','_blend'), o='local')[0]
        for num,suffix in enumerate(suffixList):
            targ=orig+suffix
            cmds.blendShape(bls, e=True, t=(orig, num, targ, 1.0))
        outList.append(bls)
    return outList
            
            
def _connectCornerCtrl(blinkCtls, blendCrvs, bsNodeList):
    #blinkCtls = [{'ctl': 'blink_upper_r_ctl'}, {'ctl': 'blink_lower_r_ctl'}, {'ctl': 'blink_upper_l_ctl'}, {'ctl': 'blink_lower_l_ctl'}]
    #bsNodeList = ['upper_lid_r_blend','lower_lid_r_blend','upper_lid_l_blend','lower_lid_l_blend']
    #closedCrvs=['upper_lid_r_curve_closed','lower_lid_r_curve_closed','upper_lid_l_curve_closed','lower_lid_l_curve_closed']
    upperCtls = [d['ctl'] for d in blinkCtls if 'upper' in d['ctl']]
    lowerCtls = [d['ctl'] for d in blinkCtls if 'lower' in d['ctl']]
    upperNode = [d for d in bsNodeList if 'upper' in d]
    lowerNode = [d for d in bsNodeList if 'lower' in d]
    upperClosed = [d for d in blendCrvs if 'upper' in d and 'closed' in d]
    lowerClosed = [d for d in blendCrvs if 'lower' in d and 'closed' in d]
    
    
    for i in range(2):
            #upper
        #set driven key node1
        drv1 = cmds.setDrivenKeyframe( upperNode[i]+'.'+upperClosed[i], cd=upperCtls[i]+'.rx' )
        drv1 = upperNode[i]+'_'+upperClosed[i] #given node name is 'upper_lid_r_blend_upper_lid_r_curve_closed'
        
            #lower
        #reverse node
        rev = cmds.createNode('reverse')
        #addDoubleLinear node
        addDou = cmds.createNode('addDoubleLinear')
        #clamp node
        clmp = cmds.createNode('clamp')
        
        #set driven key node2
        drv2 = cmds.setDrivenKeyframe(clmp+'.inputR', cd=lowerCtls[i]+'.rx')
        drv2 = clmp+'_'+'inputR'
        
        #driven1 output >> reverse inputX
        cmds.connectAttr(drv1+'.output',rev+'.inputX')
        #reverse outputX >> addDoubleLinear input1
        cmds.connectAttr(rev+'.outputX',addDou+'.input1')
        #addDoubleLinear input2, 0.333
        cmds.setAttr(addDou+'.input2',0.333)
        #addDoubleLinear output >> clamp maxR
        cmds.connectAttr(addDou+'.output',clmp+'.maxR')
        #clamp outputR >> blend weight lower_lid_l_closed_curve
        cmds.connectAttr( clmp+'.outputR', lowerNode[i]+'.'+ lowerClosed[i] )
    
    
    ###
    # To set the keyframe on the selected object's translateX based on
    # curve1's rotateZ:
    #cmds.setDrivenKeyframe( at='translateX', cd='curve1.rz' )
    pass
    
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
    
def _roatateCtrlShape(ctls):
    for ctl in ctls:
        CVs = ModFunc._getCVs(ctl)
        cmds.rotate(90,0,0,CVs)
    
def _createLoftBall():
    pass
    
def _SlideOnSurface():
    pass