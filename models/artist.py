class artist:
    def __init__(self,name, genre):
        self.name =name
        self.genre =genre
        Artist.artists.append(self)
        self.songs =[]
        self.albums =[]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
     if not value:
        raise ValueError("Name cannot be empty")
     
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self,value):
        if not value:
            raise ValueError("Genre cannot be empty")
        self._genre = value

    @property
    def songs(self):
        return self._songs
     
    @property
    def albums(self):
        return self._albums
    
    def add_song(self,song):
        if song not in self._songs:
            self._songs.append(song)
        else:
            print(f"{song.title} is already in {self.name}'s songs.")

    def add_album(self,album):
        if album not in self._albums:
            self._albums.append(album)
        else:
            print(f"{album.title} is already in {self.name}'s albums.")

     
    

    

     




    