from pytube import YouTube

url = 'https://www.youtube.com/watch?v=56mjY8IyA2Y'


yt = YouTube(url).streams.first().download()

print ('Download Completo!')