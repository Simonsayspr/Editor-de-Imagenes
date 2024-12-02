from filters import Highlight, Filter
from mitems.menu_item import MenuItem

class MIHighlight(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Highlight color"
    @classmethod
    def ask_params(cls, im) -> str:
        cls.color = input("Select color to highlight (red, blue, green, yellow, orange or purple) ")
        return {'__type__': 'Highlight', 'color': cls.color}
    @classmethod
    def create_action(cls) -> Filter:
        return Highlight(cls.color)