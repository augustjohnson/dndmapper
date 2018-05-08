import random

class structureBuilder(object):
    wallPath=[]
    wallPolygonCoordinates=[]

    def __init__(self,seed,isSymmetric,turnOdds):
        self.turnOdds= 0.9 #Range from 0 to 1 affecting how often the algorithm will generate right turns.  Maybe change to range of -1 to 1 range?
        random.seed(seed)
        self.isSymmetric=isSymmetric
        initialDirection = {'axis':'x','sign':False}
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

    def generate(self):
        vector = self.vector
        for num in range(4):
            self.wallPath.append(vector)
            self.wallPolygonCoordinates.append((vector['p']['x'],vector['p']['y']))
            vector = self.getNextVector(vector)

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