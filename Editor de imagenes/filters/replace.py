from filters.filter import Filter
from PIL import Image, ImageDraw, ImageFont
class Replace(Filter):
    
    def __init__(self, color, color2):
        self.color = color
        self.color2 = color2
    def apply(self,im):
        self.im = im
        pxs = self.im.load()
        width, height = self.im.size
        
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0,0,255)
        yellow = (255,255,0)
        orange = (255, 128, 0)
        purple = (153,0,153)
        if self.color2 == "red":
            self.color2 = red
        elif self.color2 == "green":
            self.color2 = green
        elif self.color2 == "blue":
            self.color2 = blue
        elif self.color2 == "yellow":
            self.color2 = yellow
        elif self.color2 == "orange":
            self.color2 = orange
        elif self.color2 == "purple":
            self.color2 = purple
        if self.color == "red":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 >= 70 and p2<=60 and p3<=60:
                        pxs[i,j] = self.color2
                    else:
                        pass
        elif self.color == "blue":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 <= 150 and p2 <=150 and p3>=50:
                        pxs[i,j] = self.color2
                    else:
                        pass
        elif self.color == "green":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 <= 150 and p2>=60 and p3<=150:
                        pxs[i,j] = self.color2
                    else:
                        pass
        elif self.color == "yellow":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1>=160 and p1+35>=p2>=p1-35 and p3<=110:
                        pxs[i,j] = self.color2
                    else:
                        pass
        elif self.color == "purple":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if 128>= p3-p1 >=50 and p2<=60 and p3>=150:
                        pxs[i,j] = self.color2
                    else:
                        pass
        elif self.color == "orange":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 >= 180 and 170>=p1-p2>=90 and p3<=90:
                        pxs[i,j] = self.color2
                    else:
                        pass
        return self.im