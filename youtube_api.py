from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os

# YouTube API Scope and Credential File
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
CREDENTIALS_FILE = "client_secret.json"

def authenticate_youtube():
    """Authenticate and return a YouTube API client."""
    creds = None
    token_file = "token.pickle"
    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_file, "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

def search_youtube(youtube, query):
    """Search for a track on YouTube and return the first video ID."""
    response = youtube.search().list(part="snippet", q=query, maxResults=1).execute()
    return response["items"][0]["id"]["videoId"] if response["items"] else None

def create_youtube_playlist(youtube, title, description="Converted from Spotify"):
    """Create a public YouTube playlist and return its ID."""
    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {"title": title, "description": description},
            "status": {"privacyStatus": "public"}
        }
    ).execute()
    return response["id"]

def add_video_to_playlist(youtube, playlist_id, video_id):
    """Add a video to a YouTube playlist."""
    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {"kind": "youtube#video", "videoId": video_id}
            }
        }
    ).execute()
