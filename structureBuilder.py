import random
from shapely.geometry import *

class structureBuilder(object):
    wallPath=[]

    innerBounds = Polygon([(3,3),(3,-3),(-3,-3),(-3,3)])
    outerBounds = Polygon([(10,10),(10,-10),(-10,-10),(-10,10)])

    zeroPoint = (0,6)
    startingPoint = (0,4)

    def normal(self,p1,p2):
        a=p1[0]-p2[0]
        b=p1[1]-p2[1]
        return (-b,a)

    def rollDistance(self):
        return random.randint(2,8)
        #return 5

    def wallSection(self,startingPoint,direction,distance,wasCollision):
        x=0
        y=0
        if wasCollision:
            flow = self.normal(startingPoint,(0,0))
            if(random.random()>0.5):
                direction = (flow[0],0)
            else:
                direction = (0,flow[1])
        
        if random.random()<self.turnOdds:
            #follow the normal vector.
            if direction[0]!=0: x=distance*abs(direction[0])/direction[0]
            if direction[1]!=0: y=distance*abs(direction[1])/direction[1]
        else:
            #invert the normal vector.
            if direction[0]!=0: x=-distance*abs(direction[0])/direction[0]
            if direction[1]!=0: y=-distance*abs(direction[1])/direction[1]
        return (x + startingPoint[0],y + startingPoint[1]) #returns ending point

    def isInBounds(self,p):
        point = Point(p)
        return point.within(self.outerBounds) and not point.within(self.innerBounds)

    def __init__(self,seed,isSymmetric,turnOdds):
        self.turnOdds= 0.9 #Range from 0 to 1 affecting how often the algorithm will generate right turns.  Maybe change to range of -1 to 1 range?
        random.seed(seed)
        self.isSymmetric=isSymmetric

    def generate(self):
        pLast = self.zeroPoint
        pCurr = self.startingPoint
        self.wallPath.append(pCurr)
        wasCollision = False
        for num in range(4):
            distance = self.rollDistance()
            pNew = self.wallSection(pCurr,self.normal(pCurr,pLast),distance,wasCollision)
            print("pcurr: {0}, pLast: {1}, pNew: {2} ".format(pCurr,pLast,pNew))
            wasCollision = False # reset to False for the next one.
            overShoot = 0
            while(self.isInBounds(pNew)==False):
                pNew = self.wallSection(pCurr,self.normal(pCurr,pLast),distance-overShoot,wasCollision)
                overShoot+=1
                wasCollision = True
            pLast = pCurr
            pCurr = pNew
            self.wallPath.append(pCurr)

            

    def setInnerBounds(self):
        print("Setting inner bounds.")

    def setOuterBounds(self):
        print("Setting outer bounds.")

    def reflect(self):
        #only mirrors the x point right now.
        reversedPath = self.wallPath[::-1]
        invertedPath = []
        for point in reversedPath:
            invertedPath.append((-point[0],point[1]))
        return invertedPath