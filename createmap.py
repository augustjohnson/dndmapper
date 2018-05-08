import random
from PIL import Image
from PIL import ImageDraw

random.seed(1)

chanceOfTurningRight = 0.9

initialDirection = {'axis':'x','sign':False}
initialPosition = {'x':0,'y':0}
vector = {'d':initialDirection,'p':initialPosition}

def whichWay(previousDirection, chance):
	if previousDirection['axis']=='x':
		sign = (random.random()<chanceOfTurningRight) ^ previousDirection['sign']
		return {'axis':'y','sign':sign}
	if previousDirection['axis']=='y':
		sign = not ((random.random()<chanceOfTurningRight) ^ previousDirection['sign'])
		return {'axis':'x','sign':sign}
	else: print("OH SHIT")

def howFar(position):
	rangeMax = 15 - max(abs(position['x']),abs(position['y']),5)
	#return random.randint(3,max(rangeMax,4))
	return 5

def getNextVector(previousVector):
	newVector = previousVector
	newVector['d']=whichWay(previousVector['d'])
	distance = howFar(previousVector['p'])
	#add a line about innersanctum
	#You must pass in chance = 1 in that case.

	if (newVector['d']['sign']==True):
		newVector['p'][newVector['d']['axis']] += distance
	else:
		newVector['p'][newVector['d']['axis']] -= distance
	return newVector

polygonCoordinates=[]
count=0

#hard limit the vectors  While loop because this can be converted to using recursion easier
while count<6:
	polygonCoordinates.append((vector['p']['x'],vector['p']['y']))
	vector = getNextVector(vector)
	count=count+1
	print(vector)

#create set of mirrored coords
mirroredPolygonCoordinates = polygonCoordinates[::-1]
reflectedPolygonCoordinates = []
for point in mirroredPolygonCoordinates:
	reflectedPolygonCoordinates.append((-point[0],point[1]))	

#append mirrored coords	
coordinates = polygonCoordinates #+ reflectedPolygonCoordinates


draw = []
for point in coordinates:
	multiplier = 10
	shift = 256
	draw.append(((point[0]*multiplier + shift),(point[1]*multiplier + shift)))


back = Image.new('RGBA', (512,512), (255,0,0,0))
poly = Image.new('RGBA', (512,512))
pdraw = ImageDraw.Draw(poly)
#pdraw.polygon([(128,128),(384,384),(128,384),(384,128)],
pdraw.polygon(draw,
              fill=(255,255,255,127),outline=(255,255,255,255))
back.paste(poly,mask=poly)
back.show()