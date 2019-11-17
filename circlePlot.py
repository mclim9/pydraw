################################################################################
### Date: 2019.10.28
### Author: Martin C Lim
### Version: 0.1
### Description: Show drawing of Lissajous
###
### Links: 
###
################################################################################
### User Inputs
################################################################################
ScrWid      = 300
ScrHeight   = 300
MaxSpeed    = 4         # Maximum lissajous speed.
Radius      = 30
a           = 1
b           = 1
################################################################################
### Code Begin
################################################################################
import pygame
import random
import math
import time

################################################################################
### Define colors
################################################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0,0,255)
Colors = [RED,GREEN,GREEN,BLUE,WHITE]

from pygame.locals import DOUBLEBUF, FULLSCREEN
# flags = FULLSCREEN | DOUBLEBUF
flags = DOUBLEBUF
#screen = pygame.display.set_mode(resolution, flags, bpp)

################################################################################
### Definitions
################################################################################
class circles:
    def __init__(self):
        self.ljlines    = []
        self.color      = WHITE

    def addsegment(self,x,y):
        self.ljlines.append([x,y])

    def draw(self, screen):
        #(surface, color, closed, points, blend)
        pygame.draw.lines(screen, self.color, False, self.ljlines, 1)

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
    done            = False
    clock = pygame.time.Clock()     # Manage screen updates

    #############################################################################
    ### Font
    #############################################################################
    pygame.font.init() # you have to call this at the start, 
    myfont = pygame.font.SysFont('Courier', 24, bold=True)

    ###########################################################################
    ### Main Code
    ###########################################################################
    while not done:
        #######################################################################
        ### Event Processing
        #######################################################################
        #pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #######################################################################
        ### Drawing Code
        #######################################################################
        # t = totTime + clock.tick(60)/1000.0 # Limit to 60 frames per second
        t = pygame.time.get_ticks()/1000
        screen.fill(BLACK)                # Set the screen background
        x = Radius * math.sin(a*t)+ Radius
        y = Radius * math.cos(b*t)+ Radius
        # print(f'x:{x},y:{y}')
        # pygame.draw.circle(screen, color, (x,y), radius, thickness)
        pygame.draw.circle(screen, WHITE,(Radius,Radius),Radius,1)
        pygame.draw.aalines(screen, WHITE, False, [(Radius,Radius),(x,y),(ScrWid,y)], 1)

        outText = "lissajouss:%d FPS:%.2f"%(len([0,0]),clock.get_fps())
        textsurface = myfont.render(outText, True, (255, 255, 255)) #render
        screen.blit(textsurface,(0,0))  # Draw text
        pygame.display.update()         # update the screen with what we've drawn.
    #End While
    pygame.quit()
 
if __name__ == "__main__":
     main()
