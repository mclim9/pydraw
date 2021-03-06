################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Square Smiles
###
################################################################################
### User Inputs
################################################################################
glyphSizeX  = 6
glyphSizeY  = 6
glyphPtSpc  = 8
glyphSize   = (glyphSizeX + 2) * glyphPtSpc
symmetryV   = 1
bkgColor    = (255, 255, 255)
################################################################################
### Code Begin
################################################################################
numCol      = 10
numRow      = 10
ScrWid      = (numCol + 2) * glyphSize
ScrHeight   = (numRow + 2) * glyphSize

import pygame
import random
import math
import time
from colors import  *
from pygame import gfxdraw
from math   import pi

################################################################################
### Define colors
################################################################################
Colors  = [RED,ORANGE,YELLOW,GREEN,DkGREEN,BLUE,PURPLE,SEAFOAM,MAGENTA,GREY50,TEAL]

from pygame.locals import DOUBLEBUF, FULLSCREEN
flags = DOUBLEBUF       # FULLSCREEN | DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Definitions
################################################################################
class glyph:
    ###Class to keep track of a each glyph plot
    def __init__(self,xPos,yPos,Size):
        self.size       = Size
        self.color      = random.choice(Colors)
        self.color      = bkgColor
        self.x          = int(xPos)
        self.y          = int(yPos)
        self.Xorigin    = int(self.x - self.size/2)
        self.Yorigin    = int(self.y - self.size/2)
        self.segments   = []

        numI = int(glyphSizeX/2) if symmetryV else glyphSizeX
        for i in range(numI):
            for j in range(glyphSizeY):
                UpRti = self.Xorigin + (i+1) * glyphPtSpc
                UpRtj = self.Yorigin + (j+1) * glyphPtSpc
                UpLti = self.Xorigin + (glyphSizeX - i) * glyphPtSpc
                UpRtj = self.Yorigin + (j+1) * glyphPtSpc
                if random.randint(0,100) < 50:      #Hori Line
                    self.segments.append([(UpRti,UpRtj),(UpRti+glyphPtSpc,UpRtj)])
                    if symmetryV: self.segments.append([(UpLti,UpRtj),(UpLti-glyphPtSpc,UpRtj)])
                if random.randint(0,100) < 65:      #Vert Line
                    self.segments.append([(UpRti,UpRtj),(UpRti,UpRtj+glyphPtSpc)])
                    if symmetryV: self.segments.append([(UpLti,UpRtj),(UpLti,UpRtj+glyphPtSpc)])
                # if random.randint(0,200) < 1:      #Diag Line
                #     self.segments.append([(UpRti,UpRtj),(UpRti+glyphPtSpc,UpRtj+glyphPtSpc)])
                #     self.segments.append([(UpLti,UpRtj),(UpLti-glyphPtSpc,UpRtj+glyphPtSpc)])
                # if random.randint(0,100) < 5:      #Diag Line
                #     self.segments.append([(UpRti+glyphPtSpc,UpRtj),(UpRti,UpRtj+glyphPtSpc)])

    def draw(self, screen):
        self.screen = screen
        self.draw_bkgnd()
        for points in self.segments:
            pygame.draw.lines(self.screen, BLACK, False, points, 3)

    def draw_bkgnd(self):
        pygame.draw.rect(self.screen, self.color , (self.Xorigin,self.Yorigin,self.size,self.size), 0)
        pygame.draw.rect(self.screen, WHITE      , (self.Xorigin,self.Yorigin,self.size,self.size), 1)

def makeGlyph(self):
    print('Hello')

################################################################################
### Main Code
################################################################################
def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [ScrWid, ScrHeight]
    screen = pygame.display.set_mode(size,flags)
    screen.set_alpha(None)

    pygame.display.set_caption("glyph Plot")
    done                    = False
    clock = pygame.time.Clock()     # Manage screen updates

    ###########################################################################
    ### Main Code
    ###########################################################################
    while not done:
        glyphArry = []
        for i in range(numCol):
            for j in range(numRow):
                xPos = int((i+1) * glyphSize + glyphSize/2)
                yPos = int((j+1) * glyphSize + glyphSize/2)
                glyphArry.append(glyph(xPos,yPos,glyphSize))

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
        screen.fill(bkgColor)              # Set the screen background
        for face in glyphArry:
            face.draw(screen)
        clock.tick(0.5)                 # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    pygame.image.save(screen, f"Glyph_{numCol}x{numRow}_{glyphSize}x{glyphSizeX}x{glyphSizeY}_SymV{symmetryV}.jpg")
    # var = input("Please enter something: ")

if __name__ == "__main__":
     main()