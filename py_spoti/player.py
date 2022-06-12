import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import json

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b0749846ac1845bea752201825e7787c',
                     client_secret='d1311ac290484889b47c2ea2b16b1e83', redirect_uri='http://localhost', scope=scope))

# Shows playing devices
res = sp.devices()
mac_device_id = '7b552a49a23bfb184d001ea9e8ec560abfede93b'
pprint([item for item in res.get('devices') if item.get('id') == mac_device_id][0])
pprint([item for item in res.get('devices') if item.get('id') == mac_device_id][0].get('volume_percent'))

sp.volume(0)
# pprint(sp.current_playback())
# pprint(sp.current_user_playing_track())
# pprint(sp.currently_playing())
# pprint([item for item in res.get('devices') if item.get('id') == mac_device_id][1])

# pause playing
# sp.pause_playback()
# sp.start_playback(device_id='7b552a49a23bfb184d001ea9e8ec560abfede93b')
# pprint(sp.current_playback())
# Change track

# FIXME cant play liked song
# sp.start_playback(context_uri='spotify:playlist:4RHTIRJNFKPuF9wcmXEHD4',
#                   device_id='7b552a49a23bfb184d001ea9e8ec560abfede93b')

# Change volume
# sp.volume(100)
# sleep(2)
# sleep(2)
# sp.volume(100)
