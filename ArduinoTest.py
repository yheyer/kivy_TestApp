from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget



class Function(Screen):
    def play_led(self):
        board.digital[pin].write(1)
    def off_led(self):
        board.digital[pin].write(0)

class Main(MDApp):
    def build(self):
        Builder.load_file("layoutArduinoTest.kv")
        return Function()

Main().run()