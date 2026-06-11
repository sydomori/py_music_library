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

    def get_discography(self):
        print(f" {self.name} — Discography")
        print(f"  Genre: {self.genre}")
        if self.albums:
            print(f"  Albums ({len(self.albums)}):")
            for album in self.albums:
                print(f"    • {album.title} ({album.release_year})")
        if self.songs:
            print(f"  Songs ({len(self.songs)}):")
            for song in self.songs:
                print(f"    • {song.title}")
        if not self.albums and not self.songs:
            print("  No songs or albums added yet.")

    def         


                
   