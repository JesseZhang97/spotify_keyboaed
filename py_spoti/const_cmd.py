import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

# -------------------------------------------SPOTIFY-------------------------------------------
# auth verify
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b0749846ac1845bea752201825e7787c',
                                               client_secret='d1311ac290484889b47c2ea2b16b1e83', redirect_uri='http://localhost', scope=scope))
# show playing device info
res=sp.devices()
pprint(res)


# -------------------------------------------PYSERISAL-------------------------------------------

