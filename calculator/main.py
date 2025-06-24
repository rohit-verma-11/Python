from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


Window.size = 400,630


class CalculatorApp(App):
    def build(self):
        self.last_key = ''
        self.expression:str = ''
        self.label = Label(font_size=46,size_hint_y=0.2,halign='right',valign='center',width=400)
        self.label.text = self.expression
        base_layout = BoxLayout(orientation = 'vertical', padding=10,spacing=10)
        nav_bar = BoxLayout(orientation = 'horizontal', size_hint_y=None, height=50)
        keys = [
            ['%','CE','C','<'],
            ['1/x','^2','^0.5','/'],
            ['7','8','9','*'],
            ['4','5','6','+'],
            ['1','2','3','-'],
            ['+/-','0','.','=']
        ]
        keyboard = GridLayout(cols=4,spacing=2,size_hint_y=0.8)
        for row in keys:
            for key in row:
                if key == '=':
                    color=(0.961,0.961,0.863,1)
                elif key.isdigit():
                    color=(0.9,0.9,0.9,0.7)
                else:
                    color=(0.8,0.8,0.8,0.5)
                button = Button(text=key,background_color = color)
                button.bind(on_release=lambda instance, k = key: self.keypress(k))
                keyboard.add_widget(button)
        base_layout.add_widget(self.label)
        base_layout.add_widget(keyboard)
        return base_layout
    
    def keypress(self,key):
        try:
            if key == '=':
                self.expression = str(eval(self.expression))
            elif key in ('CE','C'):
                self.expression = ''
            elif key == '<':
                self.expression = self.expression[:-1]
            elif key == '1/x':
                self.expression = str(1/float(eval(self.expression)))
            elif key == '^2':
                self.expression += '**2'
            elif key == '^0.5':
                self.expression += '**0.5'
            elif key == '+/-':
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
            else:
                if self.last_key == '=' and key.isdigit():
                    self.expression = ''
                self.expression += key
            self.label.text = self.expression
            self.last_key = key
            print(self.expression)
        except Exception as e:
            self.label.text = "Error:"+str(e)
            self.expression = ''
CalculatorApp().run()