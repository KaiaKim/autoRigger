###-----------------------------------------------------CLASS---------------------------------------------------
class template():
    def __init__(self):
        #These names are from the template file. No change this!
        self.faceBind = 'face_bind'
        self.faceUpBind = 'face_upper_bind' 
        self.faceLoBind = 'face_lower_bind' 

        self.noseBigBind = 'nose_bind'
        self.sneerBinds = ['sneer_r_bind','sneer_l_bind']
        self.nostrilBinds = ['nostril_r_bind','nostril_l_bind']
        self.noseBinds = [self.noseBigBind] + self.sneerBinds + self.nostrilBinds
        
        self.jawBind = 'jaw_bind'
        self.toungueBinds = ['tongue_01_bind', 'tongue_02_bind', 'tongue_03_bind', 'tongue_04_bind', 'tongue_05_bind', 'tongue_06_bind', 'tongue_07_bind']
        self.teethBinds = ['teeth_upper_bind','teeth_lower_bind']
        
        self.eyeSocBinds = ['eye_socket_r_bind','eye_socket_l_bind'] 
        self.eyeBinds = ['eye_r_bind','eye_l_bind']
        
        self.browBigBinds = ['brow_r_bind','brow_l_bind']
        self.browInBinds = ['brow_inner_r_bind','brow_inner_l_bind']
        self.browPeakBinds = ['brow_peak_r_bind','brow_peak_l_bind']
        self.browCorBinds = ['brow_corrugator_r_bind','brow_corrugator_l_bind']
        self.browBinds = self.browBigBinds + self.browInBinds + self.browPeakBinds + self.browCorBinds
        
        self.cheekUpperBinds = ['cheek_upper_r_bind','cheek_upper_l_bind']
        self.cheekMidBinds = ['cheek_r_bind','cheek_l_bind']
        self.cheekLowerBinds = ['cheek_lower_r_bind','cheek_lower_l_bind']
        self.cheekBinds = self.cheekUpperBinds + self.cheekMidBinds + self.cheekLowerBinds

class mouth():
    def __init__(self,verts):
        self.upperCrv = 'lip_upper_curve' #No change this!
        self.lowerCrv = 'lip_lower_curve' #No change this!
        self.crv = 'mouth_curve' #No change this!
            ###
        self.upperLocGrp = 'lip_upper_loc_grp' #Grp means group name
        self.lowerLocGrp = 'lip_lower_loc_grp'
        self.upperLocs = self._lipLocs(verts['lipUpper'], prefix='lip_upper')
        self.lowerLocs = self._lipLocs(verts['lipLower'], prefix='lip_lower')
        self.locs = self.upperLocs + self.lowerLocs
        self.binds = [d.replace('_loc', '_bind') for d in self.locs]
        
        self.drivJntGrp = 'mouth_driver_jnt_grp'
        driverList = ['corner_r','upper_00_r','upper_01_r','upper_m','upper_01_l','upper_00_l','corner_l','lower_00_l','lower_01_l','lower_m','lower_01_r','lower_00_r']
        self.drivJnts = ['mouth_'+d+'_driver' for d in driverList]
        
        self.bindmeshesGrp = 'mouth_bindmesh_grp'
        self.bindmeshes = [d.replace('_driver','_bindmesh') for d in self.drivJnts]
        self.folGrp = 'mouth_fol_grp'
        self.fols = [d.replace('bindmesh','fol') for d in self.bindmeshes]
        self.clusGrp = 'mouth_cls_grp'
        self.clus = [d.replace('bindmesh','cls') for d in self.bindmeshes]
        
            ###
        self.bigCtl = 'mouth_ctl_grp'
        self.microCtlGrp = 'lip_micro_ctl_grp'
        self.microCtls =  [d.replace('fol','ctl').replace('mouth','lip') for d in self.fols]
        self.macroCtlGrp = 'lip_macro_ctl_grp'
        self.macroFols = [d for d in self.fols if '_m_' in d] #'mouth_upper_m_fol','mouth_lower_m_fol'
        self.macroCtls = [d.replace('fol','ctl') for d in self.macroFols]
        self.thickCtlGrp = 'lip_thick_ctl_grp'
        self.thickCtls = ['lip_thick_upper_ctl','lip_thick_lower_ctl']
        self.cornerCtlGrp = 'mouth_corner_ctl_grp'
        self.cornerFols = [d for d in self.fols if '_corner_' in d]
        self.cornerCtls = [d.replace('fol','ctl') for d in self.cornerFols]
        self.cvCls = [d.replace('lip_','lipCv_').replace('_ctl','_cls') for d in self.microCtls] #ex) lipCV_corner_r_cls
        
            ###
        self.blendCrvGrp = 'mouth_blend_crv_grp'
        suffixList = ['_wide','_small','_smile','_frown']
        self.blendCrvs = []
        for suffix in suffixList:
            self.blendCrvs.append(self.crv+'_r'+suffix)
            self.blendCrvs.append(self.crv+'_l'+suffix)
        self.bsNode = 'mouth_curve_blend'
        
    def _lipLocs(self,inList, prefix=''):
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


class lid():
    def __init__(self,verts):
        self.crvs = ['upper_lid_r_curve', 'lower_lid_r_curve', 'upper_lid_l_curve', 'lower_lid_l_curve'] #No change this!
        self.drivCrvs = [d.replace('_curve','_driver_curve') for d in self.crvs] #lid driver curve
        
        self.ctlGrp = 'blink_ctl_grp'
        self.ctls = ['blink_upper_r_ctl', 'blink_lower_r_ctl', 'blink_upper_l_ctl', 'blink_lower_l_ctl']  
        
        self.microCtlGrp = 'lid_micro_ctl_grp'
        self.drivJnts = [] #upper_r_0_driver lower_r upper_l lower_l
        for crv in self.crvs:
            for i in range(5):
                self.drivJnts.append(crv.rsplit('_',1)[0]+'_'+str(i)+'_driver') 
        self.microCtls = [d.replace('_driver','_ctl') for d in self.drivJnts]
        
        self.rLocGrp = 'lid_r_loc_grp'
        self.lLocGrp = 'lid_l_loc_grp'
        self.upperRLocs = self._eyeLocs(verts['lidUpperR'], prefix='lid_upper_r')
        self.upperLLocs = self._eyeLocs(verts['lidUpperR'], prefix='lid_upper_l') #we're just getting len of the list. left&right doesn't matter
        self.lowerRLocs = self._eyeLocs(verts['lidLowerR'], prefix='lid_lower_r')
        self.lowerLLocs = self._eyeLocs(verts['lidLowerR'], prefix='lid_lower_l')
        self.rLocs = self.upperRLocs + self.lowerRLocs
        self.lLocs = self.upperLLocs + self.lowerLLocs
        
        self.rBinds = [d.replace('_loc', '_bind') for d in self.rLocs]
        self.lBinds = [d.replace('_loc', '_bind') for d in self.lLocs]
        
        self.rBlendCrvGrp = 'lid_r_blend_crv_grp'
        self.lBlendCrvGrp = 'lid_l_blend_crv_grp'
        suffixList = ['_open','_neutral','_mid','_closed']
        self.rBlendCrvs = [self.crvs[0]+d for d in suffixList]+[self.crvs[1]+d for d in suffixList]
        self.lBlendCrvs = [d.replace('_r_','_l_') for d in self.rBlendCrvs]
        nodeNames = ['upper_r_open','upper_r_closed','lower_r_open','lower_r_closed']
        self.rBsNodes = ['lid_'+d+'_blend' for d in nodeNames]
        self.lBsNodes = [d.replace('_r_','_l_') for d in self.rBsNodes]
        
    def _eyeLocs(self,inList, prefix=''):
        outList = []
        for i in range(len(inList)):
            name = prefix
            name += '_%02d' %i #'lower_lid_00_l_loc'
            name += '_loc'
            
            outList.append(name) #append the loc name to self.lipLocs list
        return outList


class eye():
    def __init__(self,verts):
            ###
        self.rotCtl = 'eye_rot_ctl'
        self.ctls = ['eye_r_ctl','eye_l_ctl']
        self.aimCtl = 'eye_aim_ctl'
        self.aimMicroCtls = ['eye_r_aim_ctl','eye_l_aim_ctl']
        self.pupilCtls = ['eye_r_pupil_ctl','eye_l_pupil_ctl']
            ###
        self.rLoft = None

class brow():
    def __init__(self,verts):
        self.ctlGrp = 'brow_ctl_grp'
        self.ctls = ['brow_r_ctl','brow_l_ctl']
        self.inCtls = ['brow_inner_r_ctl','brow_inner_l_ctl']
        self.peakCtls = ['brow_peak_r_ctl','brow_peak_l_ctl']
        
        self.drv = [d.replace('_ctl','_driver') for d in self.ctls]
        self.localDrv = [d.replace('_ctl','_localDriver') for d in self.ctls]
        
        self.inDrv =[d.replace('_ctl','_driver') for d in self.inCtls]
        self.inLocalDrv = [d.replace('_ctl','_localDriver') for d in self.inCtls]
        
        self.peakDrv =[d.replace('_ctl','_driver') for d in self.peakCtls]
        self.peakLocalDrv = [d.replace('_ctl','_localDriver') for d in self.peakCtls]
        
        self.xfGrp = 'brow_xform_grp'
        
class nose():
    def __init__(self,verts):
        self.ctlGrp = 'nose_ctl_grp'
        self.ctl = 'nose_ctl'
        self.sneerCtls = ['nose_sneer_r_ctl', 'nose_sneer_l_ctl']
        self.nostrilCtls = ['nose_nostril_r_ctl', 'nose_nostril_l_ctl']
        
