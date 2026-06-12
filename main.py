import argparse
from my_models.artist2 import Artist
from my_models.song2 import Song
from my_models.album2 import Album
from my_models.user2 import User
from functions import (
    create_artist, list_all_artists,
    create_song, list_all_songs,
    create_album, list_all_albums,
    create_user, list_all_users,
    add_favorite_song, add_favorite_album,
    view_favorites,
    search_by_artist, search_by_genre
)

#load data
def load_data():
    Artist.read_all()
    Song.read_all()
    Album.read_all()
    User.read_all()

def main():
    load_data()

    parser = argparse.ArgumentParser(
        prog = "Music Library",
        description="manage your music from the command line"
    )

    subparsers = parser.add_subparsers(
        dest = "command",
        help = "available commands"
    )

    #artist commands
    subparsers.add_parser(
        "add artist",
        help = "create a new artist",
    )

    subparsers.add_parser(
        "list artists",
        help = "list all artists",
    )

    #song commands
    subparsers.add_parser(
        "add song",
        help = "create a new song",
    )

    subparsers.add_parser(
        "list songs",
        help = "list all songs",
    )
    
    #album commands
    subparsers.add_parser(
        "add album",
        help = "create a new album",
    )

    subparsers.add_parser(
        "list albums",
        help = "list all albums",
    )

    #user commands
    subparsers.add_parser(
        "add user",
        help = "create a new user",
    )

    subparsers.add_parser(
        "list users",
        help = "list all users",
    )
    
    #favorite commands
    subparsers.add_parser(
        "add favorite song",
        help = "add a song to a user's favorites",
    )

    subparsers.add_parser(
        "add favorite album",
        help = "add an album to a user's favorites",
    )

    subparsers.add_parser(
        "view favorites",
        help = "view a user's favorites",
    )

    #search
    search_parser = subparsers.add_parser(
        "search",
        help="Search by artist or genre"
    )
    
    search_parser.add_argument(
        "--by",
        choices=["artist", "genre"],
        required=True,
        help="Search by artist or genre"
    )