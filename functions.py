def create_artist():
    name = input("Enter artist name: ")
    genre = input("Enter genre: ")
    new_artist = Artist(name, genre)
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