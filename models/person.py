class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name
    