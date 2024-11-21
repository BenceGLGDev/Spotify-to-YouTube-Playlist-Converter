from spotify_api import get_spotify_tracks
from youtube_api import authenticate_youtube, search_youtube, create_youtube_playlist, add_video_to_playlist

def main():
    print("Welcome to Spotify-to-YouTube Playlist Converter!")
    
    # Get Spotify playlist
    spotify_link = input("Enter Spotify playlist link: ")
    tracks = get_spotify_tracks(spotify_link)
    
    # Authenticate with YouTube
    youtube = authenticate_youtube()
    
    # Create YouTube playlist
    playlist_name = input("Enter a name for your YouTube playlist: ")
    youtube_playlist_id = create_youtube_playlist(youtube, playlist_name)
    
    print("\nConverting playlist...")
    for track in tracks:
        video_id = search_youtube(youtube, track)
        if video_id:
            add_video_to_playlist(youtube, youtube_playlist_id, video_id)
            print(f"Added: {track}")
        else:
            print(f"Could not find: {track}")
    
    print(f"\nConversion complete! Your playlist is public and available on YouTube.")

if __name__ == "__main__":
    main()
