from filters.filter import Filter
from PIL import Image
class Negative(Filter):
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
                pxs[i,j] = (255-p1, 255-p2, 255-p3)
        return self.im
