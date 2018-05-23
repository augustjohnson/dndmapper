import mapBuilder
import structureBuilder
from shapely.geometry import *

#HOUSE SETUP
SEED = 4
SYMMETRIC = True
INNER_SQUARE = 5
OUTER_SQUARE = 9
TURN_ODDS = 0.8
OUTER_BOUNDS = box(-OUTER_SQUARE,-OUTER_SQUARE,OUTER_SQUARE,OUTER_SQUARE)
INNER_BOUNDS = box(-INNER_SQUARE,-INNER_SQUARE,INNER_SQUARE,INNER_SQUARE)

#MAP OUTPUT SETUP
CANVAS_SIZE = 512 #512 by 512px
MULTIPLIER = 16 #16x magnification of points.


#building the house.

house = structureBuilder.structureBuilder(SEED,INNER_BOUNDS,OUTER_BOUNDS)
walls = house.generateRandomWalk(25)


map = mapBuilder.mapBuilder(MULTIPLIER,CANVAS_SIZE)
map.drawPolygon(OUTER_BOUNDS)
map.drawPolygon(INNER_BOUNDS)
map.drawLine(walls)
map.showMap()