import kivy

# kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.button import Button
# from kivy.uix.label import Label

class MyApp(App):
    def build(self):
#        return Label(tex='Hello World')
        return Button(tex='Hello World')

if __name__=='__main__':
    MyApp().run()
