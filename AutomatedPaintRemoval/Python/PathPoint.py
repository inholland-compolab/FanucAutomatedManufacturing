"""
This module is contains the PathPoint class

This class is used to specify the different points the robotarm
needs to sand to.
"""


from enum import Enum


class ESandingDirection(Enum):
    """
    Sets the Sanding direction of the path
    """
    NoDirection = 0
    Up = 1
    Down = 2
    Right = 3
    Left = 4


class PathPoint:
    """
    The PathPoint class were different point objects a created from.
    """
    def __init__(self, x: float, y: float, z=1.0, allowed_to_sand=True, sanding_direction=ESandingDirection.NoDirection):
        """
        The PathPoint constructor

        :param float x: specifies the x location of the point on the object
        :param float y: specifies the y location of the point on the object
        :param float z: specifies the z location of the point on the object
        :param boolean allowed_to_sand: Whether the point path to the point is allowed to bes sand
        :param SandingDirection sanding_direction: The sanding direction
        """
        self.PointX = x
        self.PointY = y
        self.PointZ = z

        self.AllowedToSand = allowed_to_sand
        self.SandingDirection = sanding_direction
    
    def __str__(self):
        return f'Point coordinate X: {self.PointX:-6.2f}, Y: {self.PointY:-6.2f}, Z: {self.PointZ:.2f}, AllowedToSand: {self.AllowedToSand}, SandingDirection: {self.SandingDirection}'

    """Getter and setters of the different property's"""

    @property
    def PointX(self):
        return self.__PointX
    
    @PointX.setter
    def PointX(self, val):
        self.__PointX = val

    @property
    def PointY(self):
        return self.__PointY
    
    @PointY.setter
    def PointY(self, val):
        self.__PointY = val
    
    @property
    def PointZ(self):
        return self.__PointZ
    
    @PointZ.setter
    def PointZ(self, val):
        self.__PointZ = val

    @property
    def AllowedToSand(self):
        return self.__AllowedToSand
    
    @AllowedToSand.setter
    def AllowedToSand(self, val):
        self.__AllowedToSand = val
