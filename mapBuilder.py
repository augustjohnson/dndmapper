from PIL import Image
from PIL import ImageDraw
from shapely.geometry import *
from shapely.ops import transform

class mapBuilder(object):
    def __init__(self,multiplier,canvasSize):
        self.back = Image.new('RGBA', (canvasSize,canvasSize), (255,0,0,0))
        self.grid = ImageDraw.Draw(self.back)
        self.multiplier = multiplier
        self.canvasSize = canvasSize
        self.drawGrid()
        self.layers = []

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

    def resizeAndCenter(self,x,y,z=None):
        return tuple(filter(None, [x * self.multiplier + self.canvasSize/2, y* self.multiplier + self.canvasSize/2, z]))

    def drawPolygon(self,poly):
        newLayerPoly = Image.new('RGBA', (self.canvasSize,self.canvasSize))
        newLayerDraw = ImageDraw.Draw(newLayerPoly)
        poly_t = transform(self.resizeAndCenter,poly)
        #print(poly_t.exterior.coords[:])
        newLayerDraw.polygon(poly_t.exterior.coords[:],fill=(255,255,255,127),outline=(255,255,255,255))
        self.back.paste(newLayerPoly,mask=newLayerPoly)

    def drawLine(self,line):
        newLayerLine = Image.new('RGBA', (self.canvasSize,self.canvasSize))
        newLayerDraw = ImageDraw.Draw(newLayerLine)
        line_t = transform(self.resizeAndCenter,line)
        #print(line_t.coords[:])
        newLayerDraw.line(line_t.coords[:],fill=(0,0,255,127),width=3)
        self.back.paste(newLayerLine,mask=newLayerLine)
    
    def showMap(self):
        self.back.show()
