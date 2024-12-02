from filters.filter import Filter
from PIL import Image, ImageDraw
class Rectangle(Filter):
    def __init__(self,x,y,x2,y2,color)-> None:
        self.x=x
        self.y=y
        self.x2=x2
        self.y2=y2
        self.color=color
    def apply(self, im):
        self.im = im
        draw = ImageDraw.Draw(self.im)
        draw.rectangle([(self.x,self.y),(self.x2,self.y2)],outline=self.color)
        return self.im