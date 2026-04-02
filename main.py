from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import yt_dlp
import os

class MiApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.layout.add_widget(Label(text="Pegar enlace de YouTube:", size_hint_y=None, height=40))
        
        self.url_input = TextInput(multiline=False, size_hint_y=None, height=50)
        self.layout.add_widget(self.url_input)

        self.status_label = Label(text="Esperando...")
        self.layout.add_widget(self.status_label)

        btn = Button(text="Descargar Video", size_hint_y=None, height=60, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=self.descargar)
        self.layout.add_widget(btn)

        return self.layout

    def descargar(self, instance):
        url = self.url_input.text
        if not url:
            self.status_label.text = "¡Error: Pega un enlace!"
            return

        self.status_label.text = "Descargando..."
        
        # Configuración de yt-dlp para descargar en la carpeta de la app
        ydl_opts = {
            'format': 'best',
            'outtmpl': '/sdcard/Download/%(title)s.%(ext)s', # Intenta guardar en Descargas
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "¡Descarga completa en /Descargas!"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    MiApp().run()

