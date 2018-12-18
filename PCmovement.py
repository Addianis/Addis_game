#movement
import pygame
import gameClasses
#character=gameClasses.Player()
def Movement(character):
    move=2
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                character.facing="up"
                if character.posY-move<0:
                    character.posY=0
                else:
                    character.posY-=move
                    character.moving=True
                print('up')
            elif event.key==pygame.K_DOWN:
                character.facing="down"
                if character.posY+move>465:
                    character.posY=465
                else:
                    character.moving=True
                    character.posY+=move
                print('down')
            elif event.key==pygame.K_LEFT:
                character.facing="left"
                if character.posX-move<0:
                    character.PosX=0
                else:
                    character.moving=True
                    character.posX-=move
                print('left')
            elif event.key==pygame.K_RIGHT:
                character.facing="right"
                if character.posX+move>670:
                    character.posX=670
                else:
                    character.moving=True
                    character.posX+=move
                print('right')
            elif event.key==pygame.K_SPACE:
                pass
            if character.moveCount<40:
                character.moveCount=character.moveCount+1
            else:
                character.moveCount=0
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                pass
            elif event.key==pygame.K_UP:
                character.facing="up"
                character.moving=False
            elif event.key==pygame.K_DOWN:
                character.facing="down"
                character.moving=False
            elif event.key==pygame.K_LEFT:
                character.facing="left"
                character.moving=False
            elif event.key==pygame.K_RIGHT:
                character.facing="right"
                character.moving=False
