from enum import Enum

# Enum for Gestures
class Gesture(Enum):
    RIGHT_SWIPE = 1
    LEFT_SWIPE = 2
    FINGER_UP = 3
    FINGER_DOWN = 4
    OPEN_HAND = 5
    CLOSED_FIST = 6

# Enum for Volume Control
class VolumeControl(Enum):
    UP = 1
    DOWN = 2
