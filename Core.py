import pygame
import gameClasses #will house the game classes such as building, player and npc
import PCmovement #Will house all functions related to player movement
import SpriteSheetLoad #Loads sprite sheets for use of gameClasses
import hitBox #hitBox houses custom code for telling if a sprite can interact with another
import GUI #will house all functions for creating GUI aspects of the game such as buttons

pygame.init()
pygame.key.set_repeat(10,10) #allows for keys to repeat

height=500 #will eventually add an option for varying sizes
length=700
winSize=(length,height)
screen=pygame.display.set_mode((winSize),0,32)

gameClasses.Test() #Makes sure that things work within the gameClasses file

building=gameClasses.createBuildings(30,30,30,30,False) #Sample building for working on interactions
character=gameClasses.Player() #Creates the actual player. Will eventually chnage how this works

possibleHitList=[] #Global list for  potetional interactions to save on memory
mainBox=hitBox.hitBox(-5,-5,-5,-5) #generates hitbox for interaction testing

GUI.setupPlayer(character,screen) #Sets player up for first time play
spriteList=[building,character]

while True: #main game loop
    hitBox.detectPossibleCollision(spriteList)
    hitBox.detectCollision(possibleHitList)
    character.updatePlayer()
    screen.fill((255,255,255))
    PCmovement.Movement(character)
    screen.blit(SpriteSheetLoad.playerImage,[character.posX,character.posY],character.animationStep)
    pygame.draw.rect(screen,(building.color),(building.construction),0)
    pygame.display.update()
