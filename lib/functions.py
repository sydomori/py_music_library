from models.songs import Song
from models.albums import Album

GLOBAL_SONGS = {}
GLOBAL_ALBUMS = {}


def add_new_song (title, genre, artist, duration):
    new_song = Song(title, genre, artist, duration)

    GLOBAL_SONGS[title] = new_song
    print(f"Success: Added song '{title}' to the Library.")


def  add_new_album(title,artist,genre,release_year):
    new_album=Album(title,artist,genre,release_year)

    GLOBAL_ALBUMS[title]= new_album
    print(f"Success:Added album '{title} to the Library")