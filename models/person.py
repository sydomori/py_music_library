"""Person class for representing individuals in the music library.
This class can represent artists,users"""

class Person:
    _id_counter = 0
""" base class to represent person with name and email, and an auto-incrementing id. """
    def __init__(self, name: str, email: str):
        person._id_counter += 1
        self.id = person._id_counter
        self.name = name
        self.email = email 

