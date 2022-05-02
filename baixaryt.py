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
    link.streams.get_by_resolution("720p").download()

def Tags(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.keywords
    print(r)

def getTitulo(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.title
    return r


l = ['https://www.youtube.com/watch?v=nny6kuchJ7o']

for i in l:
    baixaraudio(i)

