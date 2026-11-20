from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.uix.filechooser import FileChooserListView
from kivy.core.audio import SoundLoader

class GuilhermePlayer(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Guilherme Player - Video e Musica', size_hint_y=0.1)
        self.video = Video(source='', state='play')
        self.chooser = FileChooserListView(filters=['*.mp3','*.mp4','*.wav','*.m4a'])
        self.chooser.bind(on_submit=self.abrir)
        btn = Button(text='Toque 2x no arquivo para abrir', size_hint_y=0.1)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.video)
        self.layout.add_widget(self.chooser)
        self.layout.add_widget(btn)
        return self.layout

    def abrir(self, chooser, selection, *args):
        if not selection:
            return
        arquivo = selection[0]
        self.label.text = arquivo.split('/')[-1]
        if arquivo.endswith('.mp4'):
            self.video.source = arquivo
            self.video.state = 'play'
        else:
            self.som = SoundLoader.load(arquivo)
            if self.som:
                self.som.play()

GuilhermePlayer().run()
