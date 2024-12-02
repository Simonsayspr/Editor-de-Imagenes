from filters.filter import Filter
from PIL import Image
class Pixel(Filter):
    def __init__(self,num)-> None:
        self.num = num
    def apply(self, im):
        self.im = im
        pxs=self.im.load()
        height, width = self.im.size
        w = width
        h = height
        print(height, width)
        a = h//self.num
        c = w//self.num
        r1 = h%self.num
        r2 = w%self.num
        if self.num>=2 and self.num<=50:
            while w>=self.num and h>=self.num:
                for d in range(0,c):
                    for b in range(0,a):
                        p1 = 0
                        p2 = 0
                        p3 = 0
                        for i in range(0,self.num):
                            for j in range(0,self.num):
                                data=pxs[i+b*self.num,j+d*self.num]
                                p1 += data[0]
                                p2 += data[1]
                                p3 += data[2]
                        for i in range(0,self.num):
                            for j in range(0,self.num):
                                pxs[i+b*self.num,j+d*self.num] = (p1//(self.num**2),p2//(self.num**2), p3//(self.num**2))
                h -= self.num
                if h<self.num:
                    h = height
                    w-=self.num
            for d in range(0,c):
                for i in range(1,r1):
                    for j in range(0,self.num):
                        data=pxs[height-i,j+d*self.num]
                        p1 += data[0]
                        p2 += data[1]
                        p3 += data[2]
                for i in range(1,r1):
                    for j in range(0,self.num):
                        pxs[height-i,j+d*self.num] = (p1//(r1*self.num),p2//(r1*self.num), p3//(r1*self.num))
            for b in range(0,a):
                for i in range(0,self.num):
                    for j in range(1,r2):
                        data=pxs[i+b*self.num,width-j]
                        p1 += data[0]
                        p2 += data[1]
                        p3 += data[2]
                for i in range(0,self.num):
                    for j in range(1,r2):
                        pxs[i+b*self.num,width-j] = (p1//(r2*self.num),p2//(r2*self.num), p3//(r2*self.num))
        return self.im