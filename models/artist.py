"""
models/artist.py
Artist class — inherits from Person.
One-to-many: Artist -> Albums
"""
from models.person import Person
class Artist(Person):
    """
    A music artist or band.
    Inherits name/email from Person.
    Adds genre, country, formed_year, and albums.
    """

    _artist_registry: list = []

    def __init__(self, name: str, email: str = "",
                 genre: str = "Unknown", country: str = "Unknown",
                 formed_year: int = 0):
        super().__init__(name, email)
        self._genre = genre
        self._country = country
        self._formed_year = formed_year
        self._albums: list = []

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str):
        self._genre = value.strip()

    @property
    def country(self) -> str:
        return self._country

    @property
    def formed_year(self) -> int:
        return self._formed_year

    @property
    def albums(self) -> list:
        return self._albums

    def add_album(self, album) -> None:
        self._albums.append(album)

    def get_album_by_title(self, title: str):
        for a in self._albums:
            if a.title.lower() == title.lower():
                return a
        return None

    def total_songs(self) -> int:
        return sum(len(a.songs) for a in self._albums)

    def total_plays(self) -> int:
        return sum(
            song.play_count
            for album in self._albums
            for song in album.songs
        )

    @classmethod
    def create(cls, name: str, email: str = "",
               genre: str = "Unknown", country: str = "Unknown",
               formed_year: int = 0) -> "Artist":
        artist = cls(name, email, genre, country, formed_year)
        cls._artist_registry.append(artist)
        return artist

    @classmethod
    def all(cls) -> list:
        return cls._artist_registry

    @classmethod
    def find_by_name(cls, name: str):
        for a in cls._artist_registry:
            if a.name.lower() == name.lower():
                return a
        return None

    @classmethod
    def find_by_genre(cls, genre: str) -> list:
        return [a for a in cls._artist_registry
                if a.genre.lower() == genre.lower()]

    @classmethod
    def clear_registry(cls) -> None:
        cls._artist_registry.clear()
        Person._id_counter = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "genre": self._genre,
            "country": self._country,
            "formed_year": self._formed_year,
            "albums": [a.to_dict() for a in self._albums],
        })
        return base

    @classmethod
    def from_dict(cls, data: dict) -> "Artist":
        from models.albums import Album
        artist = cls.__new__(cls)
        Person.__init__(artist, data["name"], data.get("email", ""))
        artist._id = data["id"]
        artist._genre = data.get("genre", "Unknown")
        artist._country = data.get("country", "Unknown")
        artist._formed_year = data.get("formed_year", 0)
        artist._albums = [Album.from_dict(a, artist=artist)
                          for a in data.get("albums", [])]
        return artist

    def __str__(self) -> str:
        return (
            f"Artist #{self._id} | {self._name} | "
            f"{self._genre} | {self._country} | Albums: {len(self._albums)}"
        )

    def __repr__(self) -> str:
        return f"Artist(id={self._id}, name={self._name!r})"