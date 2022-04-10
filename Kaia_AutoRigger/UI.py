import maya.cmds as cmds
from functools import partial

def createWindow(arg1):
    #test to see if the window exists
    if cmds.window(arg1.winName, exists=True):
        cmds.deleteUI(arg1.winName) #we don't want to create extra windows

    cmds.window(arg1.winName, title=arg1.winTitle) #create a new window
    cmds.scrollLayout( 'scorllLayout', width=320) #makes your entire layout scrollable #first - main layout
    cmds.columnLayout( adjustableColumn=True ) #second layout - attaches to the main layout
    ###
    cmds.frameLayout( l='Template', collapsable=True, collapse=False )
    cmds.columnLayout()
    cmds.text(l='Load template files')
    cmds.setParent('..')
    
    cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(150, 20))
    cmds.text( l='Face Bind Joints')
    cmds.button( l='Import',c=lambda x:cmds.file(arg1.mayascripts+'/Kaia_AutoRigger/templateFiles/faceBindJoints.ma',i=True))
    cmds.text( l='Lip Curves')
    cmds.button( l='Import',c=lambda x:cmds.file(arg1.mayascripts+'/Kaia_AutoRigger/templateFiles/lipCurves.ma',i=True))
    cmds.text( l='Eye Curves')
    cmds.button( l='Import',c=lambda x:cmds.file(arg1.mayascripts+'/Kaia_AutoRigger/templateFiles/eyeCurves.ma',i=True))

    cmds.setParent('..')
    cmds.setParent('..')
    ###
    cmds.frameLayout( l='Assign', collapsable=True, collapse=False )

    cmds.columnLayout()
    cmds.text(l='Assign vertices from selection')
    cmds.button(l='Quick Test Data',c=arg1.quickTestData )

    cmds.setParent('..')

    cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(100, 20) ) #fourth layout - frame layout

    cmds.text( l='Upper Lip Verts')
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('arg1.lipUpperVerts','ass') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('arg1.lipUpperVerts','del') )

    cmds.text( l='Lower Lip Verts')
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('arg1.lipLowerVerts','ass') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('arg1.lipLowerVerts','del') )

    cmds.text( l='Upper Eye Verts R')
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('arg1.lidUpperRVerts','ass') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('arg1.lidUpperRVerts','del') )

    cmds.setParent('..')
    cmds.setParent('..')
    ###
    cmds.frameLayout( l='Helper', collapsable=True, collapse=True)
    cmds.columnLayout( rowSpacing = 10 )

    cmds.text( l='! eye cluster name: eye_r_cls')
    cmds.text( l='! eye lattice name: eye_r_ffd1')
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.text(l='eye lattice points: ')
    cmds.button( l='mirror R to L', c=lambda _:arg1.latticeData('mirror'))
    cmds.button( l='save', c=lambda _:arg1.latticeData('save'))
    cmds.button( l='load', c=lambda _:arg1.latticeData('load'))
    cmds.setParent('..')
    
    cmds.setParent('..')
    cmds.setParent('..')
    ###
    cmds.frameLayout( l='Build', collapsable=True, collapse=False)
    cmds.columnLayout( rowSpacing = 10 )
    
    cmds.button(l='Build Mouth Rig 01',c=arg1.buildMouthRig01)
    cmds.button(l='Build Eye Rig 01',c=arg1.buildEyeRig01)
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.text( l='Ctrl orients: ')
    cmds.button( l='mirror R to L', c=lambda _:arg1.orientData('mirror'))
    cmds.button( l='save', c=lambda _:arg1.orientData('save'))
    cmds.button( l='load', c=lambda _:arg1.orientData('load'))
    cmds.setParent('..')
    
    cmds.button(l='Build Mouth Rig 02',c=arg1.buildMouthRig02)
    cmds.button(l='Build Eye Rig 02')
    
    cmds.button(l='Build Mouth Blendshapes 01', c=arg1.BuildMouthBlendshapes01)
    cmds.button(l='Build Eye Blendshapes 01', c=arg1.BuildEyeBlendshapes01)
    
    cmds.rowLayout(numberOfColumns=5)
    cmds.text( l='Blend curv CVs: ')
    cmds.button( l='mirror Mouth', c=arg1.mirrorBlendCrvMouth)
    cmds.button( l='mirror Eyes', c=arg1.mirrorBlendCrvEyes)
    cmds.button( l='save', c=lambda _:arg1.blendCrvData('save'))
    cmds.button( l='load', c=lambda _:arg1.blendCrvData('load'))
    cmds.setParent('..')
    
    cmds.setParent('..')
    cmds.setParent('..')
    ###
    cmds.frameLayout( l='Extra', collapsable=True, collapse=False)
    cmds.columnLayout( rowSpacing = 10 )
    
    cmds.button(l='000: Arrange Groups',c=arg1.arrangeGrps)
    cmds.button(l='select Jaw Bind',c=lambda _:cmds.select(arg1.jawBind))

    cmds.showWindow()