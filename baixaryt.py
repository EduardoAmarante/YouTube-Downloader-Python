from pytube import YouTube, Search
from pytube.cli import on_progress
import requests
from bs4 import BeautifulSoup


def baixaraudio(url):
    link = YouTube(url, on_progress_callback=on_progress)
    print("\n Baixando o audio: ",getTitulo(url))
    link.streams.get_audio_only(subtype="mp4").download()

def baixarvideo(url):
    link = YouTube(url, on_progress_callback=on_progress)
    
    print('1080')
    link.streams.filter(res="720p").first().download()

    # print('720')
    # link.streams.get_by_resolution("720p").download()

def Tags(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.keywords
    print(r)

def getTitulo(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.title
    return r

ratoborrachudo = [
'https://youtu.be/zWCvgOYerUU',
'https://youtu.be/-0i_ZAIzQBE'
'https://youtu.be/JRUTUcAX51A']

# for video in ratoborrachudo:
#     print(getTitulo(video))
#     baixarvideo(video)

# baixarvideo('https://www.youtube.com/watch?v=akzT9gqw3Bk')

baixaraudio('https://youtu.be/nny6kuchJ7o')
baixaraudio('https://youtu.be/rD7_OB3Ua1w')