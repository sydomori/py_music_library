import json
from My_models.artist2 import Artist

class Song:
    all = []
    FILE_PATH = "data/songs.json"

    def __init__(self, title, genre, artist):
        self.title = title
        self.genre = genre
        self.artist = artist
        Song.all.append(self)
        artist.add_song(self)

    def save_to_json(self):
        try:
            with open(self.FILE_PATH, 'r') as f:
                existing_data = json.load(f)
            existing_data.append({
                "title": self.title,
                "genre": self.genre,
                "artist": self.artist.name
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
        songs = []
        for song_info in data:
            artist = Artist.find_by_name(song_info["artist"])
            if artist:
                songs.append(cls(
                    title=song_info["title"],
                    genre=song_info["genre"],
                    artist=artist
                ))
        return songs

    @classmethod
    def find_by_title(cls, title):
        for song in cls.all:
            if song.title.lower() == title.lower():
                return song
        return None

    @classmethod
    def find_by_genre(cls, genre):
        return [s for s in cls.all if s.genre.lower() == genre.lower()]

    @classmethod
    def find_by_artist(cls, artist_name):
        return [s for s in cls.all if s.artist.name.lower() == artist_name.lower()]

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

    def __repr__(self):
        return f"Song('{self.title}' by {self.artist.name})"
