from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.config import Config

Config.set('graphics', 'window_state', 'maximized')
typ="start"


class DfaWindow(Screen):
    global typ
    def start(self):
        typ="start"
        sm.current="comm"
    def end(self):
        typ="end"
        sm.current="comm"
    def ins(self):
        typ="ins"
        sm.current="comm"
    def active(self):
        sm.current="comm"
class NfaWindow(Screen):
    global typ
    def start(self):
        typ="start"
        sm.current="comm"
    def end(self):
        typ="end"
        sm.current="comm"
    def ins(self):
        typ="ins"
        sm.current="comm"
    def active(self):
        sm.current="comm"

class CommonFA(Screen):
    show="True"
    exp,st,text="","",""
    txt1 = ObjectProperty(None)
    txt2 = ObjectProperty(None)
    def process0(self):
        self.text = self.txt1.text 
        self.exp=self.text
    def process1(self):
        self.text = self.txt2.text 
        self.st=self.text
    def display(self):
        self.show="True"
        if typ=="start":
            if not(self.st.startswith(self.exp)):
                self.show="False"
        elif typ=="end":
            if not(self.st.endswith(self.exp)):
                self.show="False"
        else:
            if self.exp not in self.st:
                self.show="False"
        popup = Popup(title ="Result", content = Label(text=self.show), 
                        size_hint =(None, None), size =(200, 200))
        popup.open()
    pass



class WindowManager(ScreenManager):
    pass


kv1 = Builder.load_file("Auto.kv")
sm = WindowManager()

screens = [DfaWindow(name="dfa"), CommonFA(name="comm"), NfaWindow(name="nfa")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "dfa"


class Kivysub(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Kivysub().run()
