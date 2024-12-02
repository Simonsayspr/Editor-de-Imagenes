from filters.filter import Filter
from PIL import Image
class Highlight(Filter):
    def __init__(self,color)-> None:
        self.color = color
    def apply(self, im):
        self.im = im
        pxs=self.im.load()
        width, height = self.im.size
        if self.color == "red":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 >= 70 and p2<=60 and p3<=60:
                        pass
                    else:
                        pxs[i,j] = ((p1+p2+p3)//3, (p1+p2+p3)//3, (p1+p2+p3)//3)
        elif self.color == "blue":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 <= 150 and p2 <=150 and p3>=50:
                        pass
                    else:
                        pxs[i,j] = ((p1+p2+p3)//3, (p1+p2+p3)//3, (p1+p2+p3)//3)
        elif self.color == "green":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 <= 150 and p2>=60 and p3<=150:
                        pass
                    else:
                        pxs[i,j] = ((p1+p2+p3)//3, (p1+p2+p3)//3, (p1+p2+p3)//3)
        elif self.color == "yellow":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1>=160 and p1+35>=p2>=p1-35 and p3<=110:
                        pass
                    else:
                        pxs[i,j] = ((p1+p2+p3)//3, (p1+p2+p3)//3, (p1+p2+p3)//3)
        elif self.color == "purple":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if 128>= p3-p1 >=50 and p2<=60 and p3>=150:
                        pass
                    else:
                        pxs[i,j]= ((p1+p2+p3)//3, (p1+p2+p3)//3, (p1+p2+p3)//3)
        elif self.color == "orange":
            for i in range(0,width):
                for j in range(0,height):
                    data = pxs[i,j]
                    p1 = data[0]
                    p2 = data[1]
                    p3 = data[2]
                    if p1 >= 180 and 170>=p1-p2>=90 and p3<=90:
                        pass
                    else:
                        pxs[i,j] = ((p1+p2+p3)//3, (p1+p2+p3)//3, (p1+p2+p3)//3)
        return self.im