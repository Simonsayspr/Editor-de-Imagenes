from filters.filter import Filter
from PIL import Image
class Watermark(Filter):
    def __init__(self,filename2)-> None:
        self.filename2 = filename2
        with Image.open(self.filename2).convert('RGB') as im2:
            self.im2 = im2
    def apply(self, im):
        self.im = im
        pixs1 = self.im.load()
        pixs2 = self.im2.load()
        width1, height1 = self.im.size
        width2, height2 = self.im2.size
        width = min(width1, width2)
        height = min(height1, height2)
        water_image = Image.new('RGB', (max(width1,width2),max(height1,height2)))
        pixs_water = water_image.load()
        for x in range(width):
            for y in range(height):
                r1, g1, b1 = pixs1[x, y]
                r2, g2, b2 = pixs2[x, y]
                r_avg = int(0.7*r1 + 0.3*r2) 
                g_avg = int(0.7*g1 + 0.3*g2) 
                b_avg = int(0.7*b1 + 0.3*b2)  
                pixs_water[x, y] = (r_avg, g_avg, b_avg)
        self.im = water_image
        return self.im