# ----- IMPORT ----- #
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

# ----- FUNCTIONS ----- #
def convertVideo(url):
    # Create YouTube instance
    yt = YouTube(url)

    # Get stream
    stream = yt.streams.filter(only_audio=True).first()
    print(yt.title)
    return yt.title
    # streams: itag, mime_type, abr, codecs, type



# ----- UI COMPONENTS ----- #


# ----- SECTION ----- #
class InputSection(GridLayout):
    def __init__(self, **kwargs):
        super(InputSection, self).__init__(**kwargs)
        self.padding = 8
        self.rows = 3

        self.inputUrl = TextInput(multiline=False)
        self.add_widget(Label(text='Enter video URL:'))
        self.add_widget(self.inputUrl)
        downloadButton = Button(text='Download')
        self.add_widget(downloadButton)
   
        def callback():
            return convertVideo(self.inputUrl.text)
        
        downloadButton.bind(on_press=callback)



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