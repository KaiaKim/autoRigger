###-----------------------------------------------------CLASS---------------------------------------------------
class Face():
    def __init__(self):
        self.bind = 'face_bind'
        self.upBind = 'face_upper_bind' 
        self.loBind = 'face_lower_bind' 
        self.jawBind = 'jaw_bind'
        self.jawTipBind = 'jaw_tip_bind'
        
        self.ctl = 'face_ctl'
        self.upCtl = 'face_upper_ctl'
        self.loCtl = 'face_lower_ctl'
        self.jawCtl = 'jaw_ctl'


class Mouth():
    def __init__(self,verts):
        self.upCrv = 'lip_upper_curve' #No change this!
        self.loCrv = 'lip_lower_curve' #No change this!
        self.crv = 'mouth_curve' #No change this!

        self.upBindGrp = 'lip_upper_bind_grp' #Grp means group name
        self.loBindGrp = 'lip_lower_bind_grp'
        self.upBinds = self._lipBinds(verts['lipUpper'], prefix='lip_upper')
        self.loBinds = self._lipBinds(verts['lipLower'], prefix='lip_lower')
        self.binds = self.upBinds + self.loBinds
        
        mList = ['_corner_r','_upper_00_r','_upper_01_r','_upper_m','_upper_01_l','_upper_00_l','_corner_l','_lower_00_l','_lower_01_l','_lower_m','_lower_01_r','_lower_00_r']
        self.drivGrp = 'mouth_driver_grp'
        self.drivs = ['mouth'+d+'_driver' for d in mList]
        self.lipDrivGrp = 'lip_driver_grp'
        self.lipDrivs = ['lip'+d+'_driver' for d in mList]
        self.bindmeshesGrp = 'mouth_bindmesh_grp'
        self.bindmeshes = ['mouth'+d+'_bindmesh' for d in mList]
        self.uvPins = ['mouth'+d+'_uvPin' for d in mList]
        
        self.clusGrp = 'mouth_cls_grp'
        self.clus = 'mouth_cls'
        self.jawClus = ['jaw_upper_cls','jaw_lower_cls']
        self.cornerClus = ['mouth_corner_r_cls','mouth_corner_l_cls']

        self.ctl = 'mouth_ctl'
        self.lipCtlGrp = 'lip_ctl_grp'
        self.lipCtls =  ['lip'+d+'_ctl' for d in mList]
        self.cornerCtls = ['mouth_corner_r_ctl','mouth_corner_l_ctl']

        self.blendCrvGrp = 'mouth_blend_crv_grp'
        mbList = ['_r_wide','_l_wide','_r_small','_l_small','_r_smile','_l_smile','_r_frown','_l_frown']
        self.blendCrvs = ['mouth'+d+'_blendCurve' for d in mbList]
        self.bsNode = 'mouth_curve_blend'

    def _lipBinds(self,inList, prefix=''):
        outList = []
        for i in range(len(inList)):
            name = prefix
            if i==((len(inList)-1)/2):
                name += '_m_'
            elif i<((len(inList)-1)/2):
                name += '_r_%02d'%i #result: 'lip_lower_l_00_loc'
            elif i>((len(inList)-1)/2):
                name += '_l_%02d'%( (len(inList)-1)-i ) #result: 'lip_lower_r_00_loc'
            name += '_bind'
            
            outList.append(name) #append the loc name to self.lipLocs list
        return outList
    
class Cheek():
    def __init__(self):
        cList = ['_upper_r','_upper_l','_r','_l','_lower_r','_lower_l']
        self.bindGrp = 'cheek_bind_grp'
        self.binds = ['cheek'+d+'_bind' for d in cList]
        self.ctlGrp = 'cheek_ctl_grp'
        self.ctls = ['cheek'+d+'_ctl' for d in cList]
        self.drvs = ['cheek_driver_r_nul','cheek_driver_l_nul']
        
class TeethTongue():
    def __init__(self):
        tList=['_01','_02','_03','_04','_05','_06','_07',]
        self.tongueCtlGrp = 'tongue_ctl_grp'
        self.tongueBinds = ['tongue'+d+'_bind' for d in tList]
        self.tongueCtls = ['tongue'+d+'_ctl' for d in tList]
        
        self.teethBinds = ['teeth_upper_bind','teeth_lower_bind']
        self.teethCtls = ['teeth_upper_ctl','teeth_lower_ctl']
        


class Lid():
    def __init__(self,verts):
        lList = ['_upper_r', '_lower_r', '_upper_l', '_lower_l']
        self.crvs = ['lid'+d+'_curve' for d in lList] #No change this!
        self.drivCrvs = ['lid'+d+'_driver_curve' for d in lList] #lid driver curve
        
        self.ctlGrp = 'blink_ctl_grp'
        self.ctls = ['blink'+d+'_ctl' for d in lList]  
        
        self.drivGrp = 'blink_driver_grp'
        self.drivs = [['blink%s_%d_driver'%(i,d) for d in range(5)] for i in lList]
        self.lidDrivGrp = 'lid_driver_grp'
        self.lidDrivs = [['lid%s_%d_driver'%(i,d) for d in range(5)] for i in lList]
        self.microCtlGrp = 'lid_micro_ctl_grp'
        self.microCtls = [['lid%s_%d_ctl'%(i,d) for d in range(5)] for i in lList]
        
        self.rBindGrp = 'lid_r_bind_grp'
        self.lBindGrp = 'lid_l_bind_grp'
        self.upperRBinds = self._eyeBinds(verts['lidUpperR'], prefix='lid_upper_r')
        self.upperLBinds = self._eyeBinds(verts['lidUpperR'], prefix='lid_upper_l') #we're just getting len of the list. left&right doesn't matter
        self.lowerRBinds = self._eyeBinds(verts['lidLowerR'], prefix='lid_lower_r')
        self.lowerLBinds = self._eyeBinds(verts['lidLowerR'], prefix='lid_lower_l')
        self.rBinds = self.upperRBinds + self.lowerRBinds
        self.lBinds = self.upperLBinds + self.lowerLBinds
        
        self.rBlendCrvGrp = 'lid_r_blend_crv_grp'
        self.lBlendCrvGrp = 'lid_l_blend_crv_grp'
        suffixList = ['_open','_neutral', '_mid', '_closed']
        self.rBlendCrvs = [self.crvs[0]+d for d in suffixList]+[self.crvs[1]+d for d in suffixList]
        self.lBlendCrvs = [d.replace('_r_', '_l_') for d in self.rBlendCrvs]
        nodeNames = ['upper_r_open', 'upper_r_closed', 'lower_r_open', 'lower_r_closed']
        self.rBsNodes = ['lid_'+d+'_blend' for d in nodeNames]
        self.lBsNodes = [d.replace('_r_', '_l_') for d in self.rBsNodes]
        
    def _eyeBinds(self,inList, prefix=''):
        outList = []
        for i in range(len(inList)):
            name = prefix
            name += '_%02d' %i #'lower_lid_00_l_bind'
            name += '_bind'
            
            outList.append(name) #append the bind name to self.lipBinds list
        return outList


class Eye():
    def __init__(self):
        self.socBinds = ['eye_socket_r_bind','eye_socket_l_bind'] 
        self.binds = ['eye_r_bind','eye_l_bind']
            ###
        self.rotCtl = 'eye_rot_ctl'
        self.ctls = ['eye_r_ctl','eye_l_ctl']
        self.aimCtl = 'eye_aim_ctl'
        self.aimMicroCtls = ['eye_r_aim_ctl','eye_l_aim_ctl']
        self.pupilCtls = ['eye_r_pupil_ctl','eye_l_pupil_ctl'] #not using
            ###
        self.rLoft = None

class Brow():
    def __init__(self):
        self.bigBinds = ['brow_r_bind','brow_l_bind']
        self.inBinds = ['brow_inner_r_bind','brow_inner_l_bind']
        self.peakBinds = ['brow_peak_r_bind','brow_peak_l_bind']
        self.corBinds = ['brow_corrugator_r_bind','brow_corrugator_l_bind']
        self.binds = self.bigBinds + self.inBinds + self.corBinds + self.peakBinds
        
        self.ctlGrp = 'brow_ctl_grp'
        self.bigCtls = ['brow_r_ctl','brow_l_ctl']
        self.inCtls = ['brow_inner_r_ctl','brow_inner_l_ctl']
        self.corCtls = ['brow_corrugator_r_ctl','brow_corrugator_l_ctl']
        self.peakCtls = ['brow_peak_r_ctl','brow_peak_l_ctl']
        self.ctls = self.bigCtls + self.inCtls + self.corCtls + self.peakCtls

        
class Nose():
    def __init__(self):
        self.tipBind = 'nose_bind'
        self.bridgeBind = 'nose_bridge_bind'
        self.sneerBinds = ['sneer_r_bind','sneer_l_bind']
        self.binds = [self.tipBind,self.bridgeBind] + self.sneerBinds
        
        self.ctlGrp = 'nose_ctl_grp'
        self.bridgeCtl = 'noseBridge_ctl'
        self.ctl = 'nose_ctl'
        self.sneerCtls = ['nose_sneer_r_ctl', 'nose_sneer_l_ctl']

        
