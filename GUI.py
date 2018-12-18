import pygame
blue=(0,0,180)
Dblue=(0,0,140)
Lblue=(0,0,255)
pygame.init()
fontTest=pygame.font.SysFont("comicsansms",30)#Creates font object

def setupBoxStrength(shadeA,shadeB,screen):
        #Draws the first box
    pygame.draw.rect(screen,shadeB,(86,346,170,90),0)#Darker box
    pygame.draw.rect(screen,shadeA,(90,350,160,80),0)
    strengthText=fontTest.render("Strength",True,(255,255,255))#creates font texts
    screen.blit(strengthText,(100,363))#"Blits" the text object to screen
def setupBoxDexterity(shadeA,shadeB,screen):
        #Draws the second box
    pygame.draw.rect(screen,shadeB,(266,346,170,90),0)#Darker box
    pygame.draw.rect(screen,shadeA,(270,350,160,80),0)
    dexterityText=fontTest.render("Dexterity",True,(255,255,255))
    screen.blit(dexterityText,(280,363))
def setupBoxIntellect(shadeA,shadeB,screen):
        #Draws the third box
    pygame.draw.rect(screen,shadeB,(446,346,170,90),0)#Darker box
    pygame.draw.rect(screen,shadeA,(450,350,160,80),0)
    intelligenceText=fontTest.render("Intellect",True,(255,255,255))
    screen.blit(intelligenceText,(470,363))
def setupPlayer(player,screen):#Sets up for first time play
    print("working")#Shows that the function is working properly
    attributes=6#number of starting attributes
    shadeSA=blue#SA and SB mean strength A and strength B.
    shadeSB=Dblue
    shadeDA=blue#DA and DB mean dexterity A and dexterity B.
    shadeDB=Dblue
    shadeIA=blue#IA and IB mean intelligence A and intelligence B.
    shadeIB=Dblue
    while attributes>0:#creates a loop so that all atttibute points get spent
        screen.fill((0,0,0))#blanks out the screen to start a new screen
        buttonA,buttonB,buttonC=pygame.mouse.get_pressed()#sets up a couple variables to store data from the mouse
        mousePosX,mousePosY=pygame.mouse.get_pos()#Gets and stores the mouse's position
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    screen.fill((255,255,255))
            elif event.type==pygame.MOUSEBUTTONUP:
                if mousePosX<258 and mousePosX>90:#checks if a box is clicked on
                    if mousePosY<450 and mousePosY>350:
                        player.strength+=1
                        attributes-=1
                elif mousePosX>266 and mousePosX<420:
                    if mousePosY<450 and mousePosY>350:
                        player.dexterity+=1
                        attributes-=1
                        print(mousePosY)
                elif mousePosX>465 and mousePosX<621:
                    if mousePosY<450 and mousePosY>350:
                        player.intelligence+=1
                        attributes-=1
                else:
                    pass
            if mousePosX<258 and mousePosX>90:#checks whether the mouse is on a box or not and changes color
                if mousePosY<450 and mousePosY>350:#checks mouse y postion. If true, make box light up
                    shadeSA=Lblue
                    shadeSB=blue
                else:#If false, turn box back to normal
                    shadeSA=blue
                    shadeSB=Dblue
            elif mousePosX>266 and mousePosX<460:
                if mousePosY<450 and mousePosY>350:
                    shadeDA=Lblue
                    shadeDB=blue
                else:
                    shadeDA=blue
                    shadeDB=Dblue
            elif mousePosX>465 and mousePosX<621:
                if mousePosY<450 and mousePosY>350:
                    shadeIA=Lblue
                    shadeIB=blue
                else:
                    shadeIA=blue
                    shadeIB=Dblue
            else:#if none is true, make all boxes normal
                shadeSA=blue
                shadeSB=Dblue
                shadeDA=blue
                shadeDB=Dblue
                shadeIA=blue
                shadeIB=Dblue
            attributeCounter=fontTest.render("you have this many points left: "+str(attributes),True,(255,255,255))#Creates words
            strengthCount=fontTest.render("Strength: "+str(player.strength),True,(255,255,255))
            dexterityCount=fontTest.render("Dexterity: "+str(player.dexterity),True,(255,255,255))
            intelligenceCount=fontTest.render("Intellect: "+str(player.intelligence),True,(255,255,255))
            screen.blit(attributeCounter,(70,20))#each of these shows what attributes you currently have
            screen.blit(strengthCount,(70,50))
            screen.blit(dexterityCount,(70,80))
            screen.blit(intelligenceCount,(70,110))
            setupBoxStrength(shadeSA,shadeSB,screen)#These create the boxes for players to click on
            setupBoxDexterity(shadeDA,shadeDB,screen)
            setupBoxIntellect(shadeIA,shadeIB,screen)#The above adds text to the screen.
            pygame.display.update()
        player.max_health=player.strength*2+1 #ensures that the player can not have 0 hp resulting in death
        player.defense=player.dexterity*2+1 
        player.mana=player.intelligence*2+1
        player.current_health=player.max_health #Makes the player start with max hit points and not none.
        player.saveCharacter()