from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.label import Label

# interface
class Interface(GridLayout): # Change (..) depending on Layout
    def On_Enter_Pressed(self):
        print("Enter has been pressed! \n Good job!")
    def On_Text_Field_Press(self):
        self.text = ""


# app creation
class TestApp(MDApp):
    pass


TestApp().run()