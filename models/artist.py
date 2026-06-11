class artist:
    def __init__(self,name, genre, artist_id):
        self.name =name
        self.genre =genre
        self.artist_id =artist_id
        self.songs =[]
        self.albums =[]

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)

    def get_discography(self)
                
   