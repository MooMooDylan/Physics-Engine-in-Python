import rigidbodies
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
