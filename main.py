
import spotipy
import pprint
import spotipy.util as util
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import requests
import time
client_id1 = "id here"
client_secret1 = "secret here"
from colorthief import ColorThief
from urllib.request import urlopen
import io
import webcolors

scopes = 'user-read-currently-playing user-modify-playback-state'

objectd = spotipy.SpotifyOAuth(client_id=client_id1,
                     client_secret=client_secret1,
                     redirect_uri="http://localhost:7777/callback",
                     scope=scopes)

token = objectd.get_access_token(as_dict=False)


spotify_object = spotipy.Spotify(auth=token)



root = Tk()

root.wm_attributes('-transparentcolor', root['bg'])

def compcolor(rgb):

    rgb = str(rgb)

    l = []
    l2 = []
    for x in rgb : 
        if x != "(" and x != ")" : 
            l.append(x)

    for x in "".join(l).split(", "):
        l2.append(x)

    r = 255 - int(l2[0])

    g = 255 - int(l2[1])

    b = 255 - int(l2[2])

    tup = (r,g,b)

    return webcolors.rgb_to_hex(tup)

root.geometry('800x325')

frame1= Frame(root, height= "325", width = "800")

song_name = ""

#pausepng = ImageTk.PhotoImage(Image.open(requests.get("https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-pause-512.png", stream=True).raw))


frame1.pack_propagate(False)

while True:
    time.sleep(1)

    current = spotify_object.current_user_playing_track()

    if current != None:

        root.update()
        
        if current['item']['name'] != song_name:

            #pause = Button( image=pausepng)
            
            song_name = current['item']['name']

            l = []

            for artist in current['item']['artists']:
                
                l.append(artist['name'])

            artists = ", ".join(l)

            img = current['item']['album']['images'][1]['url']

            image1 = ImageTk.PhotoImage(Image.open(requests.get(img, stream=True).raw))

            fd = urlopen(img)

            f = io.BytesIO(fd.read())

            color_thief = ColorThief(f)

            dominant_color = color_thief.get_color(quality=1)

            for item in frame1.winfo_children():

                item.destroy()

            main_color = webcolors.rgb_to_hex(dominant_color)

            frame1.config(bg=main_color)

            complimentary = compcolor(dominant_color)

            img1 = Label(frame1, image=image1, bg=main_color, fg = complimentary)

            songlabel = Label(frame1, text = song_name, bg=main_color, fg = complimentary, font = ('gotham rounded book', '14'))

            artistslabel = Label(frame1, text = artists, bg=main_color, fg = complimentary, font=('gotham rounded book', '9'))

            frame1.place(anchor="nw")

            img1.place(x=12.5, y = 12.5)
            
            artistslabel.place(x=320, y = 292.5)

            songlabel.place(x=320, y = 260.5)

            root.update()

    

        

