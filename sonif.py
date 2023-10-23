import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from textblob import TextBlob
import csv
# Set up your Spotify API credentials
client_id = os.getenv('SPOTIPY_CLIENT_ID')  # Replace with your own client_id
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')  # Replace with your own client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_polarity = analysis.sentiment.polarity
    return sentiment_polarity

def get_playlist_metadata(playlist_uri):
    # Rest of the code...

    # Get all tracks in the playlist
    tracks = sp.playlist_tracks(playlist_uri)

    # Create a list to store track data
    track_data = []

    # Loop through each track and retrieve track data
    for idx, item in enumerate(tracks['items']):
        track = item['track']
        track_name = track['name']
        track_artists = ', '.join([artist['name'] for artist in track['artists']])
        track_album = track['album']['name']
        track_popularity = track['popularity']
        track_sentiment = analyze_sentiment(track_name)
        track_uri = track['uri']
        audio_features = sp.audio_features(track_uri)[0]

        # Append track data to the list
        track_data.append({
            'Track Name': track_name,
            'Artists': track_artists,
            'Popularity': track_popularity,
            'Danceability': audio_features['danceability'],
            'Energy': audio_features['energy'],
            'Loudness': audio_features['loudness'],
            'Liveness': audio_features['liveness'],
            'Tempo': audio_features['tempo']
        })

    # Sort track data by danceability, energy, and tempo in descending order
    track_data.sort(key=lambda x: (x['Danceability'], x['Energy'], x['Tempo']), reverse=True)

    # Write sorted track data to CSV
    with open('playlist_metadata.csv', 'w', newline='') as csvfile:
        fieldnames = ['Track Name', 'Artists', 'Popularity', 'Danceability', 'Energy', 'Loudness', 'Liveness', 'Tempo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for track in track_data:
            writer.writerow(track)



# Specify the Spotify playlist URI
playlist_uri = 'https://open.spotify.com/playlist/4U0jzJ06jwAJYBeSM7WwEH?si=6b51b0ed35484b89'  # Replace with your own playlist URI
get_playlist_metadata(playlist_uri)
