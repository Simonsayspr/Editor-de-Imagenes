from filters import Text, Filter
from mitems.menu_item import MenuItem

class MIText(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Add Text"
    @classmethod
    def ask_params(cls, im) -> str:
        cls.im = im
        width, height = cls.im.size
        print(f"width: {width-1} height: {height-1}")
        while True:
            cls.x = int(input("Select coordenate x "))
            cls.y = int(input("Select coordenate y "))
            if 0<=cls.x<=width and 0<=cls.y<=height:
                cls.s = int(input("Select text size with a number "))
                cls.color = input("Select a color ")
                cls.st = input("Write text ")
                return {'__type__': 'Text', 'x': cls.x, 'y': cls.y, 's': cls.s, 'color': cls.color, 'st': cls.st}
            else:
                print("One of your coordinates exceeds the limit or isn't a number, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Text(cls.x,cls.y,cls.s,cls.color,cls.st)