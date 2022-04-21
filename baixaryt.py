from pytube import YouTube, Search
from pytube.cli import on_progress
import requests
from bs4 import BeautifulSoup

#url = input("Cole o link do seu video aqui:\n")
url = "https://www.youtube.com/watch?v=wkX-7G0vF7s"
#op = int(input("1 para audio e 2 para video:"))



def baixaraudio(url):
    link = YouTube(url, on_progress_callback=on_progress)
    link.streams.get_audio_only(subtype="mp4").download()

def baixarvideo(url):
    link = YouTube(url, on_progress_callback=on_progress)
    link.streams.get_by_resolution("720p").download()

""" if op != 1:
    baixarvideo(url)
else:
    baixaraudio(url) """

def Tags(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.keywords
    print(r)



#busca = Search("RATO BORRACHUDO")
""" for i in range(0,3):
    video = 'https://www.youtube.com/watch?v='+str(busca.results[i])[41:-1]
    Tags(video) """

#busca.results.sort(reverse=True)

baixaraudio(url)