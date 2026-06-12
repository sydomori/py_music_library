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




    