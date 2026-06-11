class user():
    """
    Extends Person. Represents a library user.
    - has many FavoriteSongs (via FavoriteSong junction)
    - has many FavoriteAlbums (via FavoriteAlbum junction)
    """

    def __init__(self, name, email, user_id):
        super().__init__(name, email)
        self.user_id = user_id
        self.favorite_songs = []    # list of FavoriteSong objects
        self.favorite_albums = []   # list of FavoriteAlbum objects

    def add_favorite_song(self, song, _quiet=False):
        # Prevent duplicates
        already = any(fs.song.song_id == song.song_id for fs in self.favorite_songs)
        if already:
            if not _quiet:
                print(f'  "{song.title}" is already in your favorites.')
            return
        entry = FavoriteSong(user=self, song=song)
        self.favorite_songs.append(entry)
        if not _quiet:
            print(f'   Added "{song.title}" to {self.name}\'s favorite songs.')

    def add_favorite_album(self, album, _quiet=False):
        already = any(fa.album.album_id == album.album_id for fa in self.favorite_albums)
        if already:
            if not _quiet:
                print(f'  "{album.title}" is already in your favorites.')
            return
        entry = FavoriteAlbum(user=self, album=album)
        self.favorite_albums.append(entry)
        if not _quiet:
            print(f'   Added "{album.title}" to {self.name}\'s favorite albums.')

    def view_favorites(self):
        print(f" Favorites for {self.name}")
        if self.favorite_songs:
            print(f"  Favorite Songs ({len(self.favorite_songs)}):")
            for fs in self.favorite_songs:
                print(f"    • {fs.song} (added {fs.date_added})")
        else:
            print("  No favorite songs yet.")

        if self.favorite_albums:
            print(f"  Favorite Albums ({len(self.favorite_albums)}):")
            for fa in self.favorite_albums:
                print(f"    • {fa.album} (added {fa.date_added})")
        else:
            print("  No favorite albums yet.")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "favorite_song_ids": [fs.song.song_id for fs in self.favorite_songs],
            "favorite_album_ids": [fa.album.album_id for fa in self.favorite_albums],
        }

    def __str__(self):
        return f"User: {self.name} | {self.email} (ID: {self.user_id})"