from filters import Darken, Filter
from mitems.menu_item import MenuItem

class MIDarken(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Darken Image"
    @classmethod
    def ask_params(cls, im) -> str:
        return {'__type__': 'Darken'}
    @classmethod
    def create_action(cls) -> Filter:
        return Darken()