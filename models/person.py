class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

  
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,value):
        if not "@" in value:
            raise ValueError("Invalid email address")
        self._email = value

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"
        
    



    