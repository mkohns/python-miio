import enum


class OperationMode(enum.Enum):
    Normal = "normal"
    Nature = "nature"


class LedBrightness(enum.Enum):
    Bright = 0
    Dim = 1
    Off = 2


class MoveDirection(enum.Enum):
    Left = "left"
    Right = "right"
