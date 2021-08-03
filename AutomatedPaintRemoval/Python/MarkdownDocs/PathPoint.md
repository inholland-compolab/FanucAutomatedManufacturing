# PathPoint.py

## Description
This module contains the class that is used to store the point coordinates of the path. 

The class stores the following information.

    PointX           : float             : The x coordinate of the point in the simulation space in mm
    PointY           : float             : The Y coordinate of the point in the simulation space in mm
    PointZ           : float             : The Z coordinate of the point in the simulation space in mm
    AllowedToSand    : boolean           : Determines whether or not the arm is allowed to sand to this point
    SandingDirection : ESandingDirection : Determines the sanding direction.

The SandingDirection value remains as of now unused, but could be useful for future development. AllowedToSand determines
whether the arm can or cannot sand towards the point. The robotcontroller determines how it accomplices this.