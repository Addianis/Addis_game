#movement
import pygame
import Classes
character=Classes.Player()
def Movement():
    print "Working"
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                character.facing="up"
                if character.posY-move<0:
                    character.posY=0
                else:
                    character.posY-=move
                    character.moving=True
            elif event.key==pygame.K_DOWN:
                character.facing="down"
                if character.posY+move>465:
                    character.posY=465
                else:
                    character.moving=True
                    character.posY+=move
            elif event.key==pygame.K_LEFT:
                character.facing="left"
                if character.posX-move<0:
                    character.PosX=0
                    print"working"
                else:
                    character.moving=True
                    character.posX-=move
            elif event.key==pygame.K_RIGHT:
                character.facing="right"
                if character.posX+move>670:
                    character.posX=670
                else:
                    character.moving=True
                    character.posX+=move
            elif event.key==pygame.K_SPACE:
                pass
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
