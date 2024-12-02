from filters.filter import Filter
from PIL import Image, ImageDraw, ImageFont
class Text(Filter):
    def __init__(self,x,y,s,color,st)-> None:
        self.x=x
        self.y=y
        self.s=s
        self.color=color
        self.st=st
    def apply(self, im):
        self.im = im
        draw = ImageDraw.Draw(self.im)
        font = ImageFont.truetype("arial.ttf",self.s)
        draw.text((self.x,self.y),self.st,font=font,fill=self.color)
        return self.im
