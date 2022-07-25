import maya.cmds as cmds

#mc.ls(sl=True)

#button for select bind joints
#template names + lid jnts + lip jnts
eyeGeo = 'eyes'
eyeBind = 'Eye_R','Eye_L'

dressGeo = ['dress_hi', 'dress_lo', 'dress_extrude']
dressBind = ['Chest_M', 'Scapula_L', 'Scapula_R', 'Spine1Part2_M', 'Spine1Part1_M', 'Spine1_M', 'RootPart2_M', 'RootPart1_M', 'Root_M', 'Hip_R', 'Hip_L', 'HipPart1_R', 'HipPart1_L'] #

jacketGeo = ['jacket_lo', 'jacket_mid', 'jacket_hi']
jacketBind = ['Neck_M', 'Chest_M', 'Scapula_R', 'Shoulder_R', 'ShoulderPart1_R', 'ShoulderPart2_R', 'Elbow_R', 'ElbowPart1_R', 'ElbowPart2_R', 'Wrist_R'] #

DaisyDressBind = ['Root_M', 'Hip_R', 'HipPart1_R', 'RootPart1_M', 'RootPart2_M', 'Spine1_M', 'Spine1Part1_M', 'Spine1Part2_M', 'Chest_M', 'Neck_M', 'NeckPart1_M', 'Scapula_R', 'Shoulder_R', 'ShoulderPart1_R', 'ShoulderPart2_R', 'Elbow_R', 'ElbowPart1_R', 'ElbowPart2_R', 'Wrist_R', 'Scapula_L', 'Shoulder_L', 'ShoulderPart1_L', 'ShoulderPart2_L', 'Elbow_L', 'ElbowPart1_L', 'ElbowPart2_L', 'Wrist_L', 'Hip_L', 'HipPart1_L'] #
DaisydressGeo = ['dress_mid','dress_lo','dress_extrude']
#########################################################################################
#bind jacket
for geo in jacketGeo:
    mc.skinCluster(jacketBind,geo,tsb=True,mi=4,sm=1)

#bind face
mc.select(DaisyfaceJntList,faceGeo)
mc.skinCluster(tsb=True,mi=4,sm=1)

#bind lash
mc.select(lidJntList,lashGeo)
mc.skinCluster(tsb=True,mi=2,sm=1)

#bind brow
mc.select(browGeo,browJntList)
mc.skinCluster(tsb=True,mi=4,sm=1)

#bind eyes
for geo in eyeRGeo:
    mc.skinCluster(eyeRBind,geo,tsb=True,mi=1,sm=0)
for geo in eyeLGeo:
    mc.skinCluster(eyeLBind,geo,tsb=True,mi=1,sm=0)

#bind teeth
for geo in upperTeethGeo:
    mc.skinCluster(upperTeethBind,geo,tsb=True,mi=1,sm=0)
for geo in lowerTeethGeo:
    mc.skinCluster(lowerTeethBind,geo,tsb=True,mi=1,sm=0)

#bind toungue
mc.select(toungue,toungueBind)
mc.skinCluster(tsb=True,mi=3)

#bind hair
for geo in hairGeo:
    mc.skinCluster(faceUpperBind,geo,tsb=True,mi=1,sm=0)
    
#bind dress
for geo in dressGeo:
    mc.skinCluster(dressBind,geo,tsb=True,mi=4,sm=0)
