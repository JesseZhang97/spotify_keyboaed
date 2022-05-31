import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b0749846ac1845bea752201825e7787c',
                     client_secret='d1311ac290484889b47c2ea2b16b1e83', redirect_uri='http://localhost', scope=scope))

# Shows playing devices
res = sp.devices()
# pprint(res)

# pause playing
# sp.pause_playback()
# sp.start_playback(device_id='7b552a49a23bfb184d001ea9e8ec560abfede93b')
pprint(sp.current_playback())
# Change track
# sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

# Change volume
# sp.volume(100)
# sleep(2)
# sleep(2)
# sp.volume(100)
