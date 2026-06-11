from models.person import Person

class User(Person):
    def __init__(self, name, email, user_id):
        super().__init__(name, email)
        self._user_id = user_id
        self.favourite_songs = []
        self.favourite_albums = []

    def add_favourite_song(self, song, _quiet=False):
        

        