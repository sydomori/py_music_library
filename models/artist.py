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
    