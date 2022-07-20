from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.theming import ThemeManager
Config.set('kivy', 'keyboard_mode', 'systemanddock')
#Window.size = (480, 800)
Builder.load_string('''


<Cesarus>:
    rows: 5
    padding: 10
    text1: text1
    text2: text2
    lbl: lbl
    AnchorLayout:
        size_hint: 1, .25
        
        
        MDTextField:
            id: text1
            font_size: '30sp'
            multiline: False
            input_type: 'text'
            #input_filter: 'str'
            hint_text: 'введите слово(а)'
            
    AnchorLayout:
        size_hint: 1, .25
        MDTextField:
            id: text2
            font_size: '30sp'
            multiline: False
            input_type: 'number'
            input_filter: 'int'
            hint_text: 'введите шаг'
            
    BoxLayout:
        AnchorLayout:
            anchor_y: 'top'
            #anchor_x: 'center_x'
            MDLabel:                           
                text: 'Ваш шифр:'
                font_size: '33sp'
                bold: True
        MDLabel:
        
            id: lbl
            text: ''
            font_size: '33sp'
            italic: True
            
    
    GridLayout:
        cols: 2
        spacing: 10
        padding: [0, 30, 0, 0]
        size_hint: .9, .25
        MDRaisedButton:
            size_hint: 1, .5
            text: 'ЗАШИФРОВАТЬ'
            bold: True
            
            on_release: root.cesar()
        MDRaisedButton:
            size_hint: 1, .5
            text: 'ДЕШИФРОВАТЬ'
            bold: True
            on_release: root.decesar()
    MDLabel:
        size_hint: 1, .15
        text: "made by EF.corp"
        italic: True

                    ''')
class Cesarus(GridLayout):

    def cesar(self):
        #self.txt = ''
        #l, s = input().upper(), int(input())
        #instance.background_color = [1, 0, 0, 0]
        l = self.text1.text.upper()
        s = int(self.text2.text)
        p = ''
        bukvi = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        for i in l:
            pos = bukvi.find(i)
            npos = pos + s
            if i in bukvi:
                p += bukvi[npos]
            else:
                p += i
        #print(p.lower())
        #self.txt +=
        self.lbl.text = p.lower()#self.txtself.update_label()
    def decesar(self):

        #l, s = input().upper(), int(input())
        #instance.background_color = [1, 0, 0, 0]
        l = self.text1.text.upper()
        s = int(self.text2.text)
        p = ''
        bukvi = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        for i in l:
            pos = bukvi.find(i)
            npos = pos - s
            if i in bukvi:
                p += bukvi[npos]
            else:
                p += i
        #print(p.lower())
        self.lbl.text = p.lower()
        #self.txt += p.lower()
        #self.lb.text = self.txt
        #self.update_label()

class cesarusApp(MDApp):
    tem_clc = ThemeManager()
    title='CESAR'
    def build(self):
        self.tem_clc.theme_style = 'Light'
        return Cesarus()


if __name__ == "__main__":
    cesarusApp().run()