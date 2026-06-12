import json
from my_models.artist2 import Artist
from my_models.song2 import Song

class Album:
    all = []
    FILE_PATH = "data/albums.json"

    def __init__(self, title, genre, release_year, artist):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.artist = artist
        self._songs = []
        Album.all.append(self)
        artist.add_album(self)

    def add_song(self, song):
        if song not in self._songs:
            self._songs.append(song)
        else:
            print(f"'{song.title}' is already in '{self.title}'")

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            print(f"'{song.title}' is not in '{self.title}'")
    @property
    def songs(self):
        return self._songs

    def list_songs(self):
        print(f"\nSongs in '{self.title}':")
        if self._songs:
            for song in self._songs:
                print(f"  - {song.title} by {song.artist.name}")
        else:
            print("  No songs added yet")

    def save_to_json(self):
        try:
            with open(self.FILE_PATH, 'r') as f:
                existing_data = json.load(f)
            existing_data.append({
                "title": self.title,
                "genre": self.genre,
                "release_year": self.release_year,
                "artist": self.artist.name,
                "songs": [song.title for song in self._songs]
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
        albums = []
        for album_info in data:
            artist = Artist.find_by_name(album_info["artist"])
            if artist:
                album = cls(
                    title=album_info["title"],
                    genre=album_info["genre"],
                    release_year=album_info["release_year"],
                    artist=artist
                )
                for song_title in album_info.get("songs", []):
                    song = Song.find_by_title(song_title)
                    if song:
                        album.add_song(song)
                albums.append(album)
        return albums

    @classmethod
    def find_by_title(cls, title):
        for album in cls.all:
            if album.title.lower() == title.lower():
                return album
        return None

    @classmethod
    def find_by_genre(cls, genre):
        return [a for a in cls.all if a.genre.lower() == genre.lower()]

    @classmethod
    def find_by_artist(cls, artist_name):
        return [a for a in cls.all if a.artist.name.lower() == artist_name.lower()]

    def __str__(self):
        return f"{self.title} by {self.artist.name} ({self.release_year})"

    def __repr__(self):
        return f"Album('{self.title}' by {self.artist.name}')"