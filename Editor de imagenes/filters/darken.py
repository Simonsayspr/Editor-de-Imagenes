from filters.filter import Filter
from PIL import Image
class Darken(Filter):
    def __init__(self)-> None:
        ...
    def apply(self, im):
        self.im = im
        pxs = self.im.load()
        width, height = self.im.size
        for i in range(0,width):
            for j in range(0,height):
                data = pxs[i,j]
                p1 = data[0]
                p2 = data[1]
                p3 = data[2]
                if p1 >= 180 and p2 >= 180 and p3 >= 180:
                    pxs[i,j] = (p1-100,p2-100,p3-100)
                else:
                    pass
        return self.im