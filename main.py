from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MiApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        btn = Button(text="Descargar video", font_size=20)
        btn.bind(on_press=self.descargar)

        layout.add_widget(btn)
        return layout

    def descargar(self, instance):
        print("Botón funcionando")

MiApp().run()
