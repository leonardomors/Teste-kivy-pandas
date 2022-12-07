from kivy.app import App
import mainwidget
from kivy.lang.builder import Builder
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        self._widget = mainwidget.MainWidget()
        return self._widget

if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    Window.size = (800,600)
    MyApp().run()