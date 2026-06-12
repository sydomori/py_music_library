import json
from models.person import Person

class Artist:
    all = []
    FILE_PATH = "data/artists.json"

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self._songs = []
        self._albums = []
        Artist.all.append(self)

    def add_song(self, song):
        if song not in self._songs:
            self._songs.append(song)

    def add_album(self, album):
        if album not in self._albums:
            self._albums.append(album)
