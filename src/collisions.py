import rigidbodies, sys
from vector import Math2
from vector import Vector2

class CircleCollision:
    def __init__(self, collision: bool, collisionNormal: Vector2, collisionDepth: float):
        self.collide = collision
        self.normal = collisionNormal
        self.depth = collisionDepth

def IntercectCircles(centerA: Vector2, radiusA: float, centerB: Vector2, radiusB: float):
    distance = Math2.Distance(centerA, centerB)
    radii = radiusA + radiusB

    if distance >= radii:
        return CircleCollision(False, 0, 0)
    
    normal = Math2.Normalize(centerB - centerA)
    depth = radii - distance

    return CircleCollision(True, normal, depth)

def IntercectPolygons(verticesA: list, verticesB: list): #Lists of Vector2s
    for i in range(len(verticesA)):
        va = verticesA[i]
        vb = verticesA[(i + 1) % len(verticesA)]

        edge = vb - va
        axis = Vector2(-edge.y, edge.x)

        minA = ProjectVertices(verticesA, axis).x
        maxA = ProjectVertices(verticesA, axis).y
        minB = ProjectVertices(verticesB, axis).x
        maxB = ProjectVertices(verticesB, axis).y

        #If so there is a gap
        if minA >= maxB or minB >= maxA:
            return False
        
    for i in range(len(verticesB)):
        va = verticesB[i]
        vb = verticesB[(i + 1) % len(verticesB)]

        edge = vb - va
        axis = Vector2(-edge.y, edge.x)

        minA = ProjectVertices(verticesA, axis).x
        maxA = ProjectVertices(verticesA, axis).y
        minB = ProjectVertices(verticesB, axis).x
        maxB = ProjectVertices(verticesB, axis).y

        #If so there is a gap
        if minA >= maxB or minB >= maxA:
            return False
    
    #No gaps found meaning collision
    return True

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
    
    return Vector2(min, max)

