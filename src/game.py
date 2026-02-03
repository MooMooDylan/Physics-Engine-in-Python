#Created 1-22-26
#Physics Simulation in Python
#Dylan Ku
#The code in this project is mostly based of of Two-Bit Codings's C# tutorial translated into Python by me :)

import pygame, sys, random, math, collisions
from pygame.locals import *
from vector import Vector2
from vector import Math2
from vector import Transform
from rigidbodies import CreateShape
from rigidbodies import RigidBody2

class Colors:
    #Colors
    BLACK = (0, 0, 0)
    GREY = (80, 80, 80)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    TEAL = (0, 128, 128)

#This is outside because python was wining
def VectorToTuple(vector: Vector2): #Converts a Vector to Coordanites(tuple) that can be rendered
    return (((vector.x * zoom * SCALE) + GAMEWIDTH), ((vector.y * zoom * SCALE * -1) + GAMEHEIGHT))

class RenderFunctions:
    #Render Functions

    @staticmethod
    def DrawBorder(color): #Draws a border showing what is seen on zoom 1 Note: Broken when scale isn't 10
        if zoom >= 1:
            pygame.draw.rect(DISPLAYSURF, color, (0, 0, WINDOWWIDTH * zoom, WINDOWHEIGHT * zoom), 1)
        else:
            pygame.draw.rect(DISPLAYSURF, color, (GAMEWIDTH / 2, GAMEHEIGHT / 2, WINDOWWIDTH * zoom, WINDOWHEIGHT * zoom), 1)

    @staticmethod
    def RenderVector(origin: Vector2, vector: Vector2, color: tuple, width: int): #Draws a vector on the screen
        pygame.draw.line(DISPLAYSURF, color, VectorToTuple(origin), VectorToTuple(origin + (vector * SCALE)), width)

    @staticmethod
    def RenderCircle(position: Vector2, color: tuple, radius: float, width: int): #Renders a circle
        pygame.draw.circle(DISPLAYSURF, color, VectorToTuple(position), radius * SCALE * zoom, width)

    @staticmethod
    def RenderBox(position: Vector2, color: tuple, sizeX: float, sizeY: float, width: int): #Renders a box
        pygame.draw.rect(DISPLAYSURF, color, ((position.x * zoom * SCALE) + GAMEWIDTH, (position.y * zoom * SCALE * -1) + GAMEHEIGHT, sizeX * SCALE * zoom, sizeY * SCALE * zoom), width)

    #Renders a polygon based on its points
    @staticmethod
    def RenderPolygon(rigidbody: RigidBody2, color: tuple, width: int):
        #Points are vectors and must be converted into a sequence of coordinates
        dst = Math2.ToCordArray(rigidbody.GetTransformedVertices())
    
        for i in range(len(dst)):
            temp = dst[i]
            temp = ((temp[1] * zoom * SCALE) + GAMEWIDTH, (temp[0] * zoom * SCALE * -1) + GAMEHEIGHT)
            dst[i] = temp

        pygame.draw.polygon(DISPLAYSURF, color, dst, width)

#----Pygame Setup----

pygame.init()

#Target FPS
FPS = 30
fpsClock = pygame.time.Clock()

#Window Dimensions
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

#World Space Dimenstions
GAMEWIDTH = WINDOWWIDTH / 2
GAMEHEIGHT = WINDOWHEIGHT / 2

#Create Window
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
image = 1
pygame.display.set_caption('Physics')

#Import Icon
try:
    if image == 0:
        icon = pygame.image.load("assets/vectorohye.webp")
    elif image == 1:
        icon = pygame.image.load("assets/Galaxy_brain.jpg")
    pygame.display.set_icon(icon)
except:
    print("Failed to load image.")

#----REDERING STUFF----

#Multiply posistion and scale by zoom
#Multiply Horizontal / Y positions by -1
#Add GAMEWIDTH and GAMEHEIGHT

#Zoom and Scale
#Note scale pixels = 1 meter when zoom = 1
SCALE = 10
zoom = 1
zoomSpeed = 0.5



#------Initialize------

#Test stuff
bodyList = list()
bodyColors = list()
bodyCount = 10
padding = 1

for i in range(bodyCount):
    type = 1

    x = random.randrange(-GAMEWIDTH / 10 + 1, GAMEWIDTH / 10 - 1)
    y = random.randrange(-GAMEHEIGHT / 10 + 1, GAMEHEIGHT / 10 - 1)

    if type == 0:
        bodyList.append(CreateShape.CreateCircleBody(1, Vector2(x, y), 2, False, 0.5))
    if type == 1:
        bodyList.append(CreateShape.CreateBoxBody(4, 4, Vector2(x, y), 2, False, 0.5))
        bodyColors.append(Colors.WHITE)
        
dx = 0
dy = 0
speed = 8

#-------Main Loop------
while True:
    deltaTime = fpsClock.tick(60) / 1000

    #Render Objects
    DISPLAYSURF.fill(Colors.TEAL)

    RenderFunctions.DrawBorder(Colors.BLACK)

    for i in range(bodyCount):
        body: RigidBody2 = bodyList[i]
        if body.SHAPETYPE == 0:
            RenderFunctions.RenderCircle(body.position, Colors.WHITE, body.RADIUS, 0)
        elif body.SHAPETYPE == 1:
            RenderFunctions.RenderPolygon(body, bodyColors[i], 0)
            if body.linearVelocity != Vector2(0, 0):
                RenderFunctions.RenderVector(body.position, body.linearVelocity, Colors.BLACK, 1)
            else:
                RenderFunctions.RenderVector(body.position)

    #Event Code 
    for event in pygame.event.get():
        #Input
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                zoom += zoomSpeed
            if event.key == K_z:
                zoom -= zoomSpeed
                if zoom < zoomSpeed:
                    zoom += zoomSpeed

            if event.key == K_LEFT:
                dx -= 1
            if event.key == K_RIGHT:
                dx += 1
            if event.key == K_UP:
                dy += 1
            if event.key == K_DOWN:
                dy -= 1

        #Quit game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Update Velocity based on input and move
    if (dx != 0 or dy != 0):
        direction = Math2.Normalize(Vector2(dx, dy))
        velocity = direction * speed * deltaTime
        bodyList[0].linearVelocity = velocity
        bodyList[0].Move(velocity)

    #Collisions

    for i in range(bodyCount):
        body = bodyList[i]
        body.Rotate(math.pi / 2 * deltaTime)
        bodyColors[i] = Colors.WHITE

    for i in range(bodyCount - 1):
        bodyA: RigidBody2 = bodyList[i]
        j = i + 1
        while j < bodyCount:
            bodyB: RigidBody2 = bodyList[j]
            
            if collisions.IntercectPolygons(bodyA.GetTransformedVertices(), bodyB.GetTransformedVertices()):
                bodyColors[i] = Colors.RED
                bodyColors[j] = Colors.RED

#            intercecting = collisions.IntercectCircles(bodyA.position, bodyA.RADIUS, bodyB.position, bodyB.RADIUS)
#
#            if intercecting.collide:
#                bodyA.Move(intercecting.normal * -1 * (intercecting.depth / 2))
#                bodyB.Move(intercecting.normal * (intercecting.depth / 2))
#
            j += 1

    #Update Display and clock
    pygame.display.update()
    fpsClock.tick(FPS)