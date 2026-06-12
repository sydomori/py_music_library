from models.artists import Artists
class Album:
    albums=[]
    def __init__(self, title, artist,genre, release_year):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        Album.albums.append(self)
        artist.add_album(self)
        self._songs = []
       
    @property
    def title(self):
        return self._title
    
    @title.setter 
    def title (self,value):
        if not value:
            raise ValueError("Album title cannot be empty")
        self._title = value

    @artist.setter
    def artist(self,value):
        if not isinstance(value,Artist):
            raise ValueError("Artist must be an instance of the Artist class")
        self._artist = value

    @property
    def release_year(self):
        return self._release_year
    
    @release_year.setter
    def release_year(self,value):
         if not isinstance(value,int) or value<1900:
             raise ValueError("Release year not valid!")
         self._release_year =value

    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self.value):
        if not value:
            raise ValueError("Album genre cannot be empty")
        self._genre =value
         

    
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            song.add_to_album(self)
            print(f"{song.title} added to {self.title} album")
        else:
            print(f"{song.title} is already in {self.title} album.")

    def remove_song(self,song):
        if song in self._songs:
            self._songs.remove(song)
            print(f"{song.title} removed from {self.title} album")


    def list_songs(self):
        return [str(song) for song in self.songs]
    
    def to_dict(self):
        return{
            "title":self.title,
            "artist":self.artist,
            "genre":self.genre,
            "release_year":self.release_year,
            "songs":[song.title for song in self.songs]
        }
    def __repr__(self):
        return f"Album: {self.title} by {self.artist}, in genre: {self.genre} released in {self.release_year}"
    
    def __str__(self):
        return f"{self._title} by {self._artist.name} ({self._release_year})"
    
    #classmethods
    @classmethod
    def find_by_title(cls,title):
        for album in cls.albums:
            if album.title.lower() == title.lower():
                return album
        return None
    
    @classmethod
    def find_by_artist(cls,artist_name):
        return [album for album in cls.albums if album.artist.name.lower() == artist_name.lower()]
    