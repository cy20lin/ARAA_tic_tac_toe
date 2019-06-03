#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Pose
import moveit_commander
import moveit_msgs.msg
from moveit_commander.conversions import pose_to_list

# Set the movement points.
def setting_section():

    # Center
    section_center = Pose()
    section_center.position.x = 0.45662
    section_center.position.y = 0.00105
    section_center.position.z = 0.05658
    section_center.orientation.w = 0.70125
    section_center.orientation.x = 2.75400954078e-05
    section_center.orientation.y = 0.71291
    section_center.orientation.z = -2.78400837859e-05

    # Section 1
    section_1 = Pose()
    section_1.position.x = 0.55711
    section_1.position.y = 0.10371
    section_1.position.z = section_center.position.z
    section_1.orientation.w = section_center.orientation.w
    section_1.orientation.x = section_center.orientation.x
    section_1.orientation.y = section_center.orientation.y
    section_1.orientation.z = section_center.orientation.z

    # Section 2
    section_2 = Pose()
    section_2.position.x = 0.55772
    section_2.position.y = 0.00105
    section_2.position.z = section_center.position.z
    section_2.orientation.w = section_center.orientation.w
    section_2.orientation.x = section_center.orientation.x
    section_2.orientation.y = section_center.orientation.y
    section_2.orientation.z = section_center.orientation.z

    # Section 3
    section_3 = Pose()
    section_3.position.x = 0.556615301837
    section_3.position.y = -0.113541598836
    section_3.position.z = section_center.position.z
    section_3.orientation.w = 0.701419382572
    section_3.orientation.x = 0.000251295300121
    section_3.orientation.y = 0.712748728062
    section_3.orientation.z = 0.000193001011865

    # Section 4
    section_4 = Pose()
    section_4.position.x = 0.456566052554
    section_4.position.y = 0.093843055923
    section_4.position.z = section_center.position.z
    section_4.orientation.w = 0.700945986292
    section_4.orientation.x = 0.000617939007431
    section_4.orientation.y = 0.713214088149
    section_4.orientation.z = 8.31769073599e-05

    # Section 6
    section_6 = Pose()
    section_6.position.x = 0.456567619194
    section_6.position.y = -0.108510988498
    section_6.position.z = section_center.position.z
    section_6.orientation.w = 0.700961312937
    section_6.orientation.x = 0.000626350361852
    section_6.orientation.y = 0.713199019497
    section_6.orientation.z = 6.35504255371e-05

    # Section 7
    section_7 = Pose()
    section_7.position.x = 0.356312306248
    section_7.position.y = 0.095512752144
    section_7.position.z = section_center.position.z
    section_7.orientation.w = 0.701404510033
    section_7.orientation.x = -0.00486289712165
    section_7.orientation.y = 0.712746325349
    section_7.orientation.z = -0.000860952758976

    # Section 8
    section_8 = Pose()
    section_8.position.x = 0.356312306248
    section_8.position.y = -0.015512752144
    section_8.position.z = section_center.position.z
    section_8.orientation.w = 0.701391533838
    section_8.orientation.x = -0.00486289712165
    section_8.orientation.y = 0.712759200663
    section_8.orientation.z = -0.000881232234046

    # Section 9
    section_9 = Pose()
    section_9.position.x = 0.356318105719
    section_9.position.y = -0.10749740194
    section_9.position.z = section_center.position.z
    section_9.orientation.w = 0.701381600262
    section_9.orientation.x = -0.00486766537702
    section_9.orientation.y = 0.71276885309
    section_9.orientation.z = -0.000847769048651

    # Save it to array.
    section = [section_1, section_2, section_3, section_4, section_center, section_6, section_7 ,section_8, section_9]
    return section

def pose_move(pose):
    # Set start and goal pose.
    group.set_start_state_to_current_state()
    group.set_pose_target(pose)

    # Plan the path.
    plan_success = group.plan()
    rospy.sleep(1.5)

    # Execute the motion trajectory
    if(plan_success):
        rospy.sleep(1)
        group.execute(plan_success, wait=True)

    # Make sure the motion is stop
    group.stop()
    group.clear_pose_targets()
    rospy.sleep(3)

def move_robot(section):
    # Set max velocity and max acceleration of robot moving
    group.set_max_acceleration_scaling_factor(0.01)
    group.set_max_velocity_scaling_factor(0.1)

    # Getting basic information.
    planning_frame = group.get_planning_frame()
    print 'Reference frame: %s' % planning_frame
    eef_link = group.get_end_effector_link()
    print 'End effector: %s' % eef_link
    print 'Robot Groups:', robot.get_group_names()

    # Start testing movement
    pose_move(section[4])
    pose_move(section[0])
    pose_move(section[4])
    pose_move(section[1])
    pose_move(section[4])
    pose_move(section[2])
    pose_move(section[4])
    pose_move(section[3])
    pose_move(section[4])
    pose_move(section[5])
    pose_move(section[4])
    pose_move(section[6])
    pose_move(section[4])
    pose_move(section[7])
    pose_move(section[4])
    pose_move(section[8])
    pose_move(section[4])

# Create a ROS node.
rospy.init_node('ARAA_Test')
rospy.loginfo('Start to move...')

# Initialize moveit_commander.
moveit_commander.roscpp_initialize(sys.argv)
# Instantiate a RobotCommander object.
robot = moveit_commander.RobotCommander()
# Give group_name and instantiate a MoveGroupCommander object.
group_name = 'manipulator'
group = moveit_commander.MoveGroupCommander(group_name)

# Set the movement points and try to follow.
section = setting_section()
move_robot(section)

rospy.loginfo('Done...')
