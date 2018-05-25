import random
import turtle
from shapely.geometry import Polygon, Point, LineString


class structureBuilder(object):

    def __init__(self,seed,innerBounds,outerBounds):
        random.seed(seed)
        self.icorner = innerBounds.exterior.coords[0][0]
        self.ocorner = outerBounds.exterior.coords[0][0]
        x = (self.icorner+self.ocorner)//2 #Find an int between the two boxes.
        self.startingPoint=(x,0.0)
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
    #reflect should take an input of walls, and return a list which includes a reflection.
    def reflect(self,walls):
        def getReflectionIndex(ls):
            print( list(ls.coords))
            for p in list(ls.coords):
                #check the last point to see if it's both less than the inner box min and greater than y=0
                if p[0] < -self.icorner and p[1] <= 0:
                    return list(ls.coords).index(p)

        
        def reflectAcrossX(coordlist):
            reflectedCoordlist = []
            for c in coordlist[::-1]:
                #Reflecting the Y coords across X=0.
                reflectedCoordlist.append((c[0],c[1]*-1))
            return reflectedCoordlist

        rindex = getReflectionIndex(walls)
        clist = list(walls.coords)[0:rindex]
        rlist = reflectAcrossX(clist)
        return LineString(clist + rlist)
        
        
