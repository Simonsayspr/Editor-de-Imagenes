from filters import Grey, Filter
from mitems.menu_item import MenuItem

class MIGrey(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Turn colors to grey"
    @classmethod
    def ask_params(cls, im) -> str:
        return {'__type__' :'Grey'}
    @classmethod
    def create_action(cls) -> Filter:
        return Grey()