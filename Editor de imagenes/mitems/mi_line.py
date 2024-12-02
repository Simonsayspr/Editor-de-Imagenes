from filters import Line, Filter
from mitems.menu_item import MenuItem

class MILine(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Add line"
    @classmethod
    def ask_params(cls, im) -> str:
        cls.im = im
        width, height = cls.im.size
        print(f"width: {width-1} height: {height-1}")
        while True:
            cls.x = int(input("Select starting coordenate x "))
            cls.y = int(input("Select starting coordenate y "))
            cls.x2 = int(input("Select end coordenate x "))
            cls.y2 = int(input("Select end coordenate y "))
            if 0<=cls.x<=width and 0<=cls.y<=height and 0<=cls.x2<=width and 0<=cls.y2<=height:
                cls.color = input("Choose a color ")
                cls.wdh = int(input("Set line width "))
                return {'__type__': 'Line', 'x': cls.x, 'y': cls.y, 'x2': cls.x2, 'y2': cls.y2, 'color': cls.color, 'wdh': cls.wdh}
            else:
                print("One of your coordinates exceeds the limit, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Line(cls.x,cls.y,cls.x2,cls.y2,cls.color,cls.wdh)