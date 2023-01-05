import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class SyringeCounterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.syringes_used = 0

    def build(self):
        # Create a button to increment the counter
        button = Button(text='Use Syringe')
        button.bind(on_press=self.increment_syringes)

        # Create a label to display the counter
        label = Label(text=f'Number of syringes used: {self.syringes_used}')

        # Return the button and label as the root widget
        return button, label

    def increment_syringes(self, instance):
        # Increment the counter and update the label
        self.syringes_used += 1
        self.root.children[1].text = f'Number of syringes used: {self.syringes_used}'

if __name__ == '__main__':
    SyringeCounterApp().run()
