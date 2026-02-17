import rigidbodies, sys
from vector import Math2
from vector import Vector2

class Collision:
    def __init__(self, collision: bool, collisionNormal=Vector2(0,0), collisionDepth=float(0)):
        self.collide = collision
        self.normal = collisionNormal
        self.depth = collisionDepth

    def __repr__(self):
        if self.collide == False:
            return f"{self.collide}"
        else:
            return f"{self.collide}, {self.normal}, {self.depth}"
        
class Projection:
    def __init__(self, min, max):
        self.min = min
        self.max = max

def IntercectCircles(centerA: Vector2, radiusA: float, centerB: Vector2, radiusB: float):
    distance = Math2.Distance(centerA, centerB)
    radii = radiusA + radiusB

    if distance >= radii:
        return Collision(False)
    
    normal = Math2.Normalize(centerB - centerA)
    depth = radii - distance

    return Collision(True, normal, depth)

def IntercectPolygons(verticesA: list, verticesB: list): #Lists of Vector2s
    normal = Vector2(0, 0)
    depth = sys.float_info.max

    for i in range(len(verticesA)):
        va: Vector2 = verticesA[i]
        vb: Vector2 = verticesA[(i + 1) % len(verticesA)]

        edge = vb - va
        axis = Vector2(-edge.y, edge.x)

        minA = ProjectVertices(verticesA, axis).min
        maxA = ProjectVertices(verticesA, axis).max
        minB = ProjectVertices(verticesB, axis).min
        maxB = ProjectVertices(verticesB, axis).max

        #If so there is a gap
        if minA >= maxB or minB >= maxA:
            return Collision(False)
        
        axisDepth = min(maxB - minA, maxA - minB)

        if axisDepth < depth:
            depth = axisDepth
            normal = Vector2(axis.y, axis.x)

    for i in range(len(verticesB)):
        va = verticesB[i]
        vb = verticesB[(i + 1) % len(verticesB)]

        edge = vb - va
        axis = Vector2(-edge.y, edge.x)

        minA = ProjectVertices(verticesA, axis).min
        maxA = ProjectVertices(verticesA, axis).max
        minB = ProjectVertices(verticesB, axis).min
        maxB = ProjectVertices(verticesB, axis).max
        
        #If so there is a gap
        if minA >= maxB or minB >= maxA:
            return Collision(False)

        axisDepth = min(maxB - minA, maxA - minB)

        if axisDepth < depth:
            depth = axisDepth
            normal = Vector2(axis.y, axis.x)
            
    depth = depth / Math2.Length(normal)
    normal = Math2.Normalize(normal)

    centerA = FindArithmaticMean(verticesA)
    centerB = FindArithmaticMean(verticesB)

    direction = centerB - centerA

    if Math2.Dot(direction, normal) < 0:
        normal = normal * -1

    #No gaps found meaning collision
    return Collision(True, normal, depth)

def ProjectVertices(vertices: list, axis: Vector2):
    min = sys.float_info.max
    max = sys.float_info.min

    for i in range(len(vertices)):
        v = vertices[i]

        proj = Math2.Dot(v, axis)

        if proj < min:
            min = proj
        if proj > max:
            max = proj
    
    return Projection(min, max)

def FindArithmaticMean(vertices: list):
    sumX = 0.0
    sumY = 0.0

    for i in range(len(vertices)):
        v: Vector2 = vertices[i]
        sumX += v.x
        sumY += v.y
    
    return Vector2(sumX / float(len(vertices)), sumY / float(len(vertices)))