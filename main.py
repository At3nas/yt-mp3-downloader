# ---- IMPORTS ---- #
# os
import os
# kivy / kivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
# pytubefix
from pytubefix import YouTube
# ffmpeg-python
import ffmpeg


# ---- KIVY ---- #
KV = '''
MDScreen:
    dl_status: dl_status
    input_url: input_url
    md_bg_color: self.theme_cls.backgroundColor 

    MDBoxLayout:
        orientation: 'vertical'
        spacing: '16dp'
        padding: '16dp', '32dp'
    
        MDLabel:
            text: 'Enter video URL:'
            halign: 'center'
        
        MDTextField:
            id: input_url
            mode: 'outlined'

            MDTextFieldLeadingIcon:
                icon: 'link'

        MDButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press: app.downloadMusic()

            MDButtonIcon:
                icon: 'download'
            MDButtonText:
                text: 'Download'
        
        MDLabel:
            id: dl_status
            text: ''
'''

# ---- MAIN ---- #
class MainApp(MDApp):
    dl_status = ObjectProperty()
    input_url = ObjectProperty()
    

    def build(self):
        return Builder.load_string(KV)
    
    def downloadMusic(self):
        #self.root.dl_status.text = 'Starting download...'
        url = self.root.input_url.text

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
    
# Run app
if __name__ == '__main__':
    MainApp().run()