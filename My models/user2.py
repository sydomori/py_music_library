import json
from my_models.person import Person
from my_models.song2 import Song
from my_models.album2 import Album

class User(Person):
    all = []
    FILE_PATH = "data/users.json"

    def __init__(self, name, email):
        super().__init__(name, email)
        self._favorite_songs = []
        self._favorite_albums = []
        User.all.append(self)

    def add_favorite_song(self, song):
        if song in self._favorite_songs:
            print(f"'{song.title}' is already in your favorites")
            return
        self._favorite_songs.append(song)
        print(f"Added '{song.title}' to favorites")

    def remove_favorite_song(self, song):
        if song not in self._favorite_songs:
            print(f"'{song.title}' is not in your favorites")
            return
        self._favorite_songs.remove(song)
        print(f"Removed '{song.title}' from favorites")
