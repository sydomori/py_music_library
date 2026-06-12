from models.artist import Artist
class Song:
    def __init__(self, title, genre,artist, duration):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.duration = duration
        self.albums=[]#list to track albums this song is apart of.


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if not value:
            raise ValueError("Song title cannot be empty")
        self._title = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self,value):
        if not value:
            raise ValueError("Song genre cannot be empty")
        self._genre = value
     
    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self,value):
        if not isinstance(value,Artist):
            raise ValueError("Artist must be an instance of the Artist class")
        self._artist = value

    #classmethods
    @classmethod
    def find_by_title(cls,title):
        for song in cls.songs:
            if song.title == title:
                return song
        return None
    
    @classmethod
    def find_by_genre(cls,genre):
        return [song for song in cls.songs if song.genre.lower() == genre.lower()]
    
    @classmethod
    def find_by_artist(cls,artist_name):
        return [song for song in cls.songs if song.artist.name.lower() == artist_name.lower()]

#data
    def __str__(self):
        return f"{self.title} by {self.artist},in genre : {self.genre} duration:{self.duration } mins"
    
    def to_dict(self):
        return{

            "title":self.title,
            "genre":self.genre,
            "artist":self.artist,
            "duration":self.duration

        }
    def add_to_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
        if self not in album.songs:
            album.add_song(self)

    def __repr__(self):
        return f"Song: {self.title} by {self.artist}, in genre: {self.genre} ,duration:{self.duration }"