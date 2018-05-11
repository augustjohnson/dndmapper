import random
from shapely.geometry import *

class structureBuilder(object):
    wallPath=[]

    zeroPoint = (0,6)
    startingPoint = (0,5)

    def normal(self,p1,p2):
        a=p1[0]-p2[0]
        b=p1[1]-p2[1]
        return (-b,a)

    def rollDistance(self):
        roll=random.randint(1,6)
        #print("Roll:{0}".format(roll))
        return roll

    def wallSection(self,start,direction,distance,wasCollision):
        x=0
        y=0
        if wasCollision:
            flow = self.normal(start,(0,0))
            #print("There was a collision.  Flow:{0}".format(flow))
            if(random.random()>0.5):
                direction = (flow[0],0)
            else:
                direction = (0,flow[1])
        
        if random.random()<self.turnOdds:
            #print("follow the normal vector. Turnodds:{0}".format(self.turnOdds))
            if direction[0]!=0: x=distance*abs(direction[0])/direction[0]
            if direction[1]!=0: y=distance*abs(direction[1])/direction[1]
        else:
            #print("#invert the normal vector.")
            if direction[0]!=0: x=-distance*abs(direction[0])/direction[0]
            if direction[1]!=0: y=-distance*abs(direction[1])/direction[1]
        return (x + start[0],y + start[1]) #returns ending point

    def isInBounds(self,p):
        point = Point(p)
        return point.within(self.outerBounds) and not point.within(self.innerBounds)

    def __init__(self,seed,isSymmetric,turnOdds,innerBoundsR,outerBoundsR):
        self.turnOdds= turnOdds #Range from 0 to 1 affecting how often the algorithm will generate right turns.  Maybe change to range of -1 to 1 range?
        random.seed(seed)
        self.isSymmetric=isSymmetric
        self.innerBounds = Polygon([(innerBoundsR,innerBoundsR),
            (innerBoundsR,-innerBoundsR),
            (-innerBoundsR,-innerBoundsR),
            (-innerBoundsR,innerBoundsR)])
        self.outerBounds = Polygon([(outerBoundsR,outerBoundsR),
            (outerBoundsR,-outerBoundsR),
            (-outerBoundsR,-outerBoundsR),
            (-outerBoundsR,outerBoundsR)])

    def generate(self):
        pLast = self.zeroPoint
        pCurr = self.startingPoint
        self.wallPath.append(pCurr)
        wasCollision = False
        for num in range(7):
            distance = self.rollDistance()
            pNew = self.wallSection(pCurr,self.normal(pCurr,pLast),distance,wasCollision)
            wasCollision = False # reset to False for the next one.
            overShoot = 0
            #print("pcurr: {0}, pLast: {1}, pNew: {2} ".format(pCurr,pLast,pNew))
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