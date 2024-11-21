## Spotify-to-YouTube Playlist Converter

A Python tool that converts a Spotify playlist into a YouTube Music playlist. This project uses the Spotify Web API and YouTube Data API to fetch tracks from a Spotify playlist and create a new playlist in your YouTube account with matching tracks.


## Features

- Fetches all tracks from a public Spotify playlist.
- Searches for matching tracks on YouTube.
- Creates a public YouTube playlist and adds the tracks to it. 
- Easy to set up and use.

## Requirements
- Python 3.7 or higher.
- Spotify and YouTube API credentials.
## Installation

Clone repository

```bash
    git clone https://github.com/BenceGLGDev/Spotify-to-YouTube-Playlist-Converter
    cd spotify-to-youtube
```

Install Dependencies: Install the required libraries listed in requirements.txt:
```bash
    pip install -r requirements.txt
```
## Set Up API Credentials:

Spotify:

- Go to the Spotify Developer Dashboard [Link](https://developer.spotify.com/dashboard "Heading link")
- Create an app and copy the Client ID and Client Secret.
- Open spotify_api.py and replace SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET with your credentials.
YouTube:

- Go to the Google Cloud Console [Link](https://cloud.google.com/cloud-console)
- Create a new project and enable the YouTube Data API v3.
- Create OAuth 2.0 credentials and download the client_secret.json file.
- Place client_secret.json in the project directory.



## Usage

Run the script
```bash
python main.py
```
Follow the Prompts:

- Enter the Spotify playlist link.
- Enter a name for your new YouTube playlist.

## Authenticate with YouTube
- A browser window will open for you to log into your Google account and authorize the application (only required on the first run).
## Conversion Process
- The script will fetch tracks from Spotify, search for them on YouTube, and add them to a new YouTube playlist.
## View the Playlist
- Once the script completes, the YouTube playlist will be available in your account.
## File Structure
```graphql
spotify_to_youtube/
│
├── spotify_api.py         # Handles Spotify API-related operations
├── youtube_api.py         # Handles YouTube API-related operations
├── main.py                # Main script to run the program
├── client_secret.json     # YouTube API credentials file (required)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation (this file)
```
## Example Workflow
Run the program:
```bash
python main.py
```
Enter the Spotify playlist link, e.g.:
```arduino
https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
```
Enter a YouTube playlist name, e.g.:
```bash
My YouTube Playlist Name
```
The program will display logs like:
```yaml
Added: Song Name - Artist Name
Could not find: Song Name - Artist Name
```
Once complete, check your YouTube account for the new playlist.
## Troubleshooting
Common Issues
- ModuleNotFoundError: Ensure all dependencies are installed by running:
```bash
pip install -r requirements.txt
```
- Invalid Spotify Link: Make sure the playlist link is valid and public.
+ YouTube Authentication Issues:
    + Ensure client_secret.json is correctly set up.
    + Delete the token.pickle file and reauthenticate if necessary.
- Debugging Tips
    + Run the script in verbose mode (add print() statements) to pinpoint issues.
    + Check for typos in API credentials or playlist links.
