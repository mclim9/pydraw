################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Show drawing of Sin Plots
###
### Links: 
###
################################################################################
### User Inputs
################################################################################
Radius      = 50        # lissajous Radius
dotRad      = 5         # Axis Dot Radius
Gap         = 10        # Gap Between plots
# LJx         = [1,1.5,2,2.5,3,3.5] # Freq for each X/Col
LJy         = [1,2,4]   # Freq for each Y/Row
TimeFactor  = 1       # Slow down factor
Spacing     = (Radius+Gap) * 2
################################################################################
### Code Begin
################################################################################
# numCol      = len(LJx)
numCol      = 6
numRow      = len(LJy)
ScrWid      = (numCol + 1) * Spacing
ScrHeight   = (numRow + 1) * Spacing

import pygame
import random
import math
import time
from colors import *

################################################################################
### Define colors
################################################################################
Colors  = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

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
        if len(self.ljlines) > 15000:
            self.ljlines = self.ljlines[-14990:-1]
            # self.ljlines = [(x,y),(x,y)]

    def draw(self, screen):
        pygame.draw.lines(screen, self.color, False, self.ljlines, 2)
        tuppy = self.ljlines[-1]
        pygame.draw.circle(screen, GREEN,(int(tuppy[0]),int(tuppy[1])),dotRad,1)

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

    pygame.display.set_caption("Trig Plot")
    done                 = False
    selected_lissajous   = None
    clock = pygame.time.Clock()     # Manage screen updates

    ###########################################################################
    ### Font
    ###########################################################################
    pygame.font.init() # you have to call this at the start, 
    myfont = pygame.font.SysFont('Courier', 20, bold=True)

    ###########################################################################
    ### Main Code
    ###########################################################################
    CircY = []
    for i,freq in enumerate(LJy):
        CircY.append(circleY(i))
        CircY[-1].b = freq

    TrigPlots = [[lissajous(1,1)] * numRow for i in range(numCol)]
    for j,row in enumerate(CircY):
        temp = lissajous(2,j)
        TrigPlots[j] = temp

    toffset = 0
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
        screen.fill(BLACK)                                  # Screen background
        t = pygame.time.get_ticks()/1000 * TimeFactor

        for circYObj in CircY:                              # Draw Left Circle
            circYObj.newRadius(t)
            circYObj.draw(screen)

        for j in range(numRow):                             # Draw plot
            Xpos = Spacing + (t-toffset) * 20
            if Xpos > ScrWid-Gap:
                toffset = t
            Xpos = Spacing + (t-toffset) * 20

            TrigPlots[j].addsegment(Xpos,CircY[j].endY)
            TrigPlots[j].draw(screen)

        outText = f"FPS:{clock.get_fps():.2f}"
        textsurface = myfont.render(outText, True, WHITE)   # Render Text
        clock.tick(60)                                      # Limit to 60 fps
        screen.blit(textsurface,(0,0))                      # Draw text
        pygame.display.update()                             # Display drawing to screen
    #End While
    pygame.quit()
 
if __name__ == "__main__":
     main()