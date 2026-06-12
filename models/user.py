from models.person import Person

class User(Person):
    #store all users
    all_users = []

    def __init__(self,name,email):
        super().__init__(name,email)
        self._favorite_songs = []
        self._favorite_albums = []
        User.all_users.append(self)

    # add favorite songs
    def add_favorite_song(self, song):
        if song in self._favorite_songs:
            print(f"{song.title} is already in {self.name}'s favorite songs.")
            return
        self._favorite_songs.append(song)
        print(f"{song.title} added to {self.name}'s favorite songs.")

    # remove favorite songs
    def remove_favorite_song(self, song):
        if song not in self._favorite_songs:
            print(f"{song.title} is not in {self.name}'s favorite songs.")
            return
        self._favorite_songs.remove(song)
        print(f"{song.title} removed from {self.name}'s favorite songs.")


    @property
    def favorite_songs(self):
        return self._favorite_songs
    
#add favorite albums
    def add_favorite_album(self,album):
        if album in self._favorite_albums:
            print(f"{album.title} is already in {self.name}'s favorite albums.")
            return
        self._favorite_albums.append(album)
        print(f"{album.title} added to {self.name}'s favorite albums.")

       







