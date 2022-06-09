import maya.cmds as cmds

#cmds.ls(sl=True)

#button for select bind joints
#template names + lid jnts + lip jnts
faceGeo = 'face'
GabifaceJntList = ['face_bind', 'face_upper_bind', 'brow_l_bind', 'brow_inner_l_bind', 'brow_corrugator_l_bind', 'brow_peak_l_bind', 'brow_r_bind', 'brow_inner_r_bind', 'brow_corrugator_r_bind', 'brow_peak_r_bind', 'eye_socket_l_bind', 'lid_upper_l_00_bind', 'lid_upper_l_01_bind', 'lid_upper_l_02_bind', 'lid_upper_l_03_bind', 'lid_upper_l_04_bind', 'lid_upper_l_05_bind', 'lid_upper_l_06_bind', 'lid_upper_l_07_bind', 'lid_upper_l_08_bind', 'lid_upper_l_09_bind', 'lid_upper_l_10_bind', 'lid_upper_l_11_bind', 'lid_upper_l_12_bind', 'lid_upper_l_13_bind', 'lid_upper_l_14_bind', 'lid_upper_l_15_bind', 'lid_upper_l_16_bind', 'lid_lower_l_00_bind', 'lid_lower_l_01_bind', 'lid_lower_l_02_bind', 'lid_lower_l_03_bind', 'lid_lower_l_04_bind', 'lid_lower_l_05_bind', 'lid_lower_l_06_bind', 'lid_lower_l_07_bind', 'lid_lower_l_08_bind', 'lid_lower_l_09_bind', 'lid_lower_l_10_bind', 'lid_lower_l_11_bind', 'lid_lower_l_12_bind', 'lid_lower_l_13_bind', 'lid_lower_l_14_bind', 'lid_lower_l_15_bind', 'lid_lower_l_16_bind', 'eye_socket_r_bind', 'lid_upper_r_00_bind', 'lid_upper_r_01_bind', 'lid_upper_r_02_bind', 'lid_upper_r_03_bind', 'lid_upper_r_04_bind', 'lid_upper_r_05_bind', 'lid_upper_r_06_bind', 'lid_upper_r_07_bind', 'lid_upper_r_08_bind', 'lid_upper_r_09_bind', 'lid_upper_r_10_bind', 'lid_upper_r_11_bind', 'lid_upper_r_12_bind', 'lid_upper_r_13_bind', 'lid_upper_r_14_bind', 'lid_upper_r_15_bind', 'lid_upper_r_16_bind', 'lid_lower_r_00_bind', 'lid_lower_r_01_bind', 'lid_lower_r_02_bind', 'lid_lower_r_03_bind', 'lid_lower_r_04_bind', 'lid_lower_r_05_bind', 'lid_lower_r_06_bind', 'lid_lower_r_07_bind', 'lid_lower_r_08_bind', 'lid_lower_r_09_bind', 'lid_lower_r_10_bind', 'lid_lower_r_11_bind', 'lid_lower_r_12_bind', 'lid_lower_r_13_bind', 'lid_lower_r_14_bind', 'lid_lower_r_15_bind', 'lid_lower_r_16_bind', 'cheek_upper_l_bind', 'cheek_upper_r_bind', 'face_lower_bind', 'jaw_bind', 'cheek_lower_r_bind', 'lip_upper_r_00_bind', 'cheek_lower_l_bind', 'lip_upper_r_01_bind', 'lip_upper_r_02_bind', 'lip_upper_r_03_bind', 'lip_upper_r_04_bind', 'lip_upper_r_05_bind', 'lip_upper_r_06_bind', 'lip_upper_r_07_bind', 'lip_upper_r_08_bind', 'lip_upper_r_09_bind', 'lip_upper_r_10_bind', 'lip_upper_r_11_bind', 'lip_upper_r_12_bind', 'lip_upper_m__bind', 'lip_upper_l_12_bind', 'lip_upper_l_11_bind', 'lip_upper_l_10_bind', 'lip_upper_l_09_bind', 'lip_upper_l_08_bind', 'lip_upper_l_07_bind', 'lip_upper_l_06_bind', 'lip_upper_l_05_bind', 'lip_upper_l_04_bind', 'lip_upper_l_03_bind', 'lip_upper_l_02_bind', 'lip_upper_l_01_bind', 'lip_upper_l_00_bind', 'lip_lower_r_00_bind', 'lip_lower_r_01_bind', 'lip_lower_r_02_bind', 'lip_lower_r_03_bind', 'lip_lower_r_04_bind', 'lip_lower_r_05_bind', 'lip_lower_r_06_bind', 'lip_lower_r_07_bind', 'lip_lower_r_08_bind', 'lip_lower_r_09_bind', 'lip_lower_r_10_bind', 'lip_lower_r_11_bind', 'lip_lower_r_12_bind', 'lip_lower_m__bind', 'lip_lower_l_12_bind', 'lip_lower_l_11_bind', 'lip_lower_l_10_bind', 'lip_lower_l_09_bind', 'lip_lower_l_08_bind', 'lip_lower_l_07_bind', 'lip_lower_l_06_bind', 'lip_lower_l_05_bind', 'lip_lower_l_04_bind', 'lip_lower_l_03_bind', 'lip_lower_l_02_bind', 'lip_lower_l_01_bind', 'lip_lower_l_00_bind', 'nose_brige_bind', 'nose_bind', 'sneer_l_bind', 'nostril_l_bind', 'sneer_r_bind', 'nostril_r_bind', 'cheek_r_bind', 'cheek_l_bind']
DaisyfaceJntList = ['face_bind', 'face_upper_bind', 'brow_l_bind', 'brow_inner_l_bind', 'brow_corrugator_l_bind', 'brow_peak_l_bind', 'brow_r_bind', 'brow_inner_r_bind', 'brow_corrugator_r_bind', 'brow_peak_r_bind', 'eye_socket_l_bind', 'lid_upper_l_00_bind', 'lid_upper_l_01_bind', 'lid_upper_l_02_bind', 'lid_upper_l_03_bind', 'lid_upper_l_04_bind', 'lid_upper_l_05_bind', 'lid_upper_l_06_bind', 'lid_upper_l_07_bind', 'lid_upper_l_08_bind', 'lid_upper_l_09_bind', 'lid_upper_l_10_bind', 'lid_upper_l_11_bind', 'lid_upper_l_12_bind', 'lid_upper_l_13_bind', 'lid_upper_l_14_bind', 'lid_upper_l_15_bind', 'lid_upper_l_16_bind', 'lid_lower_l_00_bind', 'lid_lower_l_01_bind', 'lid_lower_l_02_bind', 'lid_lower_l_03_bind', 'lid_lower_l_04_bind', 'lid_lower_l_05_bind', 'lid_lower_l_06_bind', 'lid_lower_l_07_bind', 'lid_lower_l_08_bind', 'lid_lower_l_09_bind', 'lid_lower_l_10_bind', 'lid_lower_l_11_bind', 'lid_lower_l_12_bind', 'lid_lower_l_13_bind', 'eye_socket_r_bind', 'lid_upper_r_00_bind', 'lid_upper_r_01_bind', 'lid_upper_r_02_bind', 'lid_upper_r_03_bind', 'lid_upper_r_04_bind', 'lid_upper_r_05_bind', 'lid_upper_r_06_bind', 'lid_upper_r_07_bind', 'lid_upper_r_08_bind', 'lid_upper_r_09_bind', 'lid_upper_r_10_bind', 'lid_upper_r_11_bind', 'lid_upper_r_12_bind', 'lid_upper_r_13_bind', 'lid_upper_r_14_bind', 'lid_upper_r_15_bind', 'lid_upper_r_16_bind', 'lid_lower_r_00_bind', 'lid_lower_r_01_bind', 'lid_lower_r_02_bind', 'lid_lower_r_03_bind', 'lid_lower_r_04_bind', 'lid_lower_r_05_bind', 'lid_lower_r_06_bind', 'lid_lower_r_07_bind', 'lid_lower_r_08_bind', 'lid_lower_r_09_bind', 'lid_lower_r_10_bind', 'lid_lower_r_11_bind', 'lid_lower_r_12_bind', 'lid_lower_r_13_bind', 'cheek_upper_l_bind', 'cheek_upper_r_bind', 'face_lower_bind', 'jaw_bind', 'cheek_lower_r_bind', 'lip_upper_r_00_bind', 'cheek_lower_l_bind', 'lip_upper_r_01_bind', 'lip_upper_r_02_bind', 'lip_upper_r_03_bind', 'lip_upper_r_04_bind', 'lip_upper_r_05_bind', 'lip_upper_r_06_bind', 'lip_upper_r_07_bind', 'lip_upper_r_08_bind', 'lip_upper_r_09_bind', 'lip_upper_r_10_bind', 'lip_upper_r_11_bind', 'lip_upper_r_12_bind', 'lip_upper_m__bind', 'lip_upper_l_12_bind', 'lip_upper_l_11_bind', 'lip_upper_l_10_bind', 'lip_upper_l_09_bind', 'lip_upper_l_08_bind', 'lip_upper_l_07_bind', 'lip_upper_l_06_bind', 'lip_upper_l_05_bind', 'lip_upper_l_04_bind', 'lip_upper_l_03_bind', 'lip_upper_l_02_bind', 'lip_upper_l_01_bind', 'lip_upper_l_00_bind', 'lip_lower_r_00_bind', 'lip_lower_r_01_bind', 'lip_lower_r_02_bind', 'lip_lower_r_03_bind', 'lip_lower_r_04_bind', 'lip_lower_r_05_bind', 'lip_lower_r_06_bind', 'lip_lower_r_07_bind', 'lip_lower_r_08_bind', 'lip_lower_r_09_bind', 'lip_lower_r_10_bind', 'lip_lower_r_11_bind', 'lip_lower_r_12_bind', 'lip_lower_m__bind', 'lip_lower_l_12_bind', 'lip_lower_l_11_bind', 'lip_lower_l_10_bind', 'lip_lower_l_09_bind', 'lip_lower_l_08_bind', 'lip_lower_l_07_bind', 'lip_lower_l_06_bind', 'lip_lower_l_05_bind', 'lip_lower_l_04_bind', 'lip_lower_l_03_bind', 'lip_lower_l_02_bind', 'lip_lower_l_01_bind', 'lip_lower_l_00_bind', 'nose_brige_bind', 'nose_bind', 'sneer_l_bind', 'nostril_l_bind', 'sneer_r_bind', 'nostril_r_bind', 'cheek_r_bind', 'cheek_l_bind', 'lid_upper_l_17_bind', 'lid_upper_l_18_bind', 'lid_upper_l_19_bind', 'lid_upper_r_19_bind', 'lid_upper_r_18_bind', 'lid_upper_r_17_bind'] #


lashGeo = 'lash'
lidJntList = ['lid_lower_l_16_bind', 'lid_lower_l_15_bind', 'lid_lower_l_14_bind', 'lid_lower_l_13_bind', 'lid_lower_l_12_bind', 'lid_lower_l_11_bind', 'lid_lower_l_10_bind', 'lid_lower_l_09_bind', 'lid_lower_l_08_bind', 'lid_lower_l_07_bind', 'lid_lower_l_06_bind', 'lid_lower_l_05_bind', 'lid_lower_l_04_bind', 'lid_lower_l_03_bind', 'lid_lower_l_02_bind', 'lid_lower_l_01_bind', 'lid_lower_l_00_bind', 'lid_upper_l_16_bind', 'lid_upper_l_15_bind', 'lid_upper_l_14_bind', 'lid_upper_l_13_bind', 'lid_upper_l_12_bind', 'lid_upper_l_11_bind', 'lid_upper_l_10_bind', 'lid_upper_l_09_bind', 'lid_upper_l_08_bind', 'lid_upper_l_07_bind', 'lid_upper_l_06_bind', 'lid_upper_l_05_bind', 'lid_upper_l_04_bind', 'lid_upper_l_03_bind', 'lid_upper_l_02_bind', 'lid_upper_l_01_bind', 'lid_upper_l_00_bind', 'lid_upper_r_00_bind', 'lid_upper_r_01_bind', 'lid_upper_r_02_bind', 'lid_upper_r_03_bind', 'lid_upper_r_04_bind', 'lid_upper_r_05_bind', 'lid_upper_r_06_bind', 'lid_upper_r_07_bind', 'lid_upper_r_08_bind', 'lid_upper_r_09_bind', 'lid_upper_r_10_bind', 'lid_upper_r_11_bind', 'lid_upper_r_12_bind', 'lid_upper_r_13_bind', 'lid_upper_r_14_bind', 'lid_upper_r_15_bind', 'lid_upper_r_16_bind', 'lid_lower_r_00_bind', 'lid_lower_r_01_bind', 'lid_lower_r_02_bind', 'lid_lower_r_03_bind', 'lid_lower_r_04_bind', 'lid_lower_r_05_bind', 'lid_lower_r_06_bind', 'lid_lower_r_07_bind', 'lid_lower_r_08_bind', 'lid_lower_r_09_bind', 'lid_lower_r_10_bind', 'lid_lower_r_11_bind', 'lid_lower_r_12_bind', 'lid_lower_r_13_bind', 'lid_lower_r_14_bind', 'lid_lower_r_15_bind', 'lid_lower_r_16_bind']

browGeo = 'brow'
browJntList = ['brow_l_bind', 'brow_inner_l_bind', 'brow_corrugator_l_bind', 'brow_peak_l_bind', 'brow_r_bind', 'brow_inner_r_bind', 'brow_corrugator_r_bind', 'brow_peak_r_bind']

eyeRGeo = ['eye_r_base', 'eye_r_cover', 'eye_r_halo']
eyeLGeo = ['eye_l_base', 'eye_l_cover', 'eye_l_halo']
eyeRBind = 'eye_r_bind'
eyeLBind = 'eye_l_bind'

upperTeethGeo =['Daisy_up_ence','Daisy_up_teeth']
lowerTeethGeo = ['Daisy_dw_ence','Daisy_dw_teeth']
upperTeethBind = 'teeth_upper_bind'
lowerTeethBind = 'teeth_lower_bind'

toungue = 'Daisy_toungue'
toungueBind = ['tongue_01_bind', 'tongue_02_bind', 'tongue_03_bind', 'tongue_04_bind', 'tongue_05_bind', 'tongue_06_bind', 'tongue_07_bind']

hairGeo = ['hair_white','hair_dark']
faceUpperBind = 'face_upper_bind' 

dressGeo = ['dress_hi', 'dress_lo', 'dress_extrude']
dressBind = ['Chest_M', 'Scapula_L', 'Scapula_R', 'Spine1Part2_M', 'Spine1Part1_M', 'Spine1_M', 'RootPart2_M', 'RootPart1_M', 'Root_M', 'Hip_R', 'Hip_L', 'HipPart1_R', 'HipPart1_L'] #

jacketGeo = ['jacket_lo', 'jacket_mid', 'jacket_hi']
jacketBind = ['Neck_M', 'Chest_M', 'Scapula_R', 'Shoulder_R', 'ShoulderPart1_R', 'ShoulderPart2_R', 'Elbow_R', 'ElbowPart1_R', 'ElbowPart2_R', 'Wrist_R'] #

DaisyDressBind = ['Root_M', 'Hip_R', 'HipPart1_R', 'RootPart1_M', 'RootPart2_M', 'Spine1_M', 'Spine1Part1_M', 'Spine1Part2_M', 'Chest_M', 'Neck_M', 'NeckPart1_M', 'Scapula_R', 'Shoulder_R', 'ShoulderPart1_R', 'ShoulderPart2_R', 'Elbow_R', 'ElbowPart1_R', 'ElbowPart2_R', 'Wrist_R', 'Scapula_L', 'Shoulder_L', 'ShoulderPart1_L', 'ShoulderPart2_L', 'Elbow_L', 'ElbowPart1_L', 'ElbowPart2_L', 'Wrist_L', 'Hip_L', 'HipPart1_L'] #
cmds.select(DaisyDressBind,add=True)
#########################################################################################
#bind jacket
for geo in jacketGeo:
    cmds.skinCluster(jacketBind,geo,tsb=True,mi=4,sm=1)

#bind face
cmds.select(DaisyfaceJntList,faceGeo)
cmds.skinCluster(tsb=True,mi=4,sm=1)

#bind lash
cmds.select(lidJntList,lashGeo)
cmds.skinCluster(tsb=True,mi=2,sm=1)

#bind brow
cmds.select(browGeo,browJntList)
cmds.skinCluster(tsb=True,mi=4,sm=1)

#bind eyes
for geo in eyeRGeo:
    cmds.skinCluster(eyeRBind,geo,tsb=True,mi=1,sm=0)
for geo in eyeLGeo:
    cmds.skinCluster(eyeLBind,geo,tsb=True,mi=1,sm=0)

#bind teeth
for geo in upperTeethGeo:
    cmds.skinCluster(upperTeethBind,geo,tsb=True,mi=1,sm=0)
for geo in lowerTeethGeo:
    cmds.skinCluster(lowerTeethBind,geo,tsb=True,mi=1,sm=0)

#bind toungue
cmds.select(toungue,toungueBind)
cmds.skinCluster(tsb=True,mi=3)

#bind hair
for geo in hairGeo:
    cmds.skinCluster(faceUpperBind,geo,tsb=True,mi=1,sm=0)