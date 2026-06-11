"""
artist inherits from person
artist -> albums
"""
from typing import List

from models.person import Person

class Artist(Person):
    """
    an artist is a person who creates music. inherits name and email from person.
    an artist can have multiple albums.
    adds genre,country, formed_year, and album list
    """
    _artist_registry: List['Artist'] = []
    def __init__(self, name: str, email: str, genre: str, country: str, formed_year: int):
        super().__init__(name, email)
        self._genre = genre
        self._country = country
        self._formed_year = formed_year    
        self._albums: List[str] = []
    
    # properties
    @property
    def genre(self) -> str:
        return self._genre
    
    @property
    def country(self) -> str:
        return self._country 

    @property
    def formed_year(self) -> int:
        return self._formed_year

    @property
    def albums(self) -> List[str]:
        return self._albums 

    def add_album(self, album: str) -> None:
        self._albums.append(album)

    def get_album_by_name(self, name: str) -> str:
        for album in self._albums:
            if album.name.lower() == name.lower():
                return album
        return None

    def total_songs(self) -> int:
        return sum(
            len(album.songs) for album in self._albums
        )
    def total_plays(self) -> int:
        return sum(
            song.play_count
            for album in self._albums
            for song in album.songs
        )
    #.setters
    @genre.setter
    def genre(self, value: str):
        self._genre = value.strip()

    @classmethod
    


    