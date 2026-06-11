"""
user class- inherits from person.
user can have playlists and favorite songs.
"""
from typing import List

from models import person
from models.person import Person

class User(Person):
    """
    a listener of music inherits name and email from person.
    listener can have playlists and favorite songs.
    """
    _user_registry: List['User'] = []

    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self._playlists: List[str]= []
        self._favorite_songs: List[str] = []
        self._favourite_albums: List[str] = []
        User._user_registry.append(self)

    # properties
    @property
    def playlists(self) -> List[str]:
        return self._playlists

    @property
    def favorite_songs(self) -> List[str]:
        return self._favorite_songs

    @property
    def favourite_albums(self) -> List[str]:
        return self._favourite_albums
    
    # methods to add/remove playlists and favorite songs
    def add_playlist(self, playlist: str) -> None:
        self._playlists.append(playlist)
        
    def get_playlist_by_name(self, name: str) -> str:
        for playlist in self._playlists:
            if playlist.name.lower() == name.lower():
                return playlist
        return None

    # method to add a song to favorites
    def add_favorite(self, song: str) -> None:
        if song not in self._favorite_songs:
            self._favorite_songs.append(song)

    def remove_favorite(self, song: str) -> bool:
        if song in self._favorite_songs:
            self._favorite_songs.remove(song)
            return True
        return False
    
    #class method to get all users
    @classmethod
    def create(cls, name: str, email: str) -> 'User':
        user=cls(name, email)
        cls._user_registry.append(user)
        return user
    
    @classmethod
    def all(cls) -> List['User']:
        return cls._user_registry
    
    @classmethod
    def find_by_name(cls, name: str):
        for user in cls._user_registry:
            if user.name.lower() == name.lower():
                return user
        return None
    
    @classmethod
    def clear_registry(cls) -> None:
        cls._user_registry.clear()
        person._id_counter = 0  # reset id counter for testing purposes
        
        #serialize user to dict
    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "playlists": [playlist.to_dict() for playlist in self._playlists],
            "favourite_song_ids": [song.id for song in self._favorite_songs],
            "favourite_album_ids": [album.id for album in self._favourite_albums]
        })
        return base
    
    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        user = cls.__new__(cls)  # create an uninitialized instance
        person.__init__(user, data['name'], data.get('email'))  # initialize person attributes
        user.id = data['id']  # set the id directly
        user._playlists = [Playlist.from_dict(pl, owner=user) for pl in data.get('playlists', [])]
        # For favorites, we will just store the IDs for now. The actual song/album objects will need to be linked after all data is loaded.
        user._favorite_songs = []
        user._favourite_albums = []
        user._favour_song_ids = data.get('favourite_song_ids', [])
        user._favour_album_ids = data.get('favourite_album_ids', [])
        return user
    
    def __str__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', playlists={len(self._playlists)}, favorite_songs={len(self._favorite_songs)}, favorite_albums={len(self._favourite_albums)})"

    def __repr__(self) -> str:
        return f"User(id={self.id}), name={self.name}!r)"
    

