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
            wallCorners.append((x,y))
            for i in range(length):
                new = random.randint(1,4)
                dis = random.randint(2,6)
                if new == 1:
                    x += dis
                elif new == 2:
                    y += dis
                elif new ==3 :
                    x += -dis
                else :
                    y += -dis

                wallCorners.append((x,y))
                #Bounds check, inner and outer.
                if not self.O.contains(Point(x,y)) or self.I.contains(Point(x,y)):
                    #print("removing corner {0},{1} because it was out of bounds.".format(x,y))
                    wallCorners.pop()
                    x=wallCorners[-1][0]
                    y=wallCorners[-1][1]
                    
                #Check if the wall overlaps itself.
                if not LineString(wallCorners).is_simple:
                    #print("removing corner {0},{1} because it made the string not simple.".format(x,y))
                    wallCorners.pop()
                    x=wallCorners[-1][0]
                    y=wallCorners[-1][1]

            return wallCorners
        
        rw = randomWalkb(steps)

        return(LineString(wallCorners))
