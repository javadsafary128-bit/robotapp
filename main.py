from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        forward = Button(text="FORWARD")
        back = Button(text="BACK")
        left = Button(text="LEFT")
        right = Button(text="RIGHT")

        forward.bind(on_press=self.forward)
        back.bind(on_press=self.back)
        left.bind(on_press=self.left)
        right.bind(on_press=self.right)

        layout.add_widget(forward)
        layout.add_widget(back)
        layout.add_widget(left)
        layout.add_widget(right)

        return layout

    def forward(self, instance):
        print("FORWARD")

    def back(self, instance):
        print("BACK")

    def left(self, instance):
        print("LEFT")

    def right(self, instance):
        print("RIGHT")


MyApp().run()
