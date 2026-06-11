"""Person class for representing individuals in the music library.
This class can represent artists or users.
"""


class Person:
    """Base class to represent a person with name and email and an auto-incrementing id."""

    _id_counter = 0

    def __init__(self, name: str, email: str):
        Person._id_counter += 1
        self._id = Person._id_counter
        self.name = name
        self.email = email

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    # setters -- validate data before setting it
    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Invalid email address.")
        self._email = value.strip()

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "email": self.email}

    def __str__(self) -> str:
        return f"Person(id={self.id}, name='{self.name}', email='{self.email}')"

    def __repr__(self) -> str:
        return self.__str__()