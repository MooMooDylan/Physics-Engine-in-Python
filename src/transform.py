import math
from vector import Vector2

class Transform:
    def __init__(self, position: Vector2, angle: float):
        self.positionX = position.x
        self.positionY = position.y
        self.sin = math.sin(angle)
        self.cos = math.cos(angle)