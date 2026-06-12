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


    #display
    def get_discography(self):
        print(f"\n{self.name}'s Discography:")
        print("Songs:")
        if self._songs:
            for song in self._songs:
                print(f"- {song.title} from album {song.album.title}")
        else:
            print("No songs added.")
        print("\nAlbums:")
        if self._albums:
            for album in self._albums:
                print(f"- {album.title} ({album.release_year})")
        else:
            print("No albums added.")


    @classmethod
    def find_by_genre(cls,name):
        return [artist for artist in cls.artists if artist.genre.lower() == name.lower()]
    

    @classmethod
    def find_by_name(cls,name):
        for artist in cls.artists:
            if artist.name.lower() == name.lower():
                return artist
        return None
     
    #data
    def to_dict(self):      
        return {
            "name": self._name,
            "genre": self._genre,
        }
    


           
        

     
    

    

     




    