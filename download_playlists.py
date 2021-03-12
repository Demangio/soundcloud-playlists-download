from sclib import SoundcloudAPI, Track, Playlist
import os
from pathlib import Path
import numpy as np

playlists_file = open('playlists.txt', 'r')

folders_names_file = open('folders_names.txt', 'r')

folder_names = folders_names_file.read().splitlines()

playlists_table = playlists_file.read().splitlines()

print(playlists_table)

print(folder_names)

api = SoundcloudAPI()

for index_playlist, playlist_url in enumerate(playlists_table):


    playlist = api.resolve(playlist_url)


    for track in playlist.tracks:
        filename = f'{track.artist} - {track.title}'
        for i in filename:
            if ord(i) not in np.concatenate([np.arange(49,58),np.arange(65,91), np.arange(97,123), [32,45,97]]):
                filename = filename.replace(i, "")
            if ord(i) == 32:
                filename = filename.replace(i, "_")
        filename = f"{folder_names[index_playlist]}/" + filename + '.mp3'
        if os.path.isfile(filename):
            print(f"File {filename} already exists")
        else:
            with open(filename, 'wb+') as fp:
                track.write_mp3_to(fp)
                print(f"Downloading and saving {filename}")