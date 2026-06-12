from models.person import Person

class User(Person):
    #store all users
    all_users = []

    def __init__(self,name,email):
        super().__init__(name,email)
        self._favorite_songs = []
        self._favorite_albums = []
        User.all_users.append(self)

     #add favorite songs
    def add_favorite_song(self,song):
        if song in self._favorite_songs:
            print(f"{song.title} is already in {self.name}'s favorite songs.")
            return #terminate code
        self._favorite_songs.append(song)
        print(f"{song.title} added to {self.name}'s favorite songs.")    




