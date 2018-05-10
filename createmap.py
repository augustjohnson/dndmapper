import mapBuilder
import structureBuilder

#HOUSE SETUP
SEED = 25
SYMMETRIC = True
TURN_ODDS = 0.7

#MAP OUTPUT SETUP
CANVAS_SIZE = 512 #512 by 512px
MULTIPLIER = 10 #10x magnification of points.


#building the house.
house = structureBuilder.structureBuilder(SEED,SYMMETRIC,TURN_ODDS)
house.generate() #generating the path of the wall.
coordinates = house.wallPath
coordinates+=house.reflect() #adding the reflected image of the points onto the wall.

print(house.wallPath)

map = mapBuilder.mapBuilder(MULTIPLIER,CANVAS_SIZE)
map.drawPolygon(coordinates)
map.showMap()