import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'resizable', True) 
Config.set('graphics', 'width', '325')
Config.set('graphics', 'height', '475')
Config.write()

kivy.require('1.11.1')

class CalculatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorWindow, self).__init__(**kwargs)


class CalculatorApp(App):
    def build(self):
        return CalculatorWindow()
    
if __name__ == "__main__":
    CalculatorApp().run()