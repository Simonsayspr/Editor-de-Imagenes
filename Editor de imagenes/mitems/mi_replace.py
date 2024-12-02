from filters import Replace, Filter
from mitems.menu_item import MenuItem

class MIReplace(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Replace color"
    @classmethod
    def ask_params(cls, im) -> str:  
        cls._color = input("select color to replace (red, green, blue, yellow, orange or purple) ")
        cls._color2 = input("select which color to replace with (red, green, blue, yellow, orange or purple) ")
        return {'__type__': 'Replace', 'color': cls._color, 'color2': cls._color2}
    @classmethod
    def create_action(cls) -> Filter:
        return Replace(cls._color,cls._color2)