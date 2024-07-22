from pytubefix import YouTube
import os

loop = True

while(loop):
    # Video URL
    print("Enter URL:")
    url = input("> ")

    # YouTube Object
    yt = YouTube(url)

    # Get first result
    stream = yt.streams.filter(only_audio=True).first()
    filename = yt.title.replace(' ', '')
    print("File: " + filename)
    # print(stream)
    # print('')
    # print('Enter itag:')
    # itag = input('> ')
    #stream = stream.get_by_itag(itag)



    # Download file
    stream.download(output_path="mp3", mp3=True, filename=filename)
    

    # Convert files
    os.chdir('C:/Users/ateka/OneDrive/Documents/coding/py-yt-mp3-converter/mp3')
    cmd = "ffmpeg -i "+filename+".mp3"+" -c:a libmp3lame -q:a 8 "+filename+"2.mp3"
                    # (!) Tal vez: Cambiar nombre del archivo output
    print(cmd)
    os.system(cmd)

    # Loop
    print("Download more music? (y/n)")
    answer = input("> ")

    if answer == 'n':
        loop = False