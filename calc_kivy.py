from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign='right', font_size=55)
        main_layout.add_widget(self.solution)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_but)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            
        opa_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        opa_button.bind(on_press=self.on_opa)
        main_layout.add_widget(opa_button)
        
        return main_layout
    def on_but(self, button):
        if button.text == 'C':
            self.solution.text = ''
        else:
            self.solution.text += button.text
    def on_opa(self, buton):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = 'Error'
MainApp().run()