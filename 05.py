from pytube import YouTube

url = ''

while True:
    url = input('Digite o Link , e "stop" para Encerrar !: ')
    if url == 'stop':
        break

    yt = YouTube(url).streams.get_by_itag(22).download()

    print ('Download Completo!')

   

        