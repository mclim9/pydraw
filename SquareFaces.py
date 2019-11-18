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
### Definitions
################################################################################
class squareFace:
    ###Class to keep track of a each squareFace plot
    def __init__(self,xPos,yPos,Size):
        self.size       = Size
        self.color      = random.choice(Colors)
        self.x          = int(xPos)
        self.y          = int(yPos)
        self.eyeType    = random.choice(Eyes)
        self.eyeSize    = int(self.size/10)
        self.eyePupil   = int(self.eyeSize*random.choice(Pupils))
        if self.size < 20:
            self.eyeType    = 'Small'
            self.eyeSize    = 1
            self.eyePupil   = 1

    def draw(self, screen):
        self.screen = screen
        self.draw_face()
        self.draw_eyes()
        self.draw_mouth()

    def draw_face(self):
        rectX = int(self.x - self.size/2)
        rectY = int(self.y - self.size/2)
        pygame.draw.rect(self.screen, self.color , (rectX,rectY,self.size,self.size), 0)
        pygame.draw.rect(self.screen, WHITE      , (rectX,rectY,self.size,self.size), 1)

    def draw_eyes(self):
        eyeOffX = int(self.size/5)
        if random.randint(0,100) > 10:
            """Draw eyes w/ pupil"""
            self.draw_eyeCircle(self.x + eyeOffX, self.y, self.eyeSize,  WHITE)
            self.draw_eyeCircle(self.x - eyeOffX, self.y, self.eyeSize,  WHITE)
            self.draw_eyeCircle(self.x + eyeOffX, self.y, self.eyePupil, BLACK)
            self.draw_eyeCircle(self.x - eyeOffX, self.y, self.eyePupil, BLACK)
        else:
            """Draw eyes closed"""
            pygame.draw.aaline(self.screen, BLACK, (self.x - eyeOffX - self.eyeSize, self.y), (self.x - eyeOffX + self.eyeSize, self.y), 1)
            pygame.draw.aaline(self.screen, BLACK, (self.x + eyeOffX + self.eyeSize, self.y), (self.x + eyeOffX - self.eyeSize, self.y), 1)

    def draw_eyeCircle(self, x, y, radius, color):
        if radius > 1:
            pygame.gfxdraw.filled_circle(self.screen, x, y, radius, color)      #Draw filled in circle
        pygame.gfxdraw.aacircle(self.screen, x, y, radius, color)           #AntiAlias edge

    def draw_mouth(self):
        mouthArry = ['open','line','smile','dot','open','line','smile','open','line','smile','dot']
        mouth = random.choice(mouthArry)
        mouthSize = int(self.size/20)
        if self.size < 20:
            mouthSize = 2
            mouth     = 'dot'
        if mouth == 'open':
            mouthOff = int(self.size/5)
            pygame.gfxdraw.filled_circle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
            pygame.gfxdraw.aacircle( self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
        elif mouth == 'line':
            mouthOff = int(self.size/5)
            pygame.draw.aaline(self.screen, BLACK,(self.x-mouthSize,self.y+mouthOff),(self.x+mouthSize,self.y+mouthOff)) 
        elif mouth == 'smile':
            mouthOff = int(self.size/10)
            pygame.draw.arc(self.screen, BLACK,[self.x-mouthSize, self.y+mouthOff, mouthSize*2, mouthSize*3], pi, 0, 1)
        elif mouth == 'dot':
            mouthOff = int(self.size/5)
            mouthSize = int(mouthSize/2)
            pygame.gfxdraw.filled_circle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
            pygame.gfxdraw.aacircle(self.screen, self.x, self.y+mouthOff,mouthSize,BLACK)
        else:
            pygame.draw.aaline(screen, BLACK,(self.x-mouthSize,self.y+mouthOff),(self.x+mouthSize,self.y+mouthOff)) 

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
        screen.fill(BLACK)              # Set the screen background
        for face in SmilyArry:
            face.draw(screen)
        clock.tick(0.5)                  # Limit to 60 frames per second
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    # var = input("Please enter something: ")
 
if __name__ == "__main__":
     main()