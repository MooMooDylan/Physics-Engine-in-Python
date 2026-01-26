#This is a collection of classes related to 2 Dimensional Vectors
import math
from enum import Enum

class Vector2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Math Functions
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scaler):
        return Vector2(self.x * scaler, self.y * scaler)
    
    def __truediv__(self, scaler):
        return Vector2(self.x / scaler, self.y / scaler)
    
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Math2:
    @staticmethod
    def Clamp(value, min, max):
        if(min == max):
            return min
        if(value < min):
            return min
        if(value > max):
            return max
        return value


    #Length of a vector (magnatude)
    #Uses distance formula
    @staticmethod
    def Length(vector):
        return math.sqrt(vector.x ** 2 + vector.y ** 2)
    
    #Distance between two vectors
    #Uses distace formula
    @staticmethod
    def Distance(v1, v2):
        return math.sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    #Normalize a vector
    @staticmethod
    def Normalize(vector):
        len = Math2.Length(vector)
        return Vector2(vector.x / len, vector.y / len)

    #Find the dot product of two vectors
    #v1 • v2
    @staticmethod
    def Dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    #Find the cross product of two vectors
    #Returns the z value of the cross product
    #v1 x v2
    @staticmethod
    def Cross(v1, v2):
        return v1.x * v2.y + v1.y * v2.x

class World:
    MINBODYSIZE = 0.01 ** 2
    MAXBODYSIZE = 64 ** 2

    #g/cm^3
    MINDENCITY = 0.5
    MAXDENCITY = 21.4