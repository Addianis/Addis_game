#This class handles sprite sheets
#From ww.scriptefun.com/transcript-2-using
#sprite-sheets-and-drawing-the-background
#Note: When calling images_at the rect is the format:
#(x,y,x+offset,y+offset)

import pygame
height=500
length=700
winSize=(length,height)
screen=pygame.display.set_mode((winSize),0,32)
playerImage=pygame.image.load("player.png")
walkingDown=[]
walkingUp=[]
walkingLeft=[]
walkingRight=[]
for x in range(0,3):
    #Gets all the spirit images locations and creates a usable list
    walkingDown.append((x*32,0,32,32))
    walkingLeft.append((x*32,32,32,32))
    walkingRight.append((x*32,64,32,32))
    walkingUp.append((x*32,98,32,32))
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet=pygame.image.load(filename).convert()
            #not entirely sure, but it gets the image for sprites
        except pygame.error:
            print('unable to loa spritesheet image:',filename)
            raise SystemExit
        def image_at(self, rectangle, colorkey=None):
            #loads image from x,y,x+offset,y+offset
            rect=pygame.Rect(rectangle)
            image=pygame.Surface(rect.size).convert()
            image.blit(self.sheet,(0,0),rect)
            if colorkey is not None:
                if colorkey is -1:
                    colorkey=image.get_at((0,0))
                image.set_colorkey(colorkey,pygame.RLEACCEL)
            return image
        def images_at(self, rects, colorkey=None):
            #loads a lot of images and returns a list
            return [self.image_at(rect, colorkey) for rect in rects]
        def load_strip(self,rect,image_count,colorkey=None):
            tups=[(rect[0]+rect[2]*x, rect[1], rect[2],rect[3])
                  for x in range(image_cout)]
            return self.images_at(tups, colorkey)
if __name__=='__main__':
    screen.blit(playerImage,[0,50],walkingDown[0])
    screen.blit(playerImage,[50,50],walkingDown[1])
    screen.blit(playerImage,[100,50],walkingDown[2])
    screen.blit(playerImage,[0,100],walkingLeft[0])
    screen.blit(playerImage,[50,100],walkingLeft[1])
    screen.blit(playerImage,[100,100],walkingLeft[2])
    screen.blit(playerImage,[0,150],walkingRight[0])
    screen.blit(playerImage,[0,200],walkingUp[0])
    screen.blit(playerImage,[50,200],walkingUp[1])
    screen.blit(playerImage,[100,200],walkingUp[2])
    
    pygame.display.update()

