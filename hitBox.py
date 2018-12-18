#Hit boxes
#Another list but where the heavy checking will take place
#hitBox auto adds object to hitBoxList
possibleHitList=[]
hitBoxList=[]
class hitBox():
    def __init__(self,xUpper=0,yUpper=0,length=0,height=0):#currently only have the math to set up a box
        self.xUpper=xUpper
        self.yUpper=yUpper
        self.length=length
        self.height=height
        self.xPos=self.xUpper+(self.length/2)
        self.yPos=self.yUpper-(self.height/2)
        hitBoxList.append(self)
    def __str__(self):
        box='hit box at {0} and {1}'.format(self.xUpper,self.yUpper)
        return box
def detectPossibleCollision(objects):
    for item in range(len(objects)):
        try:
            if objects[item].xPos-objects[item+1].xPos<=5 and objects[item].xPos-objects[item+1].xPos>=-5:
                possibleHitList.append((objects[item],objects[item+1]))
                print("Objects added to possible detection list")
        except IndexError:
            print("index out of range but still works")
            pass
def detectCollision(objects):
    test=[]
    intersects=[]
    for item in objects:
        test.append(item[0])
        test.append(item[1])
        aCords=[]
        bCords=[]
        print("pre-for loop")
        print(item[0])
        print(item[1])
        forRangeXA=test[0].xUpper+test[0].length
        forRangeYA=test[0].yUpper+test[0].length
        if forRangeXA<1:
            forRangeXA=1
        if forRangeYA<1:
            forRangeYA=1
        forRangeXB=test[1].xUpper+test[1].length
        forRangeYB=test[1].yUpper+test[1].length
        if forRangeXB<1:
            forRangeXB=1
        if forRangeYB<1:
            forRangeYB=1
        for z in range(test[0].xUpper, forRangeXA):
            print("Plop")
            for v in range(test[0].yUpper,forRangeYA):
                print('bloop')
                aCords.append((z,v))
        for z in range(test[1].xUpper, forRangeXB):
            for v in range(test[1].yUpper,forRangeYB):
                bCords.append((z,v))
        print(aCords)
        print(bCords)
        meets=False
        for corda in aCords:
            if meets==True:
                break
            for cordb in bCords:
                if meets==True:
                    break
                if corda[0]==cordb[0] or corda[1]==cordb[1]:
                    intersect=cordb
                    print(intersect)
                    print("Intersect found")
                    meets=True
        if meets==True:
            intersects.append((item,True))
box=hitBox()
box2=hitBox(20,3,2)
box3=hitBox(20,20,2)
box4=hitBox(19,20,3)
detectPossibleCollision(hitBoxList)
detectCollision(possibleHitList)
