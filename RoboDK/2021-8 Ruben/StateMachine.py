from enum import Enum, auto
import enum

class States(enum):
    idle = auto()
    status = auto()
    move = auto()
    emergencyStop = auto()