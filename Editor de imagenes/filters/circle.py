from filters.filter import Filter
from PIL import Image, ImageDraw, ImageFont
class Circle(Filter):
    def __init__(self,x,y,r,color)-> None:
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def apply(self, im):
        self.im = im
        draw = ImageDraw.Draw(self.im)
        draw.ellipse([(self.x-self.r,self.y-self.r),(self.x+self.r,self.y+self.r)], outline = self.color)
        return self.im