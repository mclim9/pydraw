################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Show drawing of Lissajous Plots
###
### Links: 
###
################################################################################
### User Inputs
################################################################################
Radius      = 50        # lissajous Radius
dotRad      = 5         # Axis Dot Radius
Gap         = 10        # Gap Between plots
LJx         = [1,1.5,2,2.5,3,3.5] # Freq for each X/Col
LJy         = [1,2,4]   # Freq for each Y/Row
TimeFactor  = 0.5       # Slow down factor

################################################################################
### Code Begin
################################################################################
numCol      = len(LJx)
numRow      = len(LJy)
ScrWid      = (numCol + 1) * (Radius+Gap) * 2
ScrHeight   = (numRow + 1) * (Radius+Gap) * 2

import pygame
import random
import math
import time
from colors import *

################################################################################
### Define colors
################################################################################
Colors  = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]

from pygame.locals import DOUBLEBUF, FULLSCREEN
# flags = FULLSCREEN | DOUBLEBUF
flags = DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Definitions
################################################################################
class lissajous:
    ###Class to keep track of a each lissajous plot
    def __init__(self,col,row):
        self.color      = random.choice(Colors)
        self.centerX    = (col + 1) * (Radius + Gap) * 2 + Radius 
        self.centerY    = (row + 1) * (Radius + Gap) * 2 + Radius 
        # self.ljlines    = [(self.centerX,self.centerY)]
        self.ljlines    = []

    def addsegment(self,x,y):
        self.ljlines.append((x,y))
        if len(self.ljlines) == 1:
            self.ljlines.append((x,y))
        if len(self.ljlines) > 1500:
            self.ljlines = self.ljlines[-1490:-1]
            # self.ljlines = [(x,y),(x,y)]

    def draw(self, screen):
        pygame.draw.lines(screen, self.color, False, self.ljlines, 2)
        tuppy = self.ljlines[-1]
        pygame.draw.circle(screen, GREEN,(int(tuppy[0]),int(tuppy[1])),dotRad,1)


class circleX:
    def __init__(self,col):
        self.ljlines    = []
        self.color      = WHITE         #Lissajous
        self.a          = 1             #Frequency multiplier
        self.centerX    = (col + 1) * (Radius + Gap) * 2 + Radius 
        self.centerY    = Radius
        self.endX       = 0
        self.endY       = 0

    def newRadius(self,t):
        # t = pygame.time.get_ticks()/1000
        self.endX = Radius * math.sin(self.a*t)+ self.centerX
        self.endY = Radius * math.cos(self.a*t)+ self.centerY

    def draw(self, screen):
        #(surface, color, closed, points, blend)
        pygame.draw.circle(screen, WHITE,(self.centerX,self.centerY),Radius,1)
        pygame.draw.circle(screen, BLUE, (int(self.endX),int(self.endY)),dotRad,1)
        pygame.draw.aalines(screen, GREY, False, [(self.centerX,self.centerY),(self.endX,self.endY),(self.endX,ScrHeight-2*Gap)], 1)

class circleY:
    def __init__(self,row):
        self.ljlines    = []
        self.color      = WHITE
        self.b          = 1
        self.centerX    = Radius
        self.centerY    = (row + 1) * (Radius + Gap) * 2 + Radius 
        self.endX       = 0
        self.endY       = 0

    def newRadius(self,t):
        # t = pygame.time.get_ticks()/1000
        self.endX = Radius * math.sin(self.b*t)+ self.centerX
        self.endY = Radius * math.cos(self.b*t)+ self.centerY
        # self.ljlines.append((x,y)

    def draw(self, screen):
        #(surface, color, closed, points, blend)
        pygame.draw.circle(screen, WHITE,(self.centerX,self.centerY),Radius,1)
        pygame.draw.circle(screen, BLUE, (int(self.endX),int(self.endY)),dotRad,1)
        pygame.draw.aalines(screen, GREY, False, [(self.centerX,self.centerY),(self.endX,self.endY),(ScrWid-2*Gap,self.endY)], 2)

################################################################################
### Main Code
################################################################################
def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [ScrWid, ScrHeight]
    screen = pygame.display.set_mode(size,flags)
    screen.set_alpha(None)

    pygame.display.set_caption("Lissajous Plot")
    done                 = False
    selected_lissajous   = None
    clock = pygame.time.Clock()     # Manage screen updates

    #############################################################################
    ### Font
    #############################################################################
    pygame.font.init() # you have to call this at the start, 
    myfont = pygame.font.SysFont('Courier', 20, bold=True)

    ###########################################################################
    ### Main Code
    ###########################################################################
    CircX = []
    for i,freq in enumerate(LJx):
        CircX.append(circleX(i))
        CircX[-1].a = freq

    CircY = []
    for i,freq in enumerate(LJy):
        CircY.append(circleY(i))
        CircY[-1].b = freq

    LJPlots = [[lissajous(1,1)] * numRow for i in range(numCol)]
    for i,col in enumerate(CircX):
        for j,row in enumerate(CircY):
            temp = lissajous(i,j)
            LJPlots[i][j] = temp

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
        t = pygame.time.get_ticks()/1000 * TimeFactor
        for circXObj in CircX:
            circXObj.newRadius(t)
            circXObj.draw(screen)

        for circYObj in CircY:
            circYObj.newRadius(t)
            circYObj.draw(screen)

        for i in range(numCol):
            for j in range(numRow):
                LJPlots[i][j].addsegment(CircX[i].endX,CircY[j].endY)
                LJPlots[i][j].draw(screen)

        outText = f"FPS:{clock.get_fps():.2f}"
        textsurface = myfont.render(outText, True, WHITE) #render
        clock.tick(60)                  # Limit to 60 frames per second
        screen.blit(textsurface,(0,0))  # Draw text
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    pygame.quit()
 
if __name__ == "__main__":
     main()