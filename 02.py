import pytube

url = 'https://www.youtube.com/watch?v=Wc_rsE0VJQg'

youtube = pytube.YouTube(url)
streams = youtube.streams.all()
for i in streams: # Retorna as resoluções do vídeo
    print(i)
video = youtube.streams.get_by_itag(22)
video.download ()
print('Download Completo!')