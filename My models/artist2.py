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
    @property
    def songs(self):
        return self._songs

    @property
    def albums(self):
        return self._albums

    def get_discography(self):
        print(f"\n{self.name}'s Discography")
        print("Songs")
        if self._songs:
            for song in self._songs:
                print(f"  - {song.title} ({song.genre})")
        else:
            print("  No songs yet")
        print("Albums")
        if self._albums:
            for album in self._albums:
                print(f"  - {album.title} ({album.release_year})")
        else:
            print("  No albums yet")

    def save_to_json(self):
        try:
            with open(self.FILE_PATH, 'r') as f:
                existing_data = json.load(f)
            existing_data.append({
                "name": self.name,
                "genre": self.genre
            })
            with open(self.FILE_PATH, 'w') as f:
                json.dump(existing_data, f)
            print(f'{self} successfully saved')
        except Exception as e:
            print(f'An error occurred: {e}')

    @classmethod
    def read_all(cls):
        with open(cls.FILE_PATH, 'r') as f:
            data = json.load(f)
        all_artists = [cls(**artist_info) for artist_info in data]
        return all_artists

    @classmethod
    def find_by_name(cls, name):
        for artist in cls.all:
            if artist.name.lower() == name.lower():
                return artist
        return None

    @classmethod
    def find_by_genre(cls, genre):
        return [a for a in cls.all if a.genre.lower() == genre.lower()]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Artist('{self.name}')"