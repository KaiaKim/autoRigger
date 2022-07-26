import maya.api.OpenMaya as om
import maya.cmds as mc

TRANSFORM_NODETYPES = ["transform", "joint"]

def has_non_default_locked_attributes(node):
    locked_attributes = []
    for attribute in ["translate", "rotate", "scale", "jointOrient"]:
        default_value = 1 if attribute == "scale" else 0
        for axis in "XYZ":
            if mc.attributeQuery(attribute + axis, node=node, exists=True):
                attribute_name = "{}.{}{}".format(node, attribute, axis)
                current_value = mc.getAttr(attribute_name)
                if mc.getAttr(attribute_name, lock=True) and current_value != default_value:
                    return True


def reset_transforms(node):
    for attribute in ["translate", "rotate", "scale", "jointOrient"]:
        value = 1 if attribute == "scale" else 0
        for axis in "XYZ":
            if mc.attributeQuery(attribute + axis, node=node, exists=True):
                attribute_name = "{}.{}{}".format(node, attribute, axis)
                if not mc.getAttr(attribute_name, lock=True):
                    mc.setAttr(attribute_name, value)


def bake_transform_to_offset_parent_matrix(node):
    if mc.nodeType(node) not in TRANSFORM_NODETYPES:
        raise ValueError("Node {} is not a transform node".format(node))

    if has_non_default_locked_attributes(node):
        raise RuntimeError("Node {} has at least one non default locked attribute(s)".format(node))

    local_matrix = om.MMatrix(mc.xform(node, q=True, m=True, ws=False))
    offset_parent_matrix = om.MMatrix(mc.getAttr(node + ".offsetParentMatrix"))
    baked_matrix = local_matrix * offset_parent_matrix
    mc.setAttr(node + ".offsetParentMatrix", baked_matrix, type="matrix")

    reset_transforms(node)

def bake_transform_to_offset_parent_matrix_selection():
    for node in mc.ls(sl=True):
        bake_transform_to_offset_parent_matrix(node)
###
if __name__ == "__main__":
    bake_transform_to_offset_parent_matrix_selection()
    
