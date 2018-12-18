import pygame
import SpriteSheetLoad
import hitBox
print("Starting game")
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
saveState=["level",
       'current hp',
       'max hp',
       'exp',
       'mana',
       'strength',
       'dexterity',
       'intelligence',
       ]
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
        self.moveUp=SpriteSheetLoad.walkingUp
        self.moveDown=SpriteSheetLoad.walkingDown
        self.moveLeft=SpriteSheetLoad.walkingLeft
        self.moveRight=SpriteSheetLoad.walkingRight
        self.facing='down'
        self.stats=stats=[self.level,
               self.current_health,           
               self.max_health,
               self.attack,
               self.defense,
               self.exp,
               self.mana,
               self.strength,
               self.dexterity,
               self.intelligence]
        self.animationStep=self.moveDown[2]
        self.hitBox=hitBox.hitBox(self.posX,self.posY,60,60)           
    def updatePlayer(self):
        self.hitBox.xUpper=self.posX
        self.hitBox.yUpper=self.posY
        if self.moving==False:
            if self.facing=='up':
                self.animationStep=self.moveUp[1]
            if self.facing=='down':
                self.animationStep=self.moveDown[1]
            elif self.facing=='left':
                self.animationStep=self.moveLeft[1]
            elif self.facing=='right':
                self.animationStep=self.moveRight[1]
        if self.moving==True:#sets up correct player animation for when moving
            if self.facing=='up':
                if self.moveCount<increment:
                    self.animationStep=self.moveUp[0]
                elif self.moveCount<increment*2 and self.moveCount>=increment:
                    self.animationStep=self.moveUp[1]
                elif self.moveCount<increment*3 and self.moveCount>=increment*2:
                    self.animationStep=self.moveUp[2]
                elif self.moveCount<increment*4 and self.moveCount>=increment*3:
                    self.animationStep=self.moveUp[1]
                elif self.moveCount<increment*5 and self.moveCount>=increment*4:
                    self.animationStep=self.moveUp[0]
            if self.facing=='down':
                if self.moveCount<increment:
                    self.animationStep=self.moveDown[0]
                elif self.moveCount<increment*2 and self.moveCount>=increment:
                    self.animationStep=self.moveDown[1]
                elif self.moveCount<increment*3 and self.moveCount>=increment*2:
                    self.animationStep=self.moveDown[2]
                elif self.moveCount<increment*4 and self.moveCount>=increment*3:
                    self.animationStep=self.moveDown[1]
                elif self.moveCount<increment*5 and self.moveCount>=increment*4:
                    self.animationStep=self.moveDown[0]
            if self.facing=='left':
                if self.moveCount<increment:
                    self.animationStep=self.moveLeft[0]
                elif self.moveCount<increment*2 and self.moveCount>=increment:
                    self.animationStep=self.moveLeft[1]
                elif self.moveCount<increment*3 and self.moveCount>=increment*2:
                    self.animationStep=self.moveLeft[2]
                elif self.moveCount<increment*4 and self.moveCount>=increment*3:
                    self.animationStep=self.moveLeft[1]
                elif self.moveCount<increment*5 and self.moveCount>=increment*4:
                    self.animationStep=self.moveLeft[0]
            if self.facing=='right':
                if self.moveCount<increment:
                    self.animationStep=self.moveRight[0]
                elif self.moveCount<increment*2 and self.moveCount>=increment:
                    self.animationStep=self.moveRight[1]
                elif self.moveCount<increment*3 and self.moveCount>=increment*2:
                    self.animationStep=self.moveRight[2]
                elif self.moveCount<increment*4 and self.moveCount>=increment*3:
                    self.animationStep=self.moveRight[1]
                elif self.moveCount<increment*5 and self.moveCount>=increment*4:
                    self.animationStep=self.moveRight[0]
            
    def setupPlayer(self):#Sets up for first time play
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
                            self.strength+=1
                            attributes-=1
                    elif mousePosX>266 and mousePosX<420:
                        if mousePosY<450 and mousePosY>350:
                            self.dexterity+=1
                            attributes-=1
                            print(mousePosY)
                    elif mousePosX>465 and mousePosX<621:
                        if mousePosY<450 and mousePosY>350:
                            intelligence+=1
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
        self.saveCharacter()
    def saveCharacter(self):
        save=open('save.txt')
        profile=save.read()
class createBuildings():
    def __init__(self,posX,posY,length,height,passable):
        self.posX=posX
        self.posY=posY
        self.length=length
        self.height=height
        self.passable=passable
        self.color=(235,235,235)
        self.construction=(posX,posY,length,height)
        self.hitBox=hitBox.hitBox(posX,posY,length,height)
        

def Test():
    print("test went well")
    building=createBuildings(20,20,20,20,False)
    print(building.passable)
def updateCharacter(player):
    print("saving character")
    save=open('save.txt','r+')
    if save.readline()=="old":
        print("updating character")
        save.write(str(player.level))
    else:
        print("creating new character")
        save.write("old")
        save.write(str(player.level))
    save.read()
    save.close()
character=Player()
print(character.hitBox)
character.saveCharacter()
#character.printCharacter()
#character.level=5
#character.saveCharacter()
#save=open("save.txt",'w')
#save.write("moron")
#save.close()


