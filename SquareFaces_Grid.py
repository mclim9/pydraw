################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Square Smiles
###
################################################################################
### User Inputs
################################################################################
FaceSize  = 100
TimeFactor = 0.5

################################################################################
### Code Begin
################################################################################
numCol      = 5
numRow      = 5
ScrWid      = numCol * FaceSize
ScrHeight   = numRow * FaceSize

import pygame
import math
import time
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
    SmilyGrid = [[squareFace(1,1,FaceSize)] * numRow for i in range(numCol)]
    for i in range(numCol):
        for j in range(numRow):
            xPos = int(i * FaceSize + FaceSize/2)
            yPos = int(j * FaceSize + FaceSize/2)
            SmilyGrid[i][j] = squareFace(xPos,yPos,FaceSize)

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
        for i in range(numCol):
            for j in range(numRow):
                SmilyGrid[i][j].draw(screen)
        clock.tick(0.5)                  # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    # var = input("Please enter something: ")
 
if __name__ == "__main__":
     main()