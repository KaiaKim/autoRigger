import maya.api.OpenMaya as om
import maya.cmds as cmds

TRANSFORM_NODETYPES = ["transform", "joint"]

def has_non_default_locked_attributes(node):
    locked_attributes = []
    for attribute in ["translate", "rotate", "scale", "jointOrient"]:
        default_value = 1 if attribute == "scale" else 0
        for axis in "XYZ":
            if cmds.attributeQuery(attribute + axis, node=node, exists=True):
                attribute_name = "{}.{}{}".format(node, attribute, axis)
                current_value = cmds.getAttr(attribute_name)
                if cmds.getAttr(attribute_name, lock=True) and current_value != default_value:
                    return True


def reset_transforms(node):
    for attribute in ["translate", "rotate", "scale", "jointOrient"]:
        value = 1 if attribute == "scale" else 0
        for axis in "XYZ":
            if cmds.attributeQuery(attribute + axis, node=node, exists=True):
                attribute_name = "{}.{}{}".format(node, attribute, axis)
                if not cmds.getAttr(attribute_name, lock=True):
                    cmds.setAttr(attribute_name, value)


def bake_transform_to_offset_parent_matrix(node):
    if cmds.nodeType(node) not in TRANSFORM_NODETYPES:
        raise ValueError("Node {} is not a transform node".format(node))

    if has_non_default_locked_attributes(node):
        raise RuntimeError("Node {} has at least one non default locked attribute(s)".format(node))

    local_matrix = om.MMatrix(cmds.xform(node, q=True, m=True, ws=False))
    offset_parent_matrix = om.MMatrix(cmds.getAttr(node + ".offsetParentMatrix"))
    baked_matrix = local_matrix * offset_parent_matrix
    cmds.setAttr(node + ".offsetParentMatrix", baked_matrix, type="matrix")

    reset_transforms(node)

def bake_transform_to_offset_parent_matrix_selection():
    for node in cmds.ls(sl=True):
        bake_transform_to_offset_parent_matrix(node)
###
if __name__ == "__main__":
    bake_transform_to_offset_parent_matrix_selection()
    
