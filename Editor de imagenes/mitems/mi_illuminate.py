from filters import Illuminate, Filter
from mitems.menu_item import MenuItem

class MIIlluminate(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Brighten Image"
    @classmethod
    def ask_params(cls, im) -> str:
        return {'__type__':'Illuminate'}
    @classmethod
    def create_action(cls) -> Filter:
        return Illuminate()