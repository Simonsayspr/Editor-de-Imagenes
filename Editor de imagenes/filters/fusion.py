from filters.filter import Filter
from PIL import Image
class Fusion(Filter):
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
        fusion_image = Image.new('RGB', (max(width1,width2),max(height1,height2)))
        pixs_fusion = fusion_image.load()
        for x in range(width):
            for y in range(height):
                r1, g1, b1 = pixs1[x, y]
                r2, g2, b2 = pixs2[x, y]
                r_avg = (r1 + r2) // 2
                g_avg = (g1 + g2) // 2
                b_avg = (b1 + b2) // 2
                pixs_fusion[x, y] = (r_avg, g_avg, b_avg)
        self.im = fusion_image
        return self.im
