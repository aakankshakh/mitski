import sys
import pandas as pd

#generating lyrics txt file
sys.stdout = open('all_mitski_lyrics.txt', 'w')

mitski_df = pd.read_csv("mitski_song_lyrics.csv")

for lyrics in mitski_df['lyrics']:
    print(lyrics)
    print('\n!STOP!\n') #stop word for creating training set

sys.stdout.close()

#generating song title txt file
sys.stdout = open('all_mitski_song_titles.txt', 'w')

mitski_df = pd.read_csv("mitski_song_lyrics.csv")

for song_title in mitski_df['name']:
    print(song_title)

sys.stdout.close()