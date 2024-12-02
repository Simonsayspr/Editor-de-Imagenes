from filters.filter import Filter
from PIL import Image

class CutRightLeft(Filter):
    def __init__(self, filename2):
        self.filename2 = filename2
        with Image.open(self.filename2).convert('RGB') as im2:
            self.im2 = im2
    def apply(self,im):
        self.im = im

        width1, height1 = self.im.size
        width2, height2 = self.im2.size

        right_cut = self.im.crop((0, 0, width1//2, height1))
        left_cut = self.im2.crop((0, 0, width2, height2))

        new_width = width1//2 + width2//2
        new_height = max(height1, height2)
        new_im = Image.new("RGB", (new_width, new_height))

        new_im.paste(right_cut, (0, 0))
        new_im.paste(left_cut, (width1//2, 0))
        self.im = new_im
        return self.im