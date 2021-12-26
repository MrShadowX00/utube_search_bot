import urllib.request
import re
from pytube import YouTube
import moviepy.editor as mp
import asyncio

def ubot_result(text):
    result = []
    search_keyword=text.replace(" ","+")
    print(text)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video_ids)
    for i in video_ids:
        result.append("https://www.youtube.com/watch?v=" + i)
    return result

def get_video_info(video_link):
    my_video = YouTube(video_link)
    print(my_video.title)
    print(my_video.thumbnail_url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(filename="out.mp4")
    clip = mp.VideoFileClip("out.mp4")
    clip.audio.write_audiofile("out.mp3")
    
# ubot_result("yagzon")
