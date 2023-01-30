from service import get_token, get_user_playlists, get_playlist_items, get_track
from chalice import Chalice


app = Chalice(app_name="helloworld")


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/playlist/user/{user_id}")
def get_user_playlits_controller(user_id):
    return get_user_playlists(get_token(), user_id)


@app.route("/playlist/items/{playlist_id}")
def get_playlist_items_controller(playlist_id):
    return get_playlist_items(get_token(), playlist_id)


@app.route("/playlist/tracks/{track_id}")
def get_track_controller(track_id):
    return get_track(get_token(), track_id)
