import mapBuilder
import structureBuilder

#HOUSE SETUP
SEED = 3
SYMMETRIC = True
INNER_SQUARE = 4
OUTER_SQUARE = 8
TURN_ODDS = 0.5

#MAP OUTPUT SETUP
CANVAS_SIZE = 512 #512 by 512px
MULTIPLIER = 16 #10x magnification of points.


#building the house.
house = structureBuilder.structureBuilder(SEED,SYMMETRIC,TURN_ODDS,INNER_SQUARE,OUTER_SQUARE)
house.generate() #generating the path of the wall.
coordinates = house.wallPath
coordinates+=house.reflect() #adding the reflected image of the points onto the wall.

#   print(house.wallPath)

map = mapBuilder.mapBuilder(MULTIPLIER,CANVAS_SIZE)
map.drawGrid()
map.drawPolygon(coordinates)
map.showMap()