import json
import os
import spotipy
import boto3
from datetime import datetime  
from spotipy.oauth2 import SpotifyClientCredentials

def lambda_handler(event, context):
    
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    if not client_id or not client_secret:
        return {"error": "Spotify credentials not set"}

    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    
    playlist_link = "https://open.spotify.com/playlist/774kUuKDzLa8ieaSmi8IfS"
    playlist_uri = playlist_link.split("/")[-1].split("?")[0] 

    try:
        spotify_data = sp.playlist_tracks(playlist_uri)
    except spotipy.SpotifyException as e:
        return {"error": f"Spotify API Error: {str(e)}"}

    client = boto3.client('s3')
    filename = f"spotify_raw_{playlist_uri}.json"  

    try:
        client.put_object(
            Bucket="spotify-etl-complete-project",
            Key=f"raw_data/to_processed/{filename}",
            Body=json.dumps(spotify_data)
        )
        return {"message": "Success", "file": filename}
    except Exception as e:
        return {"error": f"S3 Upload Failed: {str(e)}"}
