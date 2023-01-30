from email import header
from hashlib import new
from http import client
import json
from lib2to3.pgen2 import token
from unicodedata import name
from dotenv import load_dotenv
import os
import base64
from requests import post, get

load_dotenv()

# client_id =
# client_secret =


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def get_user_playlists(token, user_id):
    url = "https://api.spotify.com/v1/users/{user_id}/playlists".format(user_id=user_id)
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    json_formated = json.dumps(json_result, indent=4)  # formats the JSON like postman

    playlists_id_list = []
    for item in json_result["items"]:  # returns list[] of dictionaries{}
        playlist_id = item["id"]
        object = {"playlist_id": playlist_id}
        playlists_id_list.append(object)

    # returns a list of the users playlist_id
    return json.dumps(playlists_id_list)


def get_playlist_items(token, playlist_id):
    url = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(
        playlist_id=playlist_id
    )
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    json_formated = json.dumps(json_result, indent=4)  # formats the JSON like postman

    list_of_tracks_id = []
    for item in json_result["items"]:
        track_id = item["track"]["id"]
        list_of_tracks_id.append(track_id)

    # returns a list of the tracks name from a playlist
    return list_of_tracks_id


def get_track(token, track_id):
    url = "https://api.spotify.com/v1/tracks/{id}".format(id=track_id)
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    json_formated = json.dumps(json_result, indent=4)  # formats the JSON like postman

    artists = json_result["artists"]
    return artists
