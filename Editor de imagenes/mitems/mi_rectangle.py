from filters import Rectangle, Filter
from mitems.menu_item import MenuItem

class MIRectangle(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Add rectangle"
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
                return {'__type__': 'Rectangle', 'x': cls.x, 'y': cls.y, 'x2': cls.x2, 'y2': cls.y2, 'color': cls.color}
            else:
                print("One of your coordinates exceeds the limit, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Rectangle(cls.x,cls.y,cls.x2,cls.y2,cls.color)