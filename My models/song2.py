import json
from my_models.artist2 import Artist

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