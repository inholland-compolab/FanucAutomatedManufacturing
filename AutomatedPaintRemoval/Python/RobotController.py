"""This module contains the code to control the robot
as well as some utility functions"""

from robolink.robolink import *  # API to communicate with RoboDK
from robodk.robodk import *      # basic matrix operations
from PathPoint import PathPoint
import math as mt
import numpy as np

# Angle Based on Frame
# CylinderFrontTarget
#   - Angle on circle 270.0
#   - Sanding angle   -90.0
# CylinderLeftTarget
#   - Angle on circle 180.0
#   - Sanding angle   180.0
# CylinderBackTarget
#   - Angle on circle 90
#   - Sanding angle   90.0
# CylinderRightTarget
#   - Angle on circle 0
#   - Sanding angle   0.0
#
#             90
#         _.-""""""-._
#       .'            `.
#      /                \
#     |                  |
# 180 |                  | 0
#     |                  |
#      \                /
#       `._          _.'
#          `-......-'
#             270

RADIUS = 134


def calculate_cartesian(angle):
    """Used for calculating the cartesian position of a cylindrical surface"""

    x = RADIUS * mt.cos(angle * (pi / 180))
    y = RADIUS * mt.sin(angle * (pi / 180))

    return x, y


def run_debug_procedure():
    """
    This function was used as a test procedure to test the simulation arm
    on a cylindrical surface.

    :return: nothing
    """
    # Connect to the RoboDK API
    robodk = Robolink()
    robodk.setSimulationSpeed(1)

    # Retrieve specific items
    robot = robodk.Item('Fanuc M-20iA/35M')
    robot.setSpeed(500)
    home_target = robodk.Item('Home')
    cylinder_front_target = robodk.Item('CylinderFrontTarget')

    # Set home_target as approach and goto target
    approach = home_target.Pose()
    robot.MoveL(approach)

    # Set FrontTarget as approach and goto target
    approach = cylinder_front_target.Pose()
    print(approach)
    robot.MoveL(approach)
    # Use FrontTarget as initial start position
    xyzrpw = Pose_2_Fanuc(approach)

    print(xyzrpw)

    # Set speed of robot
    robot.setSpeed(50)

    # set the new middle location based on the angle of the object
    xyzrpw[0], xyzrpw[1] = calculate_cartesian(225.0)
    xyzrpw[5] = 45.0
    # Create approach middle approach
    middle_approach = Fanuc_2_Pose(xyzrpw)
    print(xyzrpw)
    print(middle_approach)

    # set the new end location based on the angle of the object
    xyzrpw[0], xyzrpw[1] = calculate_cartesian(180.0)
    xyzrpw[5] = 0.0
    # Create approach end approach
    final_approach = Fanuc_2_Pose(xyzrpw)
    print(xyzrpw)
    print(final_approach)

    # use a circular movement based on the middle approach and
    # end approach
    robot.MoveC(middle_approach, final_approach)

    # do the same thing as described above but then a different position
    xyzrpw[0], xyzrpw[1] = calculate_cartesian(270.0)
    xyzrpw[5] = 90.0
    middle_approach = Fanuc_2_Pose(xyzrpw)
    print(xyzrpw)
    print(middle_approach)

    xyzrpw[0], xyzrpw[1] = calculate_cartesian(360.0)
    xyzrpw[5] = 180.0
    final_approach = Fanuc_2_Pose(xyzrpw)
    print(xyzrpw)
    print(final_approach)

    robot.MoveC(middle_approach, final_approach)
    robot.setSpeed(500)


def run_procedure(points):
    """
    This function is used to control the arm on a 2d surface in the
    simulation.

    :param PathPoint points: a list of points
    :return:
    """

    # Connect to the RoboDK API
    robodk = Robolink()
    robodk.setSimulationSpeed(1)

    # Create a new robotprogram
    prog = robodk.AddProgram('AutoProgram')

    # Retrieve specific items from the simu
    robot = robodk.Item('Fanuc M-20iA/35M')
    robot.setSpeed(500)

    home_target = robodk.Item('Home')
    near_start_target = robodk.Item('NearStart')
    start_target = robodk.Item('Start')

    # Start at home position first
    approach = home_target.Pose()
    robot.MoveL(approach)

    # goto near_start
    approach = near_start_target.Pose()
    robot.MoveL(approach)
    # Use FrontTarget as initial start position

    # goto start
    approach = start_target.Pose()
    robot.MoveL(approach)

    # Set the middle point of the board
    middle_of_board = np.array([-250 / 2, 140 / 2])

    prevpoint = None

    for i in range(len(points)):
        # Create a new target
        ti = robodk.AddTarget('Auto Target %i' % (i+1))

        xyzrpw = Pose_2_Fanuc(approach)

        """This first if statements check whether the arm needs to
        be moved up or down based on the previous "AllowedToSand" boolean"""
        # Check whether or not this is the first point in the list
        if prevpoint is not None:
            # If it isn't, check whether this point "AllowedToSand" boolean
            # is different from the previous one.
            if points[i].AllowedToSand != prevpoint.AllowedToSand:
                # If it is, check whether the arm needs to go up or down
                if points[i].AllowedToSand:
                    xyzrpw[2] = 0
                else:
                    xyzrpw[2] = 50

                # Set new location in matrix array
                xyzrpw[0] = middle_of_board[0] + prevpoint.PointX
                xyzrpw[1] = middle_of_board[1] - prevpoint.PointY

                # Convert matrix array to usable Fanuc pose
                approach = Fanuc_2_Pose(xyzrpw)

                # Create the new up or down target
                ti2 = robodk.AddTarget('Auto Move Target %i' % (i + 1))

                # set it's position
                ti2.setPose(approach)

                ti2.setAsCartesianTarget()

                # add target to program
                prog.MoveL(ti2)
        else:
            # if it is, check whether the arm start in the air or on the
            # object
            if points[i].AllowedToSand:
                xyzrpw[2] = 0
            else:
                xyzrpw[2] = 50

        """This part sets the new movement on the object"""
        # Set new location in matrix array
        xyzrpw[0] = middle_of_board[0] + points[i].PointX
        xyzrpw[1] = middle_of_board[1] - points[i].PointY

        # Set the current point to prevpoint
        prevpoint = points[i]

        # Convert matrix to Fanuc pose
        approach = Fanuc_2_Pose(xyzrpw)

        # Set the target position
        ti.setPose(approach)

        ti.setAsCartesianTarget()

        # Add the target as linear move to the program
        prog.MoveL(ti)

    print('Done')

    check_collisions = COLLISION_OFF
    # Update the path (can take some time if collision checking is active)
    update_result = prog.Update(check_collisions)

    n_insok = update_result[0]
    time = update_result[1]
    distance = update_result[2]
    percent_ok = update_result[3] * 100
    str_problems = update_result[4]
    if percent_ok < 100.0:
        msg_str = "WARNING! Problems with <strong>%s</strong> (%.1f):<br>%s" % ("AutoProgram", percent_ok, str_problems)
    else:
        msg_str = "No problems found for program %s" % "AutoProgram"

    print(msg_str)

    # run the robot program
    prog.RunProgram()
    # prog.pause()

    # delete the program and the targets
    prog.Delete()

    for i in range(len(points)):
        target = robodk.Item('Auto Target %i' % (i+1), ITEM_TYPE_TARGET)
        target.Delete()

        movetarget = robodk.Item('Auto Move Target %i' % (i+1), ITEM_TYPE_TARGET)
        if movetarget.Valid():
            movetarget.Delete()