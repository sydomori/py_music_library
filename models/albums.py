class Album:
    def __init__(self, title, artist,genre, release_year):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.release_year = release_year
        self.songs = []#list to track songs in this album.

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            if self not in song.albums:
                song.add_to_album(self)

    def list_songs(self):
        return [str(song) for song in self.songs]
    
    def to_dict(self):
        return{
            "title":self.title,
            "artist":self.artist,
            "genre":self.genre,
            "release_year":self.release_year,
            "songs":[song.title for song in self.songs]
        }
    def __repr__(self):
        return f"Album: {self.title} by {self.artist}, in genre: {self.genre} released in {self.release_year}"