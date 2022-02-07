from datetime import datetime

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.label import Label

Builder.load_file('OtherFile.kv')  # import External Interface


class ExternalKivy(BoxLayout):  # External Main Interface in other .kv file
    pass


class Variables(BoxLayout):  # defining Variables in .kv files
    _text_ = "helloo"


class LogicalInterface(BoxLayout):
    def OnPressing(self, ID):
        print("Button pressed!")
        time = datetime.now().strftime('%H:%M:%S')
        ID.text = 'Current Time: ' + time

    def OnReleasing(self, ID, input):
        print("Button released!")
        ID.text = input.text


# interface
class Page_Layout(PageLayout):
    pass


class Page_1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello", background_color=(.3, .4, .5, 1))
        b2 = Button(text="World", background_color=(.3, .4, .6, 1))
        self.add_widget(b1)
        self.add_widget(b2)


class Page_2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Page", background_color=(.4, .9, .5, 1))
        b2 = Button(text="Two", background_color=(.5, .9, .5, 1))
        self.add_widget(b1)
        self.add_widget(b2)


class Page_3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Page", background_color=(.8, .3, .5, 1))
        b2 = Button(text="Three", background_color=(.8, .2, .5, 1))
        self.add_widget(b1)
        self.add_widget(b2)


class RelativePractice(FloatLayout):
    pass


class scroller():
    pass


class StackInterface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b1 = Button(text=str(i + 1), size_hint=(None, None), size=(100, 100))
            self.add_widget(b1)


# Bindings
class Binding(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello")
        b1.bind(on_press=self.callback_function)
        self.add_widget(b1)

    def callback_function(self, event):
        print("Hello World!")


class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Game(BoxLayout):
    def create_btn(self):
        print("Created")

    def remove_btn(self):
        print("Removed")


# app creation
class TestApp(MDApp):
    pass
    # def build(self):
    #    return Binding()  # use with external Builder


TestApp().run()
