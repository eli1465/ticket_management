from model.tools.validation import *

class User:
    def __init__(self, code, name, family,username,password,role,locked=False):
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role
        self.locked = locked

    def full_name(self):
        return f"{self.name} {self.family}"

    def __repr__(self):
        return f"{self.__dict__}"

    #def to_tuple(self):
        #return (self.code, self.name, self.family, self.age,self.username,self.password,self.locked)

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

    # ----role------
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self,value):
        if not isinstance("Customer","Admin"):
            raise ValueError (" must be customer or admin")
    # ----- locked -----
    @property
    def locked(self):
        return self.locked

    @locked.setter
    def locked(self, value):
        if not isinstance(value, bool):
            raise ValueError("locked must be a boolean")
        self.locked = value

# todo : getter/setter ---> validation


