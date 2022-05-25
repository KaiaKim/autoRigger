import maya.cmds as cmds

#cmds.ls(sl=True)

faceGeo = 'face'
faceJntList = ['face_bind', 'face_upper_bind', 'brow_l_bind', 'brow_inner_l_bind', 'brow_corrugator_l_bind', 'brow_peak_l_bind', 'brow_r_bind', 'brow_inner_r_bind', 'brow_corrugator_r_bind', 'brow_peak_r_bind', 'eye_socket_l_bind', 'lid_upper_l_00_bind', 'lid_upper_l_01_bind', 'lid_upper_l_02_bind', 'lid_upper_l_03_bind', 'lid_upper_l_04_bind', 'lid_upper_l_05_bind', 'lid_upper_l_06_bind', 'lid_upper_l_07_bind', 'lid_upper_l_08_bind', 'lid_upper_l_09_bind', 'lid_upper_l_10_bind', 'lid_upper_l_11_bind', 'lid_upper_l_12_bind', 'lid_upper_l_13_bind', 'lid_upper_l_14_bind', 'lid_upper_l_15_bind', 'lid_upper_l_16_bind', 'lid_lower_l_00_bind', 'lid_lower_l_01_bind', 'lid_lower_l_02_bind', 'lid_lower_l_03_bind', 'lid_lower_l_04_bind', 'lid_lower_l_05_bind', 'lid_lower_l_06_bind', 'lid_lower_l_07_bind', 'lid_lower_l_08_bind', 'lid_lower_l_09_bind', 'lid_lower_l_10_bind', 'lid_lower_l_11_bind', 'lid_lower_l_12_bind', 'lid_lower_l_13_bind', 'lid_lower_l_14_bind', 'lid_lower_l_15_bind', 'lid_lower_l_16_bind', 'eye_socket_r_bind', 'lid_upper_r_00_bind', 'lid_upper_r_01_bind', 'lid_upper_r_02_bind', 'lid_upper_r_03_bind', 'lid_upper_r_04_bind', 'lid_upper_r_05_bind', 'lid_upper_r_06_bind', 'lid_upper_r_07_bind', 'lid_upper_r_08_bind', 'lid_upper_r_09_bind', 'lid_upper_r_10_bind', 'lid_upper_r_11_bind', 'lid_upper_r_12_bind', 'lid_upper_r_13_bind', 'lid_upper_r_14_bind', 'lid_upper_r_15_bind', 'lid_upper_r_16_bind', 'lid_lower_r_00_bind', 'lid_lower_r_01_bind', 'lid_lower_r_02_bind', 'lid_lower_r_03_bind', 'lid_lower_r_04_bind', 'lid_lower_r_05_bind', 'lid_lower_r_06_bind', 'lid_lower_r_07_bind', 'lid_lower_r_08_bind', 'lid_lower_r_09_bind', 'lid_lower_r_10_bind', 'lid_lower_r_11_bind', 'lid_lower_r_12_bind', 'lid_lower_r_13_bind', 'lid_lower_r_14_bind', 'lid_lower_r_15_bind', 'lid_lower_r_16_bind', 'cheek_upper_l_bind', 'cheek_upper_r_bind', 'face_lower_bind', 'jaw_bind', 'cheek_lower_r_bind', 'lip_upper_r_00_bind', 'cheek_lower_l_bind', 'lip_upper_r_01_bind', 'lip_upper_r_02_bind', 'lip_upper_r_03_bind', 'lip_upper_r_04_bind', 'lip_upper_r_05_bind', 'lip_upper_r_06_bind', 'lip_upper_r_07_bind', 'lip_upper_r_08_bind', 'lip_upper_r_09_bind', 'lip_upper_r_10_bind', 'lip_upper_r_11_bind', 'lip_upper_r_12_bind', 'lip_upper_m__bind', 'lip_upper_l_12_bind', 'lip_upper_l_11_bind', 'lip_upper_l_10_bind', 'lip_upper_l_09_bind', 'lip_upper_l_08_bind', 'lip_upper_l_07_bind', 'lip_upper_l_06_bind', 'lip_upper_l_05_bind', 'lip_upper_l_04_bind', 'lip_upper_l_03_bind', 'lip_upper_l_02_bind', 'lip_upper_l_01_bind', 'lip_upper_l_00_bind', 'lip_lower_r_00_bind', 'lip_lower_r_01_bind', 'lip_lower_r_02_bind', 'lip_lower_r_03_bind', 'lip_lower_r_04_bind', 'lip_lower_r_05_bind', 'lip_lower_r_06_bind', 'lip_lower_r_07_bind', 'lip_lower_r_08_bind', 'lip_lower_r_09_bind', 'lip_lower_r_10_bind', 'lip_lower_r_11_bind', 'lip_lower_r_12_bind', 'lip_lower_m__bind', 'lip_lower_l_12_bind', 'lip_lower_l_11_bind', 'lip_lower_l_10_bind', 'lip_lower_l_09_bind', 'lip_lower_l_08_bind', 'lip_lower_l_07_bind', 'lip_lower_l_06_bind', 'lip_lower_l_05_bind', 'lip_lower_l_04_bind', 'lip_lower_l_03_bind', 'lip_lower_l_02_bind', 'lip_lower_l_01_bind', 'lip_lower_l_00_bind', 'nose_brige_bind', 'nose_bind', 'sneer_l_bind', 'nostril_l_bind', 'sneer_r_bind', 'nostril_r_bind', 'cheek_r_bind', 'cheek_l_bind']

lashGeo = 'lash'
lidJntList = ['lid_lower_l_16_bind', 'lid_lower_l_15_bind', 'lid_lower_l_14_bind', 'lid_lower_l_13_bind', 'lid_lower_l_12_bind', 'lid_lower_l_11_bind', 'lid_lower_l_10_bind', 'lid_lower_l_09_bind', 'lid_lower_l_08_bind', 'lid_lower_l_07_bind', 'lid_lower_l_06_bind', 'lid_lower_l_05_bind', 'lid_lower_l_04_bind', 'lid_lower_l_03_bind', 'lid_lower_l_02_bind', 'lid_lower_l_01_bind', 'lid_lower_l_00_bind', 'lid_upper_l_16_bind', 'lid_upper_l_15_bind', 'lid_upper_l_14_bind', 'lid_upper_l_13_bind', 'lid_upper_l_12_bind', 'lid_upper_l_11_bind', 'lid_upper_l_10_bind', 'lid_upper_l_09_bind', 'lid_upper_l_08_bind', 'lid_upper_l_07_bind', 'lid_upper_l_06_bind', 'lid_upper_l_05_bind', 'lid_upper_l_04_bind', 'lid_upper_l_03_bind', 'lid_upper_l_02_bind', 'lid_upper_l_01_bind', 'lid_upper_l_00_bind', 'lid_upper_r_00_bind', 'lid_upper_r_01_bind', 'lid_upper_r_02_bind', 'lid_upper_r_03_bind', 'lid_upper_r_04_bind', 'lid_upper_r_05_bind', 'lid_upper_r_06_bind', 'lid_upper_r_07_bind', 'lid_upper_r_08_bind', 'lid_upper_r_09_bind', 'lid_upper_r_10_bind', 'lid_upper_r_11_bind', 'lid_upper_r_12_bind', 'lid_upper_r_13_bind', 'lid_upper_r_14_bind', 'lid_upper_r_15_bind', 'lid_upper_r_16_bind', 'lid_lower_r_00_bind', 'lid_lower_r_01_bind', 'lid_lower_r_02_bind', 'lid_lower_r_03_bind', 'lid_lower_r_04_bind', 'lid_lower_r_05_bind', 'lid_lower_r_06_bind', 'lid_lower_r_07_bind', 'lid_lower_r_08_bind', 'lid_lower_r_09_bind', 'lid_lower_r_10_bind', 'lid_lower_r_11_bind', 'lid_lower_r_12_bind', 'lid_lower_r_13_bind', 'lid_lower_r_14_bind', 'lid_lower_r_15_bind', 'lid_lower_r_16_bind']

eyeRGeo = ['eye_r_base', 'eye_r_cover', 'eye_r_halo']
eyeLGeo = ['eye_l_base', 'eye_l_cover', 'eye_l_halo']
eyeRBind = 'eye_r_bind'
eyeLBind = 'eye_l_bind'

upperTeethGeo = ['Gabi_geo_up_teeth01', 'Gabi_geo_up_teeth02', 'Gabi_geo_up_teeth06', 'Gabi_geo_up_teeth07', 'Gabi_geo_up_teeth11', 'Gabi_geo_up_teeth12', 'Gabi_geo_up_ence', 'Gabi_geo_up_teeth04', 'Gabi_geo_up_teeth05'] 
lowerTeethGeo = ['Gabi_geo_dw_teeth01', 'Gabi_geo_dw_teeth02', 'Gabi_geo_dw_teeth03', 'Gabi_geo_dw_teeth06', 'Gabi_geo_dw_teeth07', 'Gabi_geo_dw_teeth08', 'Gabi_geo_dw_teeth09', 'Gabi_geo_dw_teeth12', 'Gabi_geo_dw_teeth13', 'Gabi_geo_dw_teeth14', 'Gabi_geo_dw_ence', 'Gabi_geo_dw_teeth10'] #
upperTeethBind = 'teeth_upper_bind'
lowerTeethBind = 'teeth_lower_bind'

hairGeo = ['hair_white','hair_dark']
faceUpperBind = 'face_upper_bind' 

#########################################################################################

#bind face
cmds.select(faceJntList,faceGeo)
cmds.skinCluster(tsb=True,mi=4,sm=1)

#bind lash
cmds.select(lidJntList,lashGeo)
cmds.skinCluster(tsb=True,mi=2,sm=1)

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
cmds.skinCluster(lowerTeethBind,'Gabi_toungue',tsb=True,mi=1)

#bind
for geo in hairGeo:
    cmds.skinCluster(faceUpperBind,geo,tsb=True,mi=1,sm=0)