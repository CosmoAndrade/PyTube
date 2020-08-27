from pytube import YouTube

url = 'https://www.youtube.com/watch?v=56dFC6ccUGw'


yt = YouTube(url).streams.get_by_itag(22).download()

print ('Download Completo!')