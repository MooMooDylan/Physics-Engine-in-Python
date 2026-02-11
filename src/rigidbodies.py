import math
from enum import Enum
from vector import Vector2
from vector import World
from vector import Math2
from vector import Transform

class Shapes(Enum):
        Circle = 0
        Box = 1

class RigidBody2: 

    def __init__(self, pos: Vector2, density, mass, restitution, area, isStatic: bool, radius, width, height, shapetype):
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

        #Shape key:
        #0 = cicle
        #1 = box
        self.SHAPETYPE = shapetype

        if (shapetype == 1):
            self.VERTICES = CreateShape.BoxVertices(self.WIDTH, self.HEIGHT)
            self.transformedvertices = list(range(len(self.VERTICES)))
            self.triangles = CreateShape.CreateBoxTriangles()
        else:
            self.VERTICES = list()
            self.transformedvertices = list()
            self.triangles = list()

        self.transformUpdateRequired = True

    def GetTransformedVertices(self):
        if self.transformUpdateRequired:
            transform = Transform(self.position.x, self.position.y, self.rotation)

            for i in range(len(self.VERTICES)):
                v = self.VERTICES[i]
                self.transformedvertices[i] = Math2.Transform(v, transform)
        return self.transformedvertices

    def Move(self, amount: float):
        self.position = self.position + amount
        self.transformUpdateRequired = True

    def MoveTo(self, position: Vector2):
        self.position = position
        self.transformUpdateRequired = True

    def Rotate(self, amount: float):
        self.rotation = self.rotation + amount
        self.transformUpdateRequired = True

    def __repr__(self):
        return f"{self.position}, {self.linearVelocity}"
    
class CreateShape:
    @staticmethod
    def CreateCircleBody(radius: float, position: Vector2, dencity: float, isStatic: bool, restitution: float):

            area = (radius ** 2) * math.pi

            if (area < World.MINBODYSIZE):
                print("Error: Area is too small.")
            if (area > World.MAXBODYSIZE):
                print("Error: Area is too big")
            if (dencity < World.MINDENCITY):
                 print("Error: Dencity too small")
            if (dencity > World.MAXDENCITY):
                 print("Error: Dencity too large")

            restitution = Math2.Clamp(restitution, 0, 1)

            mass = area * dencity

            body = RigidBody2(position, dencity, mass, restitution, area, isStatic, radius, 0, 0, 0)
            return body

    @staticmethod
    def CreateBoxBody(width: float, height: float, position: Vector2, dencity: float, isStatic: bool, restitution: float):
            area = width * height

            if (area < World.MINBODYSIZE):
                print("Error: Area is too small.")
            if (area > World.MAXBODYSIZE):
                print("Error: Area is too big")
            if (dencity < World.MINDENCITY):
                print("Error: Dencity too small")
            if (dencity > World.MAXDENCITY):
                print("Error: Dencity too large")

            restitution = Math2.Clamp(restitution, 0, 1)

            mass = area * dencity

            body = RigidBody2(position, dencity, mass, restitution, area, isStatic, 0, width, height, 1)
            return body
    
    @staticmethod
    def BoxVertices(width: float, height: float):
        left = -width / 2
        right = left + width
        bottom = -height / 2
        top = bottom + height

        vertices = list()
        vertices.append(Vector2(left, top))
        vertices.append(Vector2(right, top))
        vertices.append(Vector2(right, bottom))
        vertices.append(Vector2(left, bottom))

        return vertices
    
    @staticmethod
    def CreateBoxTriangles():
        triangles = [0, 1, 2, 0, 2, 3]
        return triangles