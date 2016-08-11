# This function will "undo" the roll used in ik
#   The ik roll will be set to 0, and the ik control 
#   will be moved to the appropriate location so that 
#   the pose will be identical
# We may assume:
#  1) We are in pose mode
#  2) The current bone is the ik control
#  3) The name of the ik roll is "finger-ik-roll.R" (or ".L")
#  4) The name of the last non-roll ik bone is "MCH-finger-ik.R.008" (or ".L.")

import bpy
from bpy import context
import mathutils
import math

# get ik target
ik_target = bpy.context.active_pose_bone

# get the corresponding object and armature data
obj = ik_target.id_data
armature = obj.pose

# find out which finger we are controlling
side = ik_target.name[-1]
    
# get ik roll and final location (pose coordinates)
ik_roll = armature.bones['finger-ik-roll.' + side]
final = armature.bones['MCH-finger-ik.' + side + '.008']

# move ik target to desired position
ik_target.matrix = final.matrix

# rotate to accomodate for offset
vector = mathutils.Vector((ik_target.matrix[0][0],ik_target.matrix[0][1],ik_target.matrix[0][2]))
bpy.ops.transform.rotate(
  value=math.pi/2, 
  axis=vector, 
  constraint_axis=(True, False, False), 
  constraint_orientation='LOCAL')

# reset roll
ik_roll.rotation_euler[0] = 0

