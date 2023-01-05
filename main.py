import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class SyringeCounter(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.syringes_used = 0

    def build(self):
        # Create a button to increment the number of syringes used
        button = Button(text='Use Syringe', on_press=self.increment_syringes)

        # Create a label to display the number of syringes used
        self.label = Label(text=f'Number of syringes used: {self.syringes_used}')

        return self.label

    def increment_syringes(self, instance):
        # Increment the number of syringes used and update the label
        self.syringes_used += 1
        self.label.text = f'Number of syringes used: {self.syringes_used}'

if __name__ == '__main__':
    SyringeCounter().run()
