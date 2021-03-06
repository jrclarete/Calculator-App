import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'resizable', False) 
Config.set('graphics', 'width', '315')
Config.set('graphics', 'height', '365')
Config.write()

kivy.require('1.11.1')

class CalculatorWindow(BoxLayout):
    operator = ""
    calculation = ""
    
    def __init__(self, **kwargs):
        super(CalculatorWindow, self).__init__(**kwargs)
     
    def btnPressed(self, btn_num):
        self.operator += btn_num
        self.label = self.ids["textOperator"]
        self.label.text = self.operator
        
    def btnEquals(self):
        if(self.operator):
            try:
                self.calculation = eval(self.operator)
                self.labelOperator = self.ids["textOperator"]
                self.labelAnswer = self.ids["textAnswer"]
                self.labelOperator.text = str(self.calculation)
                self.labelAnswer.text = str(self.calculation)
                self.operator = str(self.calculation)
            except Exception:
                self.label = self.ids["textAnswer"]
                self.label.text = "Syntax Error"
            
    def btnPercent(self):
        if(self.calculation):   
            self.calcPercent = float(self.calculation) / 100
            self.labelOperator = self.ids["textOperator"]
            self.labelAnswer = self.ids["textAnswer"]
            self.labelAnswer.text = str(self.calcPercent)
            self.labelOperator.text = str(self.calcPercent)
            self.calculation = str(self.calcPercent)
            self.operator = str(self.calcPercent)
        elif(self.operator):
            try:
                self.calcPercent = float(self.operator) / 100
                self.labelOperator = self.ids["textOperator"]
                self.labelAnswer = self.ids["textAnswer"]
                self.labelOperator.text = str(self.calcPercent)
                self.labelAnswer.text = str(self.calcPercent)
                self.calculation = str(self.calcPercent)
                self.operator = str(self.calcPercent)
            except Exception:
                self.label = self.ids["textAnswer"]
                self.label.text = "Syntax Error"
           
    def btnDelKey(self):
        self.label = self.ids["textOperator"]
        if(self.operator):
            self.convertToList = list(self.operator)
            del(self.convertToList[-1])
            
            self.operator = "".join(self.convertToList)
            
            self.label.text = self.operator
            
    def btnClearKey(self):
        self.operator = ""
        self.labelOperator = self.ids["textOperator"]
        self.labelOperator.text = ""
        
        self.labelAnswer = self.ids["textAnswer"]
        self.labelAnswer.text = ""


class CalculatorApp(App):
    def build(self):
        return CalculatorWindow()
    
if __name__ == "__main__":
    CalculatorApp().run()