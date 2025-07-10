from model.tools.validation import *

class Person:
    def __init__(self, code, name, family, age,username,password,is_locked=True):
        self.code = code
        self.name = name
        self.family = family
        self.age = age
        self.username = username
        self.password = password
        self.is_locked=True

    def full_name(self):
        return f"{self.name} {self.family}"

    def __repr__(self):
        return f"{self.full_name()} ({self.age}) years old"

    def to_tuple(self):
        return (self.code, self.name, self.family, self.age,self.username,self.password,self.is_locked)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        family_validator(value)
        self._family = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        age_validator(value)
        self._age = value

        # ----- username -----

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Invalid username")
        self._username = value

    # ----- password -----
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 6:
            raise ValueError("Invalid password")
        self._password = value

    # ----- is_locked -----
    @property
    def is_locked(self):
        return self._is_locked

    @is_locked.setter
    def is_locked(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_locked must be a boolean")
        self._is_locked = value
