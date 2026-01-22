#This is a collection of classes related to 2 Dimensional Vectors

import pygame

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
    

class VectorMath:
    #Length of a vector (magnatude)
    def Length(self, vector):
        x = 1
    
    #Distance between two vectors
    def Distance(self, v1, v2):
        x = 1

    #Normalize a vector
    def Normalize(self, vector):
        x = 1

    #Find the dot product of two vectors
    def Dot(self, v1, v2):
        x = 1

    #Find the cross product of two vectors
    def Cross(self, v1, v2):
        x = 1