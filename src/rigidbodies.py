import math
from enum import Enum
from physics import Vector2
from physics import World
from physics import Math2

class Shapes(Enum):
        Circle = 0
        Box = 1

class RigidBody2: 

    def __init__(self, pos, density, mass, restitution, area, isStatic, radius, width, height, shapetype):
        self.position = pos
        self.linearVelocity = Vector2(0, 0)
        self.rotation = 0
        self.rotationVelocity = 0
        
        self.DENCITY = density
        self.MASS = mass
        self.AREA = area
        self.RESTITUTION = restitution

        self.ISSTATIC = isStatic
        self.RADIUS = radius
        self.WIDTH = width
        self.HEIGHT = height

        self.SHAPETYPE = shapetype
    
class CreateShape:
    @staticmethod
    def CreateCircleBody(radius, position, dencity, isStatic, restitution):

            area = (radius ** 2) * math.pi

            if (area < World.MINBODYSIZE):
                print("Error: Area is too small.")
                return False
            if (area > World.MAXBODYSIZE):
                print("Error: Area is too big")
                return False
            if (dencity < World.MINDENCITY):
                 print("Error: Dencity too small")
                 return False
            if (dencity > World.MAXDENCITY):
                 print("Error: Dencity too large")
                 return False

            restitution = Math2.Clamp(restitution, 0, 1)

            mass = area * dencity

            body = RigidBody2(position, dencity, mass, restitution, area, isStatic, radius, 0, 0, 0)
            return body

    @staticmethod
    def CreateBoxBody(width, height, position, dencity, isStatic, restitution):
            area = width * height

            if (area < World.MINBODYSIZE):
                print("Error: Area is too small.")
                return False
            if (area > World.MAXBODYSIZE):
                print("Error: Area is too big")
                return False
            if (dencity < World.MINDENCITY):
                print("Error: Dencity too small")
                return False
            if (dencity > World.MAXDENCITY):
                print("Error: Dencity too large")
                return False

            restitution = Math2.Clamp(restitution, 0, 1)

            mass = area * dencity

            body = RigidBody2(position, dencity, mass, restitution, area, isStatic, 0, width, height, 1)
            return body