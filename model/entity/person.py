from model.tools.validation import *

class Person:
    def __init__(self, code, name, family, age):
        self.code = code
        self.name = name
        self.family = family
        self.age = age

    def full_name(self):
        return f"{self.name} {self.family}"

    def __repr__(self):
        return f"{self.full_name()} ({self.age}) years old"

    def to_tuple(self):
        return (self.code, self.name, self.family, self.age)

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