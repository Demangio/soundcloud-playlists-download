from sclib import SoundcloudAPI, Track, Playlist
import os
from pathlib import Path
import numpy as np

playlists_file = open('playlists.txt', 'r')

playlists_table = playlists_file.read().splitlines()

playlists = [playlists_table[i].split(" ")[0] for i in range(len(playlists_table))]

folder_names = [playlists_table[i].split(" ")[1] for i in range(len(playlists_table))]

print(np.array(list(zip(folder_names, playlists))))

api = SoundcloudAPI()

for folder_name, playlist_url in zip(folder_names, playlists):

    print(playlist_url)

    playlist = api.resolve(playlist_url)

    for track in playlist.tracks:
        filename = f'{track.artist} - {track.title}'
        for i in filename:
            if ord(i) not in np.concatenate([np.arange(49,58),np.arange(65,91), np.arange(97,123), [32,45,97]]):
                filename = filename.replace(i, "")
            if ord(i) == 32:
                filename = filename.replace(i, "_")
        filename = f"{folder_name}/" + filename + '.mp3'
        if os.path.isfile(filename):
            pass
        else:
            with open(filename, 'wb+') as fp:
                track.write_mp3_to(fp)
                print(f"Downloading and saving {filename}")
