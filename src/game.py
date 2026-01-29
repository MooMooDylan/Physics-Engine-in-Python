#Created 1-22-26
#Physics Simulation in Python
#Dylan Ku
#The code in this project is mostly based of of Two-Bit Codings's C# tutorial translated into Python by me :)

import pygame, sys, random, collisions, math
from pygame.locals import *
from vector import Vector2
from vector import Math2
from rigidbodies import CreateShape

#----Pygame Setup----

pygame.init()

#Target FPS
FPS = 30
fpsClock = pygame.time.Clock()

#Window Dimensions
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

GAMEWIDTH = WINDOWWIDTH / 2
GAMEHEIGHT = WINDOWHEIGHT / 2

#Create Window
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Physics')
try:
    icon = pygame.image.load("assets/vectorohye.webp")
    pygame.display.set_icon(icon)
except:
    print("Failed to load image.")

#----REDERING STUFF----

#Zoom
scale = 10
zoom = 1
zoomSpeed = 0.5

#Render Functions
def DrawBorder():
    if zoom >= 1:
        pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH * zoom, WINDOWHEIGHT * zoom), 1)
    else:
        pygame.draw.rect(DISPLAYSURF, BLACK, (GAMEWIDTH / 2, GAMEHEIGHT / 2, WINDOWWIDTH * zoom, WINDOWHEIGHT * zoom), 1)

def RenderVector(vector):
    return (((vector.x * zoom * scale) + GAMEWIDTH), ((vector.y * zoom * scale * -1) + GAMEHEIGHT))

def DrawVectorAsLine(vector, color, width):
    pygame.draw.line(DISPLAYSURF, color, RenderVector(Vector2(0, 0)), RenderVector(vector), width)

def RenderCircle(position, color, radius, width):
    pygame.draw.circle(DISPLAYSURF, color, RenderVector(position), radius * scale * zoom, width)

def RenderBox(position, color, sizeX, sizeY, width):
    pygame.draw.rect(DISPLAYSURF, color, ((position.x * zoom * scale) + GAMEWIDTH, (position.y * zoom * scale * -1) + GAMEHEIGHT, sizeX * scale * zoom, sizeY * scale * zoom), width)

#points are vectors and must be converted into a sequence of coordinates
def RenderPolygon(rigidbody, color, width):
    dst = Math2.ToCordArray(rigidbody.GetTransformedVertices())
    
    for i in range(len(dst)):
        dst[i] = ((dst[i][0] * zoom * scale) + GAMEWIDTH, (dst[i][1] * zoom * scale) + GAMEHEIGHT)

    pygame.draw.polygon(DISPLAYSURF, color, dst, width)


#Color
BLACK = (0, 0, 0)
GREY = (80, 80, 80)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)

#------Initialize------

#Test stuff
bodyList = list()
bodyCount = 10
padding = 1

for i in range(bodyCount):
    type = 1

    x = random.randrange(-GAMEWIDTH / 10 + 1, GAMEWIDTH / 10 - 1)
    y = random.randrange(-GAMEHEIGHT / 10 + 1, GAMEHEIGHT / 10 - 1)

    if type == 0:
        bodyList.append(CreateShape.CreateCircleBody(1, Vector2(x, y), 2, False, 0.5))
    if type == 1:
        bodyList.append(CreateShape.CreateBoxBody(2, 2, Vector2(x, y), 2, False, 0.5))
        
dx = 0
dy = 0
speed = 8

#Main Loop
while True:
    deltaTime = fpsClock.tick(60) / 1000

    #Render Code
    #Multiply posistion and scale by zoom
    #Multiply Horizontal / Y positions by -1
    #Add GAMEWIDTH and GAMEHEIGHT

    DISPLAYSURF.fill(TEAL)

    DrawBorder()

    for i in range(bodyCount):
        body = bodyList[i]
        if body.SHAPETYPE == 0:
            RenderCircle(body.position, WHITE, body.RADIUS, 0)
        elif body.SHAPETYPE == 1:
            RenderPolygon(body, BLACK, 0)

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

    #Update Velocity based on input
    if (dx != 0 or dy != 0):
        direction = Math2.Normalize(Vector2(dx, dy))
        velocity = direction * speed * deltaTime
        bodyList[0].Move(velocity)

    #Collisions

    for i in range(bodyCount):
        body = bodyList[i]
        body.Rotate(math.pi / 2 * deltaTime)

#    for i in range(bodyCount - 1):
#        bodyA = bodyList[i]
#        j = i + 1
#        while j < bodyCount:
#            bodyB = bodyList[j]
#            
#            intercecting = collisions.IntercectCircles(bodyA.position, bodyA.RADIUS, bodyB.position, bodyB.RADIUS)
#
#            if intercecting.collide:
#                bodyA.Move(intercecting.normal * -1 * (intercecting.depth / 2))
#                bodyB.Move(intercecting.normal * (intercecting.depth / 2))
#
#            j += 1


    pygame.display.update()
    fpsClock.tick(FPS)
