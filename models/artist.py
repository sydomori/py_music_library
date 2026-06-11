class artist:
    def __init__(self,name, genre, artist_id):
        self.name =name
        self.genre =genre
        self.artist_id =artist_id
        self.songs =[]
        self.albums =[]

    def add_song(self, song):
          
       