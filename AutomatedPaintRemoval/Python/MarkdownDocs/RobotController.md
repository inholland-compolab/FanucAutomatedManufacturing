# RobotController.py

## Description
The RobotController handles the actual actuation of the arm. To control the arm it uses the RoboDK api. The 
RobotController acquires a point list from the RobotVisionModule that it uses to move the arm over the object.
To determine where the arm needs to move in the realword space, it uses the midpoint of the object as a reference
point.

The arm is set to a default position using targets that where added in the simulation.

    home_target = robodk.Item('Home')
    near_start_target = robodk.Item('NearStart')
    start_target = robodk.Item('Start')

here we set the midpoint of the array by setting some default values:
    `middle_of_board = np.array([-250 / 2, 140 / 2])`

We start by iterating through the list of points. during each iteration we check whether the current point is the
first point. This is important because the first point determines if the arm starts on the material or above it.

    # Check whether or not this is the first point in the list
    if prevpoint is not None:

If it is, we will check whether the arm is allowed to sand on this point. This is the only point where the
system needs to check if it can sand **'from'** this point. For all the other points the system checks if it is
allowed to sand **'to'** the point.

    else:
        if points[i].AllowedToSand:
            xyzrpw[2] = 0
        else:
            xyzrpw[2] = 50

If it isn't, the application then compares whether the current points ["AllowedToSand"](PathPoint.md) boolean differs from the
previous one. This is important because an extra move needs to be made to either lower or raise the arm.

    if points[i].AllowedToSand != prevpoint.AllowedToSand:

The application then checks if the point is on the material or above it, the same way as we did above.
It then adds the x y position to the matrix and converts this matrix to a Fanuc position and creates a target
with this position. 

    xyzrpw[0] = middle_of_board[0] + prevpoint.PointX
    xyzrpw[1] = middle_of_board[1] - prevpoint.PointY

    approach = Fanuc_2_Pose(xyzrpw)
    ti2 = robodk.AddTarget('Auto Move Target %i' % (i + 1))

    ti2.setPose(approach)
    ti2.setAsCartesianTarget()
    prog.MoveL(ti2)

After checking the upwards or downwards movement, the application adds the movement of the normal path.

    xyzrpw[0] = middle_of_board[0] + points[i].PointX
    xyzrpw[1] = middle_of_board[1] - points[i].PointY

    prevpoint = points[i]
    approach = Fanuc_2_Pose(xyzrpw)
    ti.setPose(approach)
    ti.setAsCartesianTarget()
    prog.MoveL(ti)

After the application has iterated through the entire point list the application starts the program:`prog.RunProgram()`
