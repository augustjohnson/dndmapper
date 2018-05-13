import mapBuilder
import structureBuilder

#HOUSE SETUP
SEED = 4
SYMMETRIC = True
INNER_SQUARE = 5
OUTER_SQUARE = 9
TURN_ODDS = 0.8

#MAP OUTPUT SETUP
CANVAS_SIZE = 512 #512 by 512px
MULTIPLIER = 16 #16x magnification of points.


#building the house.
house = structureBuilder.structureBuilder(SEED,SYMMETRIC,TURN_ODDS,INNER_SQUARE,OUTER_SQUARE)
 #adding the reflected image of the points onto the wall.
i = 0
while (house.largerThanMin()==False):
    house.generate() #generating the path of the wall.
    coordinates = house.wallPath
    coordinates+=house.reflect()
    i+=1

print("Iterations: {0}".format(i))

map = mapBuilder.mapBuilder(MULTIPLIER,CANVAS_SIZE)
map.drawGrid()
map.drawPolygon(coordinates)
map.showMap()