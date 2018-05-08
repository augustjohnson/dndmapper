import mapBuilder
import structureBuilder

#HOUSE SETUP
SEED = 1
SYMMETRIC = True
TURN_ODDS = 0.9

#MAP OUTPUT SETUP
CANVAS_SIZE = 512 #512 by 512px
MULTIPLIER = 10 #10x magnification of points.


#building the house.
house = structureBuilder.structureBuilder(SEED,SYMMETRIC,TURN_ODDS)
house.generate() #generating the path of the wall.
coordinates = house.wallPolygonCoordinates
coordinates+=house.reflect() #adding the reflected image of the points onto the wall.


map = mapBuilder.mapBuilder(MULTIPLIER,CANVAS_SIZE)
map.drawPolygon(coordinates)
map.showMap()