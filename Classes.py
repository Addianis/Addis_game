import pygame
playerSpriteSheet=pygame.image.load("Player.png")
clock=pygame.time.Clock()
green=(0,255,0)
color=(255,0,0)
blue=(0,0,180)
Dblue=(0,0,140)
Lblue=(0,0,255)
move=2
movement=[]
increment=10
class Player():
    posX=350
    posY=250#Inital starting point
    def __init__(self):
        self.level=1
        self.current_health=0#current health is used to keep track of damage
        self.max_health=0#max health allows players to heal to the correct amount
        self.attack=0#not yet implemented
        self.defense=0
        self.exp=0
        self.inventory=[]#list of items the player will hold. Still need to decide item type
        self.mana=0
        self.strength=0#attributes
        self.dexterity=0
        self.intelligence=0
        self.moving=False
        self.moveCount=0
        self.moveUp=[]
        self.moveDown=[]
        self.moveLeft=[]
        self.moveRight=[]
        self.facing='down'
    def updatePlayer(self):
        playerAnimation=[]#set up motion cycle list
        if self.facing=='up':
            playerAnimation=self.moveUp[1]
        elif self.facing=='down':
            playerAnimation=self.moveDown[1]
        elif self.facing=='left':
            playerAnimation=self.moveLeft[1]
        elif self.facing=='right':
            playerAnimation=self.moveRight[1]
        if self.moving==True:#sets up correct player animation for when moving
            if self.facing=='up':
                if self.moveCount<movement[0]:
                    playerAnimation=self.moveUp[0]
                elif self.moveCount>movement[0] and self.moveCount<movement[1]:
                    playerAnimation=self.moveUp[1]
                elif self.moveCount>movement[1] and self.moveCount<movement[2]:
                    playerAnimation=self.moveUp[2]
                elif movement[3]>self.moveCount and self.moveCount>movement[2]:
                    playerAnimation=self.moveUp[1]
                elif self.moveCount>movement[3]and self.moveCount<movement[4]:
                    playerAnimation=self.moveUp[0]
            if self.facing=='down':
                if self.moveCount<movement[0]:
                    playerAnimation=self.moveDown[0]
                elif self.moveCount>movement[0] and self.moveCount<movement[1]:
                    playerAnimation=self.moveDown[1]
                elif self.moveCount>movement[1] and self.moveCount<movement[2]:
                    playerAnimation=self.moveDown[2]
                elif movement[3]>self.moveCount and self.moveCount>movement[2]:
                    playerAnimation=self.moveDown[1]
                elif self.moveCount>movement[3] and self.moveCount<movement[4]:
                    playerAnimation=self.moveDown[0]
            if self.facing=='left':
                if self.moveCount<movement[0]:
                    playerAnimation=self.moveLeft[0]
                elif self.moveCount>movement[0] and self.moveCount<movement[1]:
                    playerAnimation=self.moveLeft[1]
                elif self.moveCount>movement[1] and self.moveCount<movement[2]:
                    playerAnimation=self.moveLeft[2]
                elif movement[3]>self.moveCount and self.moveCount>movement[2]:
                    playerAnimation=self.moveLeft[1]
                elif self.moveCount>movement[3] and self.moveCount<movement[4]:
                    playerAnimation=self.moveLeft[0]
            if self.facing=='right':
                if self.moveCount<movement[0]:
                    playerAnimation=self.moveRight[0]
                elif self.moveCount>movement[0] and self.moveCount<movement[1]:
                    playerAnimation=self.moveRight[1]
                elif self.moveCount>movement[1] and self.moveCount<movement[2]:
                    playerAnimation=self.moveRight[2]
                elif movement[3]>self.moveCount and self.moveCount>movement[2]:
                    playerAnimation=self.moveRight[1]
                elif self.moveCount<movement[4]:
                    playerAnimation=self.moveRight[0]
        screen.blit(playerSpriteSheet,(self.posX,self.posY),playerAnimation)
    def setupPlayer(self):#Sets up for first time play
        for x in range(0,3):#need to find out what it does
            self.moveDown.append((x*32,0,32,32))
            self.moveLeft.append((x*32,32,32,32))
            self.moveRight.append((x*32,64,32,32))
            self.moveUp.append((x*32,98,32,32))
        print "working"#Shows that the function is working properly
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
                            self.strength+=1
                            attributes-=1
                    elif mousePosX>266 and mousePosX<420:
                        if mousePosY<450 and mousePosY>350:
                            self.dexterity+=1
                            attributes-=1
                            print mousePosY
                    elif mousePosX>465 and mousePosX<621:
                        if mousePosY<450 and mousePosY>350:
                            self.intelligence+=1
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
            strengthCount=fontTest.render("Strength: "+str(self.strength),True,(255,255,255))
            dexterityCount=fontTest.render("Dexterity: "+str(self.dexterity),True,(255,255,255))
            intelligenceCount=fontTest.render("Intellect: "+str(self.intelligence),True,(255,255,255))
            screen.blit(attributeCounter,(70,20))#each of these shows what attributes you currently have
            screen.blit(strengthCount,(70,50))
            screen.blit(dexterityCount,(70,80))
            screen.blit(intelligenceCount,(70,110))
            setupBoxStrength(shadeSA,shadeSB)#These create the boxes for players to click on
            setupBoxDexterity(shadeDA,shadeDB)
            setupBoxIntellect(shadeIA,shadeIB)#The above adds text to the screen.
            pygame.display.update()
        self.max_health=self.strength*2+1 #ensures that the player can not have 0 hp resulting in death
        self.defense=self.dexterity*2+1 
        self.mana=self.intelligence*2+1
        self.current_health=self.max_health #Makes the player start with max hit points and not none.


def Test():
    print "test went well"

Test()
