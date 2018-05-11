from PIL import Image
from PIL import ImageDraw

class mapBuilder(object):
    def __init__(self,multiplier,canvasSize):
        self.back = Image.new('RGBA', (canvasSize,canvasSize), (255,0,0,0))
        self.poly = Image.new('RGBA', (canvasSize,canvasSize))
        self.grid = ImageDraw.Draw(self.back)
        self.pdraw = ImageDraw.Draw(self.poly)
        self.multiplier = multiplier
        self.canvasSize = canvasSize

    def drawGrid(self):
        for l in range(self.canvasSize//self.multiplier):
            multiplier = self.multiplier
            shift = self.canvasSize/2
            offset = shift%multiplier
            x = l * multiplier + offset
            y = l * multiplier + offset
            self.grid.line((x,0, x,self.canvasSize),
                fill=(255,255,255,127), width=1)
            self.grid.line((0,y, self.canvasSize,y ),
                fill=(255,255,255,127), width=1)


    def drawPolygon(self,coordinates):
        draw = []
        for point in coordinates:
            multiplier = self.multiplier
            shift = self.canvasSize/2
            #take the small points and shift them to a more visible size.
            x = point[0] * multiplier + shift
            y = point[1] * multiplier + shift
            draw.append((x,y))
            #draw the actual points onto a polygon.
        
        self.pdraw.polygon(draw,fill=(255,255,255,127),outline=(255,255,255,255))
        self.back.paste(self.poly,mask=self.poly)



    def showMap(self):
        self.back.show()
