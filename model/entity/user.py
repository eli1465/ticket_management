from model.tools.validation import *

class User:
    def __init__(self, code, name, family, username, password, role, locked=False):
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
        return f"User({self.code}, {self.name}, {self.family}, {self.username}, {self.password}, {self.role}, {self.locked})"

    def to_tuple(self):
        return (self.code, self.name, self.family, self.username, self.password, self.role, self.locked)

    # -------- code --------
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        code_validator(value)
        self._code = value

    # -------- name --------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    # ----- family -----
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
        username_validator(value)
        self._username = value

    # ----- password -----
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        password_validator(value)
        self._password = value

    # ---- role ----
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        role_validator(value)
        self._role = str(value).lower()  # ذخیره به صورت lowercase برای یکپارچگی

    # ----- locked -----
    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        if not isinstance(value, bool):
            raise ValueError("locked must be a boolean")
        self._locked = value