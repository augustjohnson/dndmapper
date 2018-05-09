import random
from shapely.geometry import *

class structureBuilder(object):
    wallPath=[]
    wallPolygonCoordinates=[]

    innerBounds = Polygon([(3,3),(3,-3),(-3,-3),(-3,3)])
    outerBounds = Polygon([(13,13),(13,-13),(-13,-13),(-13,13)])

    zeroPoint = (0,6)
    startingPoint = (0,4)

    def normal(self,p1,p2):
        a=p1[0]-p2[0]
        b=p1[1]-p2[1]
        return (-b,a)

    def getNextPoint(self,p,normal,wasCollision):
        distance=random.randint(1,6)
        if wasCollision or random.random()<self.turnOdds:
            #follow the normal vector.
            x=distance*abs(normal[0])/normal[0]
            y=distance*abs(normal[1])/normal[1]
        else:
            #invert the normal vector.
            x=-distance*abs(normal[0])/normal[0]
            y=-distance*abs(normal[1])/normal[1]
        return (x,y)

    def isInBounds(self,p):
        point = Point(p)
        return point.within(self.outerBounds) and not point.within(self.innerBounds)

    def shortenByOne(self,p1,p2):
        #return p1 adjusted one unit towards p2

    def __init__(self,seed,isSymmetric,turnOdds):
        self.turnOdds= 0.9 #Range from 0 to 1 affecting how often the algorithm will generate right turns.  Maybe change to range of -1 to 1 range?
        random.seed(seed)
        self.isSymmetric=isSymmetric
        initialDirection = {'axis':'x','sign':True}
        initialPosition = {'x':0,'y':0}
        self.vector = {'d':initialDirection,'p':initialPosition}

    def whichWay(self, previousDirection):
        if previousDirection['axis']=='x':
            sign = (random.random()<self.turnOdds) ^ previousDirection['sign']
            return {'axis':'y','sign':sign}
        if previousDirection['axis']=='y':
            sign = not ((random.random()<self.turnOdds) ^ previousDirection['sign'])
            return {'axis':'x','sign':sign}
        else: print("OH SHIT")

    def howFar(self, position):
        rangeMax = 15 - max(abs(position['x']),abs(position['y']),5)
        #return random.randint(3,max(rangeMax,4))
        return 5

    def getNextVector(self, previousVector):
        newVector = previousVector
        newVector['d']=self.whichWay(previousVector['d'])
        distance = self.howFar(previousVector['p'])
        #add a line about innersanctum
        #You must pass in chance = 1 in that case.

        if (newVector['d']['sign']==True):
            newVector['p'][newVector['d']['axis']] += distance
        else:
            newVector['p'][newVector['d']['axis']] -= distance
        return newVector

    #def buildWallSection(self, startPoint, direction):
        #given the start point and direction
        #add a random integer
        #check to see if that integer collides
        #if it collides, use the collision to determine the next start point and direction
        #save the vector
        #if it doesn't collide, randomly determine the next start point and direction
        #save the vector
        

    def generate(self):
        p1=self.startingPoint
        self.wallPolygonCoordinates.append(p1)
        p = self.getNextPoint(self.zeroPoint,p1,False)
        collision=False
        while not p.isInBounds:
            collision=True
            p=p.shortenByOne()
        
        self.wallPolygonCoordinates.append(p2)


    def setInnerBounds(self):
        print("Setting inner bounds.")

    def setOuterBounds(self):
        print("Setting outer bounds.")

    def reflect(self):
        #only mirrors the x point right now.
        reversedPath = self.wallPolygonCoordinates[::-1]
        invertedPath = []
        for point in reversedPath:
            invertedPath.append((-point[0],point[1]))
        return invertedPath