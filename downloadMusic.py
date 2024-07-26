from pytubefix import YouTube
import ffmpeg
import os

loop = True

while(loop):
    # Get video URL from user
    print("Enter URL:")
    url = input("> ")

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

    # Loop
    print("Download more music? (y/n)")
    answer = input("> ")

    if answer == 'n':
        loop = False