"""
user class- inherits from person.
user can have playlists and favorite songs.
"""
from typing import List

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

