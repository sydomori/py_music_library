class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.albums=[]#list to track albums this song is apart of.

    def __str__(self):
        return f"{self.title} by {self.artist},duration:{self.duration } mins"
    
    def to_dict(self):
        return{

            "title":self.title,
            "artist":self.artist,
            "duration":self.duration

        }
    def add_to_album(self,album):
        if album not in self.albums:
            self.albums.append(album)
            album.add_song(self)