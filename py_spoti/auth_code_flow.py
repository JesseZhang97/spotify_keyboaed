import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b0749846ac1845bea752201825e7787c',
                     client_secret='d1311ac290484889b47c2ea2b16b1e83', redirect_uri='http://localhost', scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])
