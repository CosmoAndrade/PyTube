from pytube import YouTube


url = input('Digite o Link !: ')
yt = YouTube(url).streams.get_by_itag(22).download()
print ('Download Completo!')
