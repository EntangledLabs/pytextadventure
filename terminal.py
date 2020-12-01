import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

'''
class StartScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class TerminalScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class ChoiceScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class RollCreditsScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
'''

class GameApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    GameApp().run()