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

    @property
    def favorite_songs(self):
        return self._favorite_songs

    def add_favorite_album(self, album):
        if album in self._favorite_albums:
            print(f"'{album.title}' is already in your favorites")
            return
        self._favorite_albums.append(album)
        print(f"Added '{album.title}' to favorites")

    def remove_favorite_album(self, album):
        if album not in self._favorite_albums:
            print(f"'{album.title}' is not in your favorites")
            return
        self._favorite_albums.remove(album)
        print(f"Removed '{album.title}' from favorites")

    @property
    def favorite_albums(self):
        return self._favorite_albums

    def view_favorites(self):
        print(f"\n{self.name}'s Favorite Songs:")
        if self._favorite_songs:
            for song in self._favorite_songs:
                print(f"  - {song.title} by {song.artist}")
        else:
            print("  No favorite songs added.")
        print(f"\n{self.name}'s Favorite Albums:")
        if self._favorite_albums:
            for album in self._favorite_albums:
                print(f"  - {album.title} by {album.artist}")
        else:
            print("  No favorite albums added.")

    def save_to_json(self):
        try:
            with open(self.FILE_PATH, 'r') as f:
                existing_data = json.load(f)
            existing_data.append({
                "name": self.name,
                "email": self.email,
                "favorite_songs": [s.title for s in self._favorite_songs],
                "favorite_albums": [a.title for a in self._favorite_albums]
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
        users = []
        for user_info in data:
            user = cls(
                name=user_info["name"],
                email=user_info["email"]
            )
            for song_title in user_info.get("favorite_songs", []):
                song = Song.find_by_title(song_title)
                if song:
                    user.add_favorite_song(song)
            for album_title in user_info.get("favorite_albums", []):
                album = Album.find_by_title(album_title)
                if album:
                    user.add_favorite_album(album)
            users.append(user)
        return users

    @classmethod
    def find_by_name(cls, name):
        for user in cls.all:
            if user.name.lower() == name.lower():
                return user
        return None

    def __str__(self):
        return f"User: {self.name} | Email: {self.email}"

    def __repr__(self):
        return f"User('{self.name}', Email'{self.email}')"