import rigidbodies
from vector import Math2

class CircleCollision:
    def __init__(self, collision, collisionNormal, collisionDepth):
        self.collide = collision
        self.normal = collisionNormal
        self.depth = collisionDepth

def IntercectCircles(centerA, radiusA, centerB, radiusB):
    distance = Math2.Distance(centerA, centerB)
    radii = radiusA + radiusB

    if distance >= radii:
        return CircleCollision(False, 0, 0)
    
    normal = Math2.Normalize(centerB - centerA)
    depth = radii - distance

    return CircleCollision(True, normal, depth)