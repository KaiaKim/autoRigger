import maya.cmds as cmds
import importlib

from Kaia_AutoRigger import ModFunc
importlib.reload(ModFunc)

def _eyeLocsNamer(inList, prefix=''):
    outList = []
    for i in range(len(inList)):
        name = prefix
        name += '_%02d' %i #'lower_lid_00_l_loc'
        name += '_loc'
        
        outList.append(name) #append the loc name to self.lipLocs list
    return outList
    
def _createBsCrv(crvs,names,grpName):
    #self.eyeRCrvs = [self.lidUpperRCrv, self.lidLowerRCrv]
    #suffixList = ['_open','_closed','_neutral','_mid']
    #self.eyeRBlendCrvs = [self.lidUpperRCrv+d for d in suffixList]+[self.lidLowerRCrv+d for d in suffixList]
    #names = ['lid_upper_r_curve_open', 'lid_upper_r_curve_closed', 'lid_upper_r_curve_neutral', 'lid_upper_r_curve_mid', ...]
    grp = cmds.group(em=True,n=grpName)
    
    for name in names:
        if 'upper' in name:
            orig = crvs[0]
        elif 'lower' in name:
            orig = crvs[1]
        
        if ('upper'and'neutral') or ('lower'and'closed') in name: #lower_closed = upper_neut = upper_orig
            orig = crvs[0]
            
        if ('lower'and'neutral') or ('upper'and'closed') in name: #upper_closed = lower_neut = lower_ orig
            orig = crvs[1]
        
        dup = cmds.duplicate(orig,n=name)
        cmds.parent(crv, dup)



def _createBsNode(nodes,crvs,targList):
    #nodes = self.eyeRBsNodes = ['upper_r_open','upper_r_closed','lower_r_open','lower_r_closed']
    #crvs = self.eyeRCrvs = [self.lidUpperRCrv, self.lidLowerRCrv]
    #targList = self.eyeRBlendCrvs = ['lid_upper_r_curve_open', 'lid_upper_r_curve_closed', 'lid_upper_r_curve_neutral', 'lid_upper_r_curve_mid', ...]
    for node in nodes:
        if 'upper' in node: x=0
        elif 'lower' in node: x=1
        orig=crvs[x]
        cmds.blendShape(orig, n=node, o='local')
        if '_open' in node:
            cmds.blendShape(node, e=True, t=(orig, 1, targList[0+4*x], 1.0))
        elif '_closed' in node:
            cmds.blendShape(node, e=True, t=(orig, 1, targList[1+4*x], 1.0))
            cmds.blendShape(node, e=True, ib=True, t=(orig, 2, targList[2+4*x], 0.333))
            cmds.blendShape(node, e=True, ib=True, t=(orig, 3, targList[3+4*x], 0.666))
            

            
def _connectCornerCtrl(blinkCtls, blendCrvs, bsNodeList):
    #blinkCtls = [{'ctl': 'blink_upper_r_ctl'}, {'ctl': 'blink_lower_r_ctl'}, {'ctl': 'blink_upper_l_ctl'}, {'ctl': 'blink_lower_l_ctl'}]
    #bsNodeList = ['upper_lid_r_blend','lower_lid_r_blend','upper_lid_l_blend','lower_lid_l_blend']
    #closedCrvs=['upper_lid_r_curve_closed','lower_lid_r_curve_closed','upper_lid_l_curve_closed','lower_lid_l_curve_closed']
    upperCtls = [d for d in blinkCtls if 'upper' in d]
    lowerCtls = [d for d in blinkCtls if 'lower' in d]
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