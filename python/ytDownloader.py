from pytube import YouTube
import os
import sys


SAVE_PATH="/Users/tobiaskapfhammer/YouTube_Videos"
#link=argv[1]
link='https://www.youtube.com/watch?v=3NSkk31vFbU'
yt=YouTube(link)

print('Video title: ',yt.title)
print('Video views: ',yt.views)
#os.chdir("Macintosh HD/Benutzer/tobiaskapfhammer")
yt.streams.get_highest_resolution().download(SAVE_PATH)