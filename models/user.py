from models.person import Person

class User(Person):
    #store all users
    all_users = []
    
    def __init__(self,name,email):
        super().__init__(name,email)
        self._favorite_songs = []
        self._favorite_albums = []
        User.all_users.append(self)




