import mitems
import os.path
from PIL import Image
import pickle
import json
from filters import *

class JSONSerializableDecoderR(json.JSONDecoder):
  def __init__(self, *args, **kwargs):
    super().__init__(object_hook=self.object_hook, *args, **kwargs)

  def object_hook(self, dct):
    if '__type__' in dct:
      obj_type = dct.pop('__type__')
      return globals()[obj_type](**dct)
    return dct
class Menu:
    def __init__(self):
        self._items = []
        self._name = ''
        self._projects = {}
        self._history = []
        self._actions = []
        self._im = None
    def load_items(self) -> None:
        self._items = [cls_obj for cls_name, cls_obj in vars(mitems).items() 
                      if isinstance(cls_obj, type) and issubclass(cls_obj, mitems.MenuItem) and cls_obj is not mitems.MenuItem]
    def start(self) -> None:
        working = True
        self.create_proj()
        while working:
            self._show()
            option = int(input())
            if option < len(self._items):
                self._execute(option)
            elif option == len(self._items):
                self.create_proj()
            elif option == len(self._items)+1:
                self._show_project()
            elif option == len(self._items)+2:
                self.save_image()
            elif option == len(self._items)+3:
                self.save_project()
            elif option == len(self._items)+4:
                self.open_project()
            elif option == len(self._items)+5:
                self.undo()
            elif option == len(self._items)+6:
                self.see_history()
            elif option == len(self._items)+7:
                self.switch_projects()
            elif option == len(self._items)+8:
                self.save_script()
            elif option == len(self._items)+9:
                _script_name = input("insert script name ")
                self.open_script(_script_name)
                self._history.append(_script_name)
            else:
                working = False

    def save_script(self):
        self._script_name = input("insert script name ")
        with open(f'{self._script_name}.json', 'w') as f:
            json.dump(self._history, f)
    
    def open_script(self,_script_name):
        if os.path.isfile(f'{_script_name}.json'):
            with open(f'{_script_name}.json', 'r') as rf:
                self._scripts = json.load(rf, cls=JSONSerializableDecoderR)
            self._actions.append(self._im.copy())
            for f in self._scripts:
                if isinstance(f,str):
                    self.open_script(f)
                else:     
                    self._im = f.apply(self._im)  
        else: print("File does not exist")    

    def _execute(self, option_idx: int) -> None:
        mi = self._items[option_idx]
        a = mi.ask_params(self._im)
        action = mi.create_action()
        self._actions.append(self._im.copy())
        self._im = action.apply(self._im)
        self._history.append(a)
    
    def undo(self):
        if len(self._actions) > 0:
            self._im = self._actions.pop()

    def see_history(self):
        print(self._history)

    def create_proj(self):
        self._name = input("Insert proyect name: ")
        while True:
            filename = input("Insert file route: ")
            if os.path.isfile(filename):
                with Image.open(filename).convert('RGB') as im: 
                    self._im = im
                break
            else:
                print("Route invalid, try again ")
        self._history = []
        self._actions = []
        self._projects[self._name] = [self._im,self._history, self._actions]
    
    def _show(self) -> None:
        print("Select which option to execute:")
        for idx, mi in enumerate(self._items):
            print(f'[{idx}] {mi.get_description()}')
        print(f'[{len(self._items)}] Create new project')
        print(f'[{len(self._items)+1}] Show current project')
        print(f'[{len(self._items)+2}] Save image')
        print(f'[{len(self._items)+3}] Save project')
        print(f'[{len(self._items)+4}] Open project')
        print(f'[{len(self._items)+5}] Undo filter ')
        print(f'[{len(self._items)+6}] See history ')
        print(f'[{len(self._items)+7}] Switch project')
        print(f'[{len(self._items)+8}] Save script')
        print(f'[{len(self._items)+9}] Open script')
        print(f'[{len(self._items)+10}] Quit')

    def _show_project(self) -> None:
        self._im.show()
    
    def save_project(self):
        self._projects[self._name] = [self._im,self._history, self._actions]
        with open(f'{self._name}.pickle', 'wb') as ff:
            pickle.dump(self._projects[self._name],ff)
    
    def save_image(self):
        filename2 = input("Insert saved image route: ")
        self._im.save(filename2)
    
    def open_project(self):
        self._name = input("Select proyect to open ")
        if os.path.isfile(f'{self._name}.pickle'):
            with open(f'{self._name}.pickle', 'rb') as rf:
                loaded = pickle.load(rf)
            self._projects[self._name] = loaded
            self._im = self._projects[self._name][0]
            self._history = self._projects[self._name][1] 
            self._actions = self._projects[self._name][2] 
            return self._im
        else:
            print("File does not exist, try again ")
    
    def switch_projects(self):
        for name, project in self._projects.items():
            print(f'[{name}] {project}')
        project_name = input("Select project ")
        if project_name in self._projects:
            self._name = project_name
            self._im=self._projects[project_name][0]
            self._history = self._projects[project_name][1]
            self._actions = self._projects[self._name][2]
            return self._im
        else:
            print("Project does not exist")