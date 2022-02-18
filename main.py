#import package
from kivy.app import App
from kivy.uix.screenmanager import Screen

#load main.kv file
from kivy.lang import Builder
import os

from pandas import set_option
folder = os.path.dirname(__file__)
file = os.path.join(folder, 'main.kv')
Builder.load_file(file)

#set window size
from kivy.core.window import Window
Window.size = (450, 540)

class window(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class app(App):
    def build(self):
        self.title = "Simple Calculator"
        self.icon = os.path.join(folder, 'icon.jpg')
        return window()

if __name__=="__main__":
    app().run()