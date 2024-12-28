# Spotify Visualizer

A dynamic desktop application that displays your currently playing Spotify track with a color-adaptive interface that matches the album artwork.

## Display Components

### Album Artwork
```python
img = current['item']['album']['images'][1]['url']
image1 = ImageTk.PhotoImage(Image.open(requests.get(img, stream=True).raw))
img1 = Label(frame1, image=image1, bg=main_color, fg=complimentary)
img1.place(x=12.5, y=12.5)
```
- Displays current track's album art
- Updates automatically when track changes
- Positioned on the left side of the window
- High-quality image resolution

### Song Information
```python
# Artist Display
l = []
for artist in current['item']['artists']:
    l.append(artist['name'])
artists = ", ".join(l)
artistslabel = Label(frame1, text=artists, bg=main_color, fg=complimentary, 
                    font=('gotham rounded book', '9'))

# Song Title Display
songlabel = Label(frame1, text=song_name, bg=main_color, fg=complimentary, 
                 font=('gotham rounded book', '14'))
```
- Track title displayed in large, clear font
- All artist names shown below the title
- Multiple artists separated by commas
- Uses Gotham Rounded Book font family

### Dynamic Color Theme
```python
fd = urlopen(img)
f = io.BytesIO(fd.read())
color_thief = ColorThief(f)
dominant_color = color_thief.get_color(quality=1)
main_color = webcolors.rgb_to_hex(dominant_color)
complimentary = compcolor(dominant_color)
```
- Extracts dominant color from album artwork
- Automatically adjusts background to match
- Generates complementary text colors
- Ensures optimal readability

### Window Properties
```python
root = Tk()
root.wm_attributes('-transparentcolor', root['bg'])
root.geometry('800x325')
frame1 = Frame(root, height="325", width="800")
frame1.pack_propagate(False)
```
- Fixed size: 800x325 pixels
- Transparent background capability
- Clean, minimalist interface
- Responsive updates

## Installation and Setup

1. Clone the Repository
```bash
git clone https://github.com/raghavrat/spotify-visualizer.git
cd spotify-visualizer
```

2. Install Required Libraries
```bash
pip install spotipy pillow colorthief webcolors requests
```

3. Spotify API Setup
- Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create new application
- Set redirect URI to: `http://localhost:7777/callback`
- Add your credentials to the code

4. Run the Application
```bash
python main.py
```

## Requirements

- Python 3.7+
- Active Spotify Premium account
- Internet connection
- Spotify application running on any device

## Dependencies

- spotipy
- tkinter
- PIL (Pillow)
- colorthief
- webcolors
- requests

## Troubleshooting

1. Authentication Issues
- Check Client ID and Secret
- Verify redirect URI
- Confirm Spotify Premium subscription

2. Display Issues
- Check required fonts
- Verify screen resolution
- Check transparency support

