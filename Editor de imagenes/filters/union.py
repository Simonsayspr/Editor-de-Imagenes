from filters.filter import Filter
from PIL import Image
class Union(Filter):
    def __init__(self,filename2,form)-> None:
        self.filename2 = filename2
        with Image.open(self.filename2).convert('RGB') as im2:
            self.im2 = im2
        self.form = form
    def apply(self, im):
        self.im = im
        width1, height1 = self.im.size
        width2, height2 = self.im2.size
        if self.form == 'right':
            img = Image.new("RGB", (width1+width2,max(height1,height2)), "white")
            img.paste(self.im,(0,0))
            img.paste(self.im2,(width1,0))
            self.im = img
            return self.im
        elif self.form == 'bottom':
            img = Image.new("RGB", (max(width1,width2),height1+height2), "white")
            img.paste(self.im,(0,0))
            img.paste(self.im2,(0,height2))
            self.im = img
            return self.im