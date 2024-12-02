from filters import Star, Filter
from mitems.menu_item import MenuItem

class MIStar(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Draw star"
    @classmethod
    def ask_params(cls, im) -> str:
        cls.im = im
        width, height = cls.im.size
        print(f"width: {width-1} height: {height-1}")
        while True:
            cls.x = int(input("Select coordenate x "))
            cls.y = int(input("Select coordenate y "))
            if 0<=cls.x<=width and 0<=cls.y<=height:    
                cls.size = int(input("Select size "))
                cls.color = input("Choose a color ")
                return {'__type__':'Star', 'x': cls.x, 'y':cls.y, 'size': cls.size, 'color':cls.color}
            else:
                print("One of your coordinates exceeds the limit, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Star(cls.x,cls.y,cls.size,cls.color)