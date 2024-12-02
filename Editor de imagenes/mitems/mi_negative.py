from filters import Negative, Filter
from mitems.menu_item import MenuItem

class MINegative(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Negative filter"
    @classmethod
    def ask_params(cls, im) -> str:
        return {'__type__': "Negative"}
    @classmethod
    def create_action(cls) -> Filter:
        return Negative()