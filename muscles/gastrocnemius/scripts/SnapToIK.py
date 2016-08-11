# This will snap the FK bones to the IK orientations
#  We may assume that the ik target is selected in pose mode

import bpy

# get the ik target
ik_target = bpy.context.active_pose_bone

# get the corresponding armature
armature = ik_target.id_data.pose

# find out which finger we are controlling
side = ik_target.name[-1]

# move all FK bones to the current IK orientation
for bone in armature.bones:
    if "MCH-finger-fk." + side in bone.name:
        ik_name = bone.name[:11] + "ik" + bone.name[13:]
        ik_bone = armature.bones[ik_name]
        bpy.ops.pose.visual_transform_apply()
        bone.matrix = ik_bone.matrix