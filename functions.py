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