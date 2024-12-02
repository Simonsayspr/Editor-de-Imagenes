from filters import Union, Filter
from mitems.menu_item import MenuItem
import os.path
class MIUnion(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Join images"
    @classmethod
    def ask_params(cls, im) -> str:
        while True:    
            cls.filename2 = input("Insert route of image to fuse with ")
            if os.path.isfile(cls.filename2):
                cls.form = input("Choose bottom or right ")
                return {'__type__':'Union', 'filename2': cls.filename2, 'form': cls.form}
            else:
                print("File does not exist, try again ")
    @classmethod
    def create_action(cls) -> Filter:
        return Union(cls.filename2,cls.form)