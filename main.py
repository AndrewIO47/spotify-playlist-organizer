from email import header
from http import client
import json
from lib2to3.pgen2 import token
from unicodedata import name
from dotenv import load_dotenv
import os
import base64
from requests import post, get

load_dotenv()

client_id = "eb83c2bc3dc2445ca70717fd88e29a98"
client_secret = "9c01a944a6744f88a188dedfcb9d076d"


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
    # print("\n")
    # print("\n")
    # print("\n")
    # print(result.content)
    # print("\n")
    # print("\n")
    # print("\n")
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)


def get_user_playlists(token, user_id):
    url = "https://api.spotify.com/v1/users/{user_id}/playlists".format(user_id=user_id)
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    json_formated = json.dumps(json_result, indent=4)

    return json_result
    # print(json_formated)


def get_user_playlist_id_and_name(token):
    json_result = get_user_playlists("andrewjoshuacf")
    id_name_list = []

    for item in json_result["items"]:
        playlist_id = item["id"]
        name = item["name"]

        object = {playlist_id, name}
        id_name_list.append(object)

    print(id_name_list)


token = get_token()
# print(token)
# search_for_artist(token, "ACDC")

get_user_playlist_id_and_name(token, "andrewjoshuacf")
