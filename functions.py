def create_artist():
    name = input("Enter artist name: ")
    genre = input("Enter genre: ")
    new_artist = Artist(name, genre)
    print(f"{new_artist} created successfully")

