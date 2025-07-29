from model.tools.validation import *

class User:
    def __init__(self, user_id, name, family, birth_date, username, password, locked, role):
        self.user_id = user_id
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.username = username
        self.password = password
        self.locked = locked
        self.role = role

    def full_name(self):
        return f"{self.name} {self.family}"

    def __str__(self):
        return f"{self.user_id} - {self.username} - {self.role}"

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.family}, {self.username}, {self.role})"

    def to_tuple(self):
        return (self.user_id, self.name, self.family, self.birth_date,
                self.username, self.password, self.locked, self.role)

    # ---------- user_id ----------
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        user_id_validator(value)
        self._user_id = value

    # ---------- name ----------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    # ---------- family ----------
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        family_validator(value)
        self._family = value

    # ---------- birth_date ----------
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        birth_date_validator(value)
        self._birth_date = value

    # ---------- username ----------
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        username_validator(value)
        self._username = value

    # ---------- password ----------
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        password_validator(value)
        self._password = value

    # ---------- is_locked ----------
    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        bool_validator(value)
        self._locked = value

    # ---------- role ----------
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        role_validator(value)
        self._role = value.lower()