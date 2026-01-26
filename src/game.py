#Created 1-22-26
#Physics Simulation in Python
#Dylan Ku
#The code in this project is mostly based of of Two-Bit Codings's C# tutorial translated into Python by me :)

import pygame, sys, random
from pygame.locals import *
from physics import Vector2
from physics import Math2
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
zoom = 1
zoomSpeed = 0.5

#Render Functions
def RenderVector(vector):
    return (((vector.x * zoom * 10) + GAMEWIDTH), ((vector.y * zoom * 10 * -1) + GAMEHEIGHT))

def DrawVectorAsLine(vector, color, width):
    pygame.draw.line(DISPLAYSURF, color, RenderVector(Vector2(0, 0)), RenderVector(vector), width)

def RenderCircle(position, color, radius, width):
    pygame.draw.circle(DISPLAYSURF, color, RenderVector(position), radius * 10 * zoom, width)

def RenderBox(position, color, sizeX, sizeY, width):
    pygame.draw.rect(DISPLAYSURF, color, ((position.x * zoom * 10) + GAMEWIDTH, (position.y * zoom * 10) + GAMEHEIGHT, sizeX * 10 * zoom, sizeY * 10 * zoom), width)


#Color
BLACK = (0, 0, 0)
GREY = (80, 80, 80)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)

#---------------------

#Test stuff
bodyList = list()
bodyCount = 10

for i in range(bodyCount):
    type = random.randint(0, 1)

    x = random.randrange(-GAMEWIDTH / 10, GAMEWIDTH / 10)
    y = random.randrange(-GAMEHEIGHT / 10, GAMEHEIGHT / 10)

    if type == 0:
        bodyList.append(CreateShape.CreateCircleBody(1.5, Vector2(x, y), 2, False, 0.5))
    if type == 1:
        bodyList.append(CreateShape.CreateBoxBody(3, 3, Vector2(x, y), 2, False, 0.5))
        
        

#Main Loop
while True:

    #Render Code
    #Multiply posistion and scale by zoom
    #Multiply Horizontal / Y positions by -1
    #Add GAMEWIDTH and GAMEHEIGHT

    DISPLAYSURF.fill(TEAL)

    for i in range(bodyCount):
        body = bodyList[i]
        if body.SHAPETYPE == 0:
            RenderCircle(body.position, WHITE, body.RADIUS, 0)
        elif body.SHAPETYPE == 1:
            RenderBox(body.position, BLACK, body.WIDTH, body.HEIGHT, 0)

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

        #Quit game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
