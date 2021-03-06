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
numCol      = 2
numRow      = 2
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
def faceArryCreate():
    SmilyArry = []
    for i in range(numCol):   #Create Primary Grid
        for j in range(numRow):
            xPos = int(i * FaceSize + FaceSize/2)
            yPos = int(j * FaceSize + FaceSize/2)
            SmilyArry.append(squareFace(xPos,yPos,FaceSize))
    return SmilyArry

def faceRecurse(facearry):
    """Creates smaller faces """
    for i,thisFace in enumerate(facearry):
        if random.randint(0,100) < 40:                                  #Face --> 4 Smaller Faces?
            if thisFace.size > 20:                                      #Div if > min size
                newSize = int(thisFace.size/2)                          #Children are 1/2 size
                offset  = int(newSize/2)
                x = thisFace.x
                y = thisFace.y
                facearry[i] = squareFace(x-offset,y-offset,newSize)     #Upper left
                facearry.append(squareFace(x+offset,y-offset,newSize))  #Upper right
                facearry.append(squareFace(x-offset,y+offset,newSize))  #Lower left
                facearry.append(squareFace(x+offset,y+offset,newSize))  #Lower right

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
    done = False
    clock = pygame.time.Clock()         # Manage screen updates

    #############################################################################
    ### Font
    #############################################################################
    pygame.font.init()                  # Called at start 
    myfont = pygame.font.SysFont('Courier', 20, bold=True)

    ###########################################################################
    ### Main Code
    ###########################################################################
    SmilyArry = []
    SmilyArry = faceArryCreate()
    faceRecurse(SmilyArry)
 
    while not done:
        #######################################################################
        ### Event Processing
        #######################################################################
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print('Key0')
                    SmilyArry = []
                    SmilyArry = faceArryCreate()
                    faceRecurse(SmilyArry)

        #######################################################################
        ### Drawing Code
        #######################################################################
        screen.fill((0,0,0))                # Set the screen background
        for face in SmilyArry:
            face.draw(screen)
        clock.tick(0.5)                     # Limit to 60 frames per second

        outText = "Text"
        textsurface = myfont.render(outText, True, (255, 255, 255)) #render
        screen.blit(textsurface,(0,0))      # Draw text
        pygame.display.update()             # update the screen w/ what we've drawn.
    #End While
    # var = input("Please enter something: ")
 
if __name__ == "__main__":
     main()