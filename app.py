# ----- IMPORT ----- #
#os
import os
# kivy
import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ColorProperty
# pytube
from pytubefix import YouTube
# ffmpeg-python
import ffmpeg

# ----- FUNCTIONS ----- #




# ----- UI COMPONENTS ----- #


# ----- SECTION ----- #
class InputSection(GridLayout):
    def __init__(self, **kwargs):
        super(InputSection, self).__init__(**kwargs)
        self.padding = 8
        self.rows = 3

        # Input for video URL
        self.inputUrl = TextInput(multiline=False)
        self.add_widget(Label(text='Enter video URL:'))
        self.add_widget(self.inputUrl)

        # Download button
        self.downloadButton = Button(text='Download')
        self.downloadButton.bind(on_press=self.downloadMusic)
        self.add_widget(self.downloadButton)

    def downloadMusic(self, instance):
        url = self.inputUrl.text
        
        # Instance YouTube object
        yt = YouTube(url)

        # Get stream
        stream = yt.streams.filter(only_audio=True).first()

        # Get filename without blank spaces
        filename = yt.title.replace(' ', '')

        # Download file
        stream.download(mp3=True, filename=filename, output_path='mp3')
        
        # Convert mp4a to mp3
        stream = ffmpeg.input(f'mp3/{filename}.mp3')
        stream = ffmpeg.output(stream, f'mp3/{filename}-mp3.mp3')
        ffmpeg.run(stream, overwrite_output=True)
        os.remove(f'mp3/{filename}.mp3')






# ----- APP CLASS ----- #

# App subclass
class MyApp(App):
    # Build method
    def build(self):
        self.title = 'Musica'
        self.icon = 'icon.png'

        return InputSection()

# Run App
if __name__ == '__main__':
    MyApp().run()