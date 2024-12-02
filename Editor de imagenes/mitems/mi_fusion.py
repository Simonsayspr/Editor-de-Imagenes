from filters import Fusion, Filter
from mitems.menu_item import MenuItem
import os.path
class MIFusion(MenuItem):
    @classmethod
    def get_description(cls) -> str:
        return "Fuse with another image"
    
    @classmethod
    def ask_params(cls, im) -> str:
        while True:
            cls.filename2 = input("Insert route of image to fuse with ")
            if os.path.isfile(cls.filename2): 
                return {'__type___': 'Fusion', 'filename2': cls.filename2}
            else:
                print("File does not exist, try again")
    @classmethod
    def create_action(cls) -> Filter:
        return Fusion(cls.filename2)