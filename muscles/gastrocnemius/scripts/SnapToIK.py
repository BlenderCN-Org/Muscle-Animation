# This will snap the FK bones to the IK orientations
#  We may assume that the ik target is selected in pose mode

import bpy

# get the ik target
ik_target = bpy.context.active_pose_bone

# get the corresponding armature
armature = ik_target.id_data.pose

# find out which IK chain we are controlling
if "finger-ik." in ik_target.name:
    ik_id = "MCH-finger-fk." + ik_target.name[-1]
    fk_start = -8
else:
    ik_id = "MCH-tail-fk"
    fk_start = -6


# move all FK bones to the current IK orientation
for bone in armature.bones:
    if ik_id in bone.name:
        ik_name = bone.name[:fk_start] + "ik" + bone.name[fk_start+2:]
        ik_bone = armature.bones[ik_name]
        bpy.ops.pose.visual_transform_apply()
        bone.matrix = ik_bone.matrix