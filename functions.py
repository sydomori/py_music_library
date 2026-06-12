from My_models.artist2 import Artist
from My_models.song2 import Song
from My_models.album2 import Album
from My_models.user2 import User

def create_artist():
    name = input("Enter artist name: ")
    genre = input("Enter genre: ")
    new_artist = Artist(name, genre)
    new_artist.save_to_json()
    print(f"{new_artist} created successfully")

def list_all_artists():
    artists = Artist.read_all()
    if artists:
        for artist in artists:
            print(artist)
    else:
        print("No artists found")

def create_song():
    title = input("Enter song title: ")
    genre = input("Enter genre: ")
    artist_name = input("Enter artist name: ")
    artist = Artist.find_by_name(artist_name)
    if artist:
        new_song = Song(title, genre, artist)
        new_song.save_to_json()
        print(f"{new_song} created successfully")
    else:
        print("Artist '{artist_name}' not found")

def list_all_songs():
    songs = Song.read_all()
    if songs:
        for song in songs:
            print(song)
    else:
        print("No songs found")

def create_album():
    title = input("Enter album title: ")
    genre = input("Enter genre: ")
    release_year = int(input("Enter release year: "))
    artist_name = input("Enter artist name: ")
    artist = Artist.find_by_name(artist_name)
    if artist:
        new_album = Album(title, genre, artist)
        new_album.save_to_json()
        print(f"{new_album} created successfully")
    else:
        print("Artist '{artist_name}' not found")

def list_all_albums():
    albums = Album.read_all()
    if albums:
        for album in albums:
            print(album)
    else:
        print("No albums found")

def create_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    new_user = User(name, email)
    new_user.save_to_json()
    print(f'{new_user} created successfully')

def list_all_users():
    users = User.read_all()
    if users:
        for user in users:
            print(user)
    else:
        print("No users found")

def add_favorite_song():
    user_name = input("Enter user name: ")
    song_title = input("Enter song title: ")
    user = User.find_by_name(user_name)
    song = Song.find_by_title(song_title)
    if user and song:
        user.add_favorite_song(song)
        user.save_to_json()
    elif not user:
       print(f"User '{user_name}' not found")
    elif not song:
       print(f"Song '{song_title}' not found")

def add_favorite_album():
    user_name = input("Enter user name: ")
    album_title = input("Enter album title: ")
    user = User.find_by_name(user_name)
    album = Album.find_by_title(album_title)
    if user and album:
        user.add_favorite_album(album)
        user.save_to_json()
    elif not user:
       print(f"User '{user_name}' not found")
    elif not album:
       print(f"Album '{album_title}' not found")

def search_by_artist():
    artist_name = input("Enter artist name: ")
    songs = Song.find_by_artist(artist_name)
    albums = Album.find_by_artist(artist_name)
    if songs:
        print(f"\nSongs by {artist_name}:")
        for song in songs:
            print(song)
    else:
        print(f"No songs found for '{artist_name}'")
    if albums:
        print(f"\nAlbums by {artist_name}:")
        for album in albums:
            print(album)
    else:
        print(f"No albums found for '{artist_name}'")

def search_by_genre():
    genre = input("Enter genre: ")
    songs = Song.find_by_genre(genre)
    albums = Album.find_by_genre(genre)
    if songs:
        print(f"\nSongs with genre '{genre}':")
        for song in songs:
            print(song)
    else:
        print(f"No songs found with genre '{genre}'")
    if albums:
        print(f"\nAlbums with genre '{genre}':")
        for album in albums:
            print(album)
    else:
        print(f"No albums found with genre '{genre}'")

def view_favorites():
    user_name = input("Enter user name: ")
    user = User.find_by_name(user_name)
    if user:
        user.view_favorites()
    else:
        print(f"User '{user_name}' not found")