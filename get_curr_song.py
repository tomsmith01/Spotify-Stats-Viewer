import json
import requests

from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = ''

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']

    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        [artist['name'] for artist in artists]
    )

    link = resp_json['item']['external_urls']['spotify']

    current_track_info = {
        'id': track_id,
        'name': track_name,
        'artists': artists_names,
        'link': link
    }

    return current_track_info