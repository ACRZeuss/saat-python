import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
import time

class MyApp(App):
    def build(self):
        return Builder.load_string(
'''
Label:
    font_size: 50'''
    )
    def on_start(self):
        Clock.schedule_interval(
            self.update, 1
        )
    def update(self, *args):
        h = time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
        self.root.text = h+":"+m+":"+s

MyApp().run()
