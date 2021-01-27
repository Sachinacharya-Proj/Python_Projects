from pytube import YouTube
from pytube import Playlist
import os
username = os.environ.get("USERPROFILE")

def rename(direc):
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    os.rename(source, path)

asking = input("Playlist(P) or Single(S): ").lower()
if asking == 'p':
    url = input("Url: ")
    asking = input("Audio(A) or Video(V): ").lower()
    ytd = Playlist(url)
    if asking == 'a':
        j=1
        for audio in ytd.videos:
            title = audio.title
            print("{}: Audio {}.mp3 is downloading".format(j, title))
            cb = audio.streams.get_audio_only().download(f"{username}\\Music")
            rename(cb)
            j=j+1
    else:
        print("Downloading Videos")
        i=1
        for video in ytd.videos:
            title = video.title
            print("{}: Video {}.mp4 is downloading".format(i, title))
            video.streams.get_highest_resolution().download(f"{username}\\Videos")
            i=i+1
else:
    url = input("Url: ")
    asking = input("Audio(A) or Video(V): ").lower()
    ytd = YouTube(url)
    if asking == 'a':
        title = ytd.title
        print("Downloading Audio {}.mp3".format(title))
        cb = ytd.streams.get_audio_only().download(f"{username}/Music")
        ytd.register_on_complete_callback(rename(cb))
    else:
        print("Downloading Video {}.mp4".format(ytd.title))
        ytd.streams.get_highest_resolution().download(f"{username}/Videos")

print("\nDownload is Completed Successful\n")
