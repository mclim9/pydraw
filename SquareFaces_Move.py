################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Square Smiles
###
################################################################################
### User Inputs
################################################################################
FaceSize  = 128
TimeFactor  = 0.25       # Slow down factor

################################################################################
### Code Begin
################################################################################
numCol      = 5
numRow      = 5
ScrWid      = numCol * FaceSize
ScrHeight   = numRow * FaceSize

import pygame
import random
import math
import time
from colors import  *
from pygame import gfxdraw
from math   import pi
from SquareFaces import squareFace

ScreenRadius = int(ScrWid/2 - FaceSize/2)

################################################################################
### Define colors
################################################################################
Colors  = [RED,ORANGE,YELLOW,GREEN,DkGREEN,BLUE,PURPLE,SEAFOAM,MAGENTA,GREY50,TEAL]
Eyes    = ['Open','Wow','Small']
Pupils  = [0.3,0.5,0.5,0.9,0.5]

from pygame.locals import DOUBLEBUF, FULLSCREEN
flags = DOUBLEBUF       # FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Main Code
################################################################################
def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [ScrWid, ScrHeight]
    screen = pygame.display.set_mode(size,flags)
    screen.set_alpha(None)

    pygame.display.set_caption("squareFace Plot")
    done                    = False
    selected_squareFace     = None
    clock = pygame.time.Clock()     # Manage screen updates

    ###########################################################################
    ### Main Code
    ###########################################################################
    SmilyArry = []
    for i in range(numCol):
        for j in range(numRow):
            xPos = int(i * FaceSize + FaceSize/2)
            yPos = int(j * FaceSize + FaceSize/2)
            SmilyArry.append(squareFace(xPos,yPos,FaceSize))
    SmilyArry.append(squareFace(xPos,yPos,FaceSize))  #Moving one

    while not done:
        #######################################################################
        ### Event Processing
        #######################################################################
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #######################################################################
        ### Drawing Code
        #######################################################################
        t = pygame.time.get_ticks()/1000 * TimeFactor
        screen.fill(BLACK)              # Set the screen background
        SmilyArry[numCol*numRow].x = int(ScrWid/2    + ScreenRadius * math.cos(t))
        SmilyArry[numCol*numRow].y = int(ScrHeight/2 + ScreenRadius * math.sin(t))
        for face in SmilyArry:
            face.draw(screen)
        clock.tick(60)                   # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    # var = input("Please enter something: ")
 
if __name__ == "__main__":
     main()