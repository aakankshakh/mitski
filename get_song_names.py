import lyricsgenius
import sys

from dotenv import load_dotenv
import os
GENIUS_API_KEY = os.environ.get("GENIUS_API_KEY")

load_dotenv()
if not GENIUS_API_KEY:
    print('API Key not found. Exiting program.')
    exit()

sys.stdout = open('mitski_song_names.txt', 'w')

genius = lyricsgenius.Genius(GENIUS_API_KEY)
artist = genius.search_artist("Mitski")

sys.stdout.close()
