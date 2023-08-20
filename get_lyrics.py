import lyricsgenius
import pandas as pd
import sys

from dotenv import load_dotenv
import os
GENIUS_API_KEY = os.environ.get("GENIUS_API_KEY")

load_dotenv()
if not GENIUS_API_KEY:
    print('API Key not found. Exiting program.')
    exit()

#sys.stdout = open('all_lyrics.txt', 'w')
song_names = open('mitski_song_names.txt', 'r')

genius = lyricsgenius.Genius(GENIUS_API_KEY)
artist = genius.search_artist("Mitski",max_songs=0)

song_dict = {'name':[], 'lyrics':[]}
for name in song_names:
    song_dict['name'].append(name)

    song = artist.song(name)
    song_dict['lyrics'].append(song.lyrics)

print('SONG DICTIONARY!!!\n',song_dict)

df = pd.DataFrame(song_dict)
df.to_csv("mitski_song_lyrics.csv")
#sys.stdout.close()