import pytube

url = input('Digite o link do vídeo: ')

youtube = pytube.YouTube(url)
streams = youtube.streams.all()

video = youtube.streams.get_by_itag(22)
video.download ()
print('Download Completo!')

