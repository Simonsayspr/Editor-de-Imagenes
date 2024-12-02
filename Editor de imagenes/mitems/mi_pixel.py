from filters import Pixel, Filter
from mitems.menu_item import MenuItem

class MIPixel(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Pixelated filter"
    @classmethod
    def ask_params(cls, im) -> str:
        while True:
            cls.num = int(input("Select a number between 2 and 50 "))
            if 2<=cls.num<=50:
              return {'__type__':'Pixel', 'num': cls.num}
            else:
               print("You're exceeding the limit, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Pixel(cls.num)