import maya.cmds as cmds
from functools import partial

###------------------------------------------Global Variables-------------------------------------------------



###---------------------------------------------Function------------------------------------------------------
def createWindow(arg1):
    #test to see if the window exists
    if cmds.window(arg1.winName, exists=True):
        cmds.deleteUI(arg1.winName) #we don't want to create extra windows

    cmds.window(arg1.winName, title=arg1.winTitle) #create a new window
    cmds.scrollLayout( 'scorllLayout', width=320) #makes your entire layout scrollable #first - main layout
    cmds.columnLayout( adjustableColumn=True ) #second layout - attaches to the main layout
    ###
    cmds.frameLayout( l='Model Prepare', collapsable=True, collapse=True)
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
    cmds.button(l='Quick Test Data',c=arg1.quickTest )

    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=2)
    
    cmds.gridLayout(numberOfColumns=1,cellWidthHeight=(100, 20))
    cmds.text(l='Head Verts')
    cmds.text( l='Upper Lip Verts')
    cmds.text( l='Lower Lip Verts')
    cmds.text( l='Upper R Eye Verts')
    cmds.text( l='Lower R Eye Verts')
    cmds.text( l='R Brow Vert')
    cmds.setParent('..')
    
    cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(66, 20) ) #fourth layout - frame layout
    
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('head','ass') )
    cmds.button( l='select', c=lambda _:arg1.assignDelete('head','sel') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('head','del') )
    
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('lipUpper','ass') )
    cmds.button( l='select', c=lambda _:arg1.assignDelete('lipUpper','sel') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('lipUpper','del') )
    
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('lipLower','ass') )
    cmds.button( l='select', c=lambda _:arg1.assignDelete('lipLower','sel') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('lipLower','del') )
    
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('lidUpperR','ass') )
    cmds.button( l='select', c=lambda _:arg1.assignDelete('lidUpperR','sel') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('lidUpperR','del') )
    
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('lidLowerR','ass') )
    cmds.button( l='select', c=lambda _:arg1.assignDelete('lidLowerR','sel') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('lidLowerR','del') )
    
    cmds.button( l='assign', c=lambda _:arg1.assignDelete('browR','ass') )
    cmds.button( l='select', c=lambda _:arg1.assignDelete('browR','sel') )
    cmds.button( l='delete', c=lambda _:arg1.assignDelete('browR','del') )
    
    cmds.setParent('..')
    
    cmds.setParent('..')
    
    cmds.setParent('..')
    
    ###
    cmds.frameLayout( l='Build', collapsable=True, collapse=False)
    cmds.columnLayout( rowSpacing = 10 )
    
    cmds.button(l='Set Rig Names',c=arg1.names)
    
    cmds.button(l='Build Face Rig 01',c=arg1.buildRig01)
    
    cmds.rowLayout(numberOfColumns=4)
    cmds.text( l='Ctrl orients: ')
    cmds.button( l='mirror R to L', c=lambda _:arg1.orientData('mirror'))
    cmds.button( l='save', c=lambda _:arg1.orientData('save'))
    cmds.button( l='load', c=lambda _:arg1.orientData('load'))
    cmds.setParent('..')
    
    cmds.button(l='Build Face Rig 02',c=arg1.buildRig02)
    
    cmds.setParent('..')
    cmds.setParent('..')
    ###
    cmds.frameLayout( l='Adjust', collapsable=True, collapse=False)
    cmds.columnLayout( rowSpacing = 5 )
    
    cmds.rowLayout(numberOfColumns=3)
    cmds.text( l ='Edit Orient Mode: ')
    cmds.button( l='Enter', c=arg1.enterOrientEdit)
    cmds.button( l='Exit', c=arg1.exitOrientEdit)
    cmds.setParent('..')
    
    cmds.text( l='BlendShape Curve: ')
    cmds.rowLayout(numberOfColumns=4)
    cmds.button( l='mirror Mouth', c=arg1.mirrorBlendCrvMouth)
    cmds.button( l='mirror Eyes', c=arg1.mirrorBlendCrvEyes)
    cmds.button( l='save', c=lambda _:arg1.blendCrvData('save'))
    cmds.button( l='load', c=lambda _:arg1.blendCrvData('load'))
    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=2)
    cmds.text( l='Normalize (Scale ctrl oreint): ')
    cmds.button(l='Normalize')
    cmds.setParent('..')

    cmds.setParent('..')
    cmds.setParent('..')
    ###
    #cmds.frameLayout( l='Extra', collapsable=True, collapse=False)
    #cmds.columnLayout( rowSpacing = 10 )


    cmds.showWindow()
    
###---------------------------------------------------------------------------
