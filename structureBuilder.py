import random
import turtle
from shapely.geometry import Polygon, Point, LineString


class structureBuilder(object):

    def __init__(self,seed,innerBounds,outerBounds):
        random.seed(seed)
        self.startingPoint=(6.0,0.0)
        self.I = innerBounds
        self.O = outerBounds

    def generateRandomWalk(self,steps):
        wallCorners = []
        def randomWalkb(length):
            x,y = self.startingPoint[0],self.startingPoint[1]
            walkx,walky = [x],[y]
            for i in range(length):
                new = random.randint(1,4)
                if new == 1:
                    x += 1
                elif new == 2:
                    y += 1
                elif new ==3 :
                    x += -1
                else :
                    y += -1
                walkx.append(x)
                walky.append(y)
            return [walkx,walky]

        rw = randomWalkb(steps)
        #print(rw)
        for i in range(steps):
            wallCorners.append((rw[0][i],rw[1][i]))
        return(LineString(wallCorners))
