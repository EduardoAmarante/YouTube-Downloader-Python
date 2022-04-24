from pytube import YouTube, Search
from pytube.cli import on_progress
import requests
from bs4 import BeautifulSoup

def baixaraudio(url):
    link = YouTube(url, on_progress_callback=on_progress)
    link.streams.get_audio_only(subtype="mp4").download()

def baixarvideo(url):
    link = YouTube(url, on_progress_callback=on_progress)
    link.streams.get_by_resolution("720p").download()

def Tags(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.keywords
    print(r)

def getTITULO(url):
    link = YouTube(url, on_progress_callback=on_progress)
    r = link.title()
    print(r)

l = ['https://youtu.be/R2-0Rm8r1ik','https://youtu.be/8JhJPQHm7zA','https://youtu.be/fPDMHkS7p_w','https://youtu.be/cz-hbcVrVN8','https://youtu.be/gO2ISGyqtyM','https://youtu.be/rnjdmhUjkSo','https://www.youtube.com/watch?v=xUzeIy7EaOc','https://youtu.be/fsRUdiVznxc','https://youtu.be/mr1qPTxi0k0','https://youtu.be/_3MC8XZRnHs','https://youtu.be/ZnCxpsjFh78','https://youtu.be/haeB72i_UQU','https://youtu.be/dqrtyu6sPlE','https://youtu.be/-8mAxLSzSag','https://youtu.be/rHJIlSECIA8','https://youtu.be/YIjoOTSH3gY','https://youtu.be/NY8rWK4XRHQ','https://youtu.be/C060FJCs8dI','https://youtu.be/BOfQqJwew7I','https://youtu.be/VeTLQsAYSCI','https://youtu.be/BxVVNa3_nEg']

print(len(l))

""" for i in l:
    #getTITULO(i)
    baixaraudio(i) """

baixaraudio('https://youtu.be/xUzeIy7EaOc')