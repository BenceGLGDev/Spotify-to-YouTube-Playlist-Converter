import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"

def get_spotify_tracks(playlist_link):
    """Fetch track details from a Spotify playlist."""
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
    ))
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    results = sp.playlist_items(playlist_id)
    return [f"{item['track']['name']} {item['track']['artists'][0]['name']}" for item in results['items']]
