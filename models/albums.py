class Album:
    def __init__(self, title, artist, release_year):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.songs = []#list to track songs in this album.

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            song.add_to_album(self)

    def list_songs(self):
        return [str(song) for song in self.songs]
    
    def to_dict(self):
        return{
            "title":self.title,
            "artist":self.artist,
            "release_year":self.release_year,
            "songs":[song.title for song in self.songs]
        }
    def __repr__(self):
        return f"Song: {self.title} by {self.artist},released in {self.release_year}"