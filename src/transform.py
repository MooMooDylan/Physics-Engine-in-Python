import math

class Transform:
    def __init__(self, position, angle):
        self.positionX = position.x
        self.positionY = position.y
        self.sin = math.sin(angle)
        self.cos = math.cos(angle)