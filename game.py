#Created 1-22-26
#Physics Simulation in Python
#Dylan Ku
#The code in this project is mostly based of of Two-Bit Codings's C# tutorial translated into Python by me :)

import pygame, sys
from pygame.locals import *
from lib.physics import Vector2
from lib.physics import VectorMath

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
icon = pygame.image.load("assets/Galaxy_brain.jpg")
pygame.display.set_icon(icon)

#Zoom
zoom = 1
zoomSpeed = 0.5

#Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (0, 128, 128)

#Vectors
VectorA = Vector2(1, 1)
VectorB = Vector2(2, 2)

#Main Loop
while True:

    #Render Code
    #Multiply posistion and scale by zoom
    #Multiply Horizontal / Y positions by -1
    #Add GAMEWIDTH and GAMEHEIGHT

    DISPLAYSURF.fill(TEAL)

    pygame.draw.line(DISPLAYSURF, BLACK, ((0 * zoom) + GAMEWIDTH, (0 * zoom) + GAMEWIDTH),  ((VectorA.x * zoom * -1, VectorA.y * zoom * -1)) + GAMEHEIGHT, 1)

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