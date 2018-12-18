import pygame, sys, random, os
from pygame.locals import *
pygame.init()
y=776
x=10
winWidth=600
winHeight=800
white=(255,255,255)
black=(0,0,0)
speech=[]
test=0
texts=open('Intro.txt','r')
text=texts.readlines()
texts.close()
DISPLAYSURF=pygame.display.set_mode((winWidth,winHeight))
fontObj=pygame.font.Font('freesansbold.ttf',24)
pygame.display.set_caption('Arisen Storm')
scrollRate=4
timer=0
line=0
while True:
    lineA=fontObj.render(text[line],True,white)#Creates text surface object
    lineB=fontObj.render(text[line+1],True,white)
    lineC=fontObj.render(text[line+2],True,white)
    DISPLAYSURF.fill(black)
    DISPLAYSURF.blit(lineA,(x,y))
    DISPLAYSURF.blit(lineB,(x,y+28))
    DISPLAYSURF.blit(lineC,(x,y+56))
    if timer==scrollRate:
        y-=1
        timer=0
        if y<-56:
            y=799
            if line+3>len(text):
                print len(text)
            else:
                line=line+3
    else:
        timer=timer+1
    pygame.display.update()
