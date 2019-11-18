################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Square Smiles
###
################################################################################
### User Inputs
################################################################################
FaceSize  = 256
TimeFactor = 0.5

################################################################################
### Code Begin
################################################################################
numCol      = 3
numRow      = 3
ScrWid      = numCol * FaceSize
ScrHeight   = numRow * FaceSize

import pygame
import math
import time
import random
from SquareFaces import squareFace

################################################################################
### Define colors
################################################################################
from pygame.locals import DOUBLEBUF, FULLSCREEN
flags = DOUBLEBUF       # FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Definitions
################################################################################
def faceRecurs(facearry):
    for i,thisFace in enumerate(facearry):
        if random.randint(0,100) < 40:
            if thisFace.size > 20:
                newSize = int(thisFace.size/2)
                offset  = int(newSize/2)
                x = thisFace.x
                y = thisFace.y
                facearry[i] = squareFace(x-offset,y-offset,newSize)     #Upper left
                facearry.append(squareFace(x+offset,y-offset,newSize)) #Upper right
                facearry.append(squareFace(x-offset,y+offset,newSize)) #Lower left
                facearry.append(squareFace(x+offset,y+offset,newSize)) #Lower right

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

    #############################################################################
    ### Font
    #############################################################################
    pygame.font.init() # you have to call this at the start, 
    # myfont = pygame.font.SysFont('Courier', 20, bold=True)

    ###########################################################################
    ### Main Code
    ###########################################################################
    SmilyArry = []
    for i in range(numCol):   #Create Primary Grid
        for j in range(numRow):
            xPos = int(i * FaceSize + FaceSize/2)
            yPos = int(j * FaceSize + FaceSize/2)
            SmilyArry.append(squareFace(xPos,yPos,FaceSize))

    faceRecurs(SmilyArry)
    faceRecurs(SmilyArry)

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
        screen.fill((0,0,0))              # Set the screen background
        for face in SmilyArry:
            face.draw(screen)
        clock.tick(0.5)                  # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    # var = input("Please enter something: ")
 
if __name__ == "__main__":
     main()