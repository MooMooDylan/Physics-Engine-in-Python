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
            return Collision(False)
        
        axisDepth = min(maxB - minA, maxA - minB)

        if axisDepth < depth:
            depth = axisDepth
            normal = axis
        
    depth = depth / Math2.Length(normal)
    normal = Math2.Normalize(normal)

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
            return Collision(False)
    
    #No gaps found meaning collision
    return Collision(True, depth, normal)

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

