from filters import Watermark, Filter
from mitems.menu_item import MenuItem
import os.path

class MIWatermark(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Watermark with another image"
    @classmethod
    def ask_params(cls, im) -> str:
        while True:
            cls.filename2 = input("Insert route of image to watermark with ")
            if os.path.isfile(cls.filename2):
                return {'__type__': 'Watermark', 'filename2': cls.filename2}
            else:
                print("File does not exist, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Watermark(cls.filename2)