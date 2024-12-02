from filters.filter import Filter
from PIL import Image, ImageDraw
class Line(Filter):
    def __init__(self,x,y,x2,y2,color,wdh)-> None:
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.wdh = wdh
    def apply(self, im):
        self.im = im
        draw = ImageDraw.Draw(self.im)
        draw.line([(self.x,self.y),(self.x2,self.y2)],fill=self.color,width=self.wdh)
        return self.im