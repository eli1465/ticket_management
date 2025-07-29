from model.entity.user import User
from model.repository import file_manager
from model.tools.validation import *

class UserController:
    def save(self, user_id, name, family, birth_date, username, password, role,locked):
        try:
            user_id_validator(user_id)
            name_validator(name)
            family_validator(family)
            birth_date_validator(birth_date)
            username_validator(username)
            password_validator(password)
            role_validator(role)
            bool_validator(locked)

            user = User(user_id, name, family, birth_date, username, password, role, locked)

            user_list = file_manager.read_users()
            for u in user_list:
                if u.user_id == user.user_id:
                    return False, "User ID already exists."

            user_list.append(user)
            file_manager.write_users(user_list)
            return True, "User saved successfully."

        except Exception as e:
            return False, str(e)

    def edit(self, user_id, name, family, birth_date, username, password, role,locked):
        try:
            user_id_validator(user_id)
            name_validator(name)
            family_validator(family)
            birth_date_validator(birth_date)
            username_validator(username)
            password_validator(password)
            role_validator(role)
            bool_validator(locked)

            user_list = file_manager.read_users()
            for i in range(len(user_list)):
                if user_list[i].user_id == user_id:
                    user_list[i] = User(user_id, name, family, birth_date, username, password, role, locked)
                    file_manager.write_users(user_list)
                    return True, "User updated successfully."

            return False, "User not found."

        except Exception as e:
            return False, str(e)

    def delete(self, user_id):
        try:
            user_id_validator(user_id)
            user_list = file_manager.read_users()
            for u in user_list:
                if u.user_id == user_id:
                    user_list.remove(u)
                    file_manager.write_users(user_list)
                    return True, "User deleted successfully."
            return False, "User not found."
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            user_list = file_manager.read_users()
            return True, user_list
        except Exception as e:
            return False, str(e)

    def find_by_name_family(self, name, family):
        try:
            user_list = file_manager.read_users()
            result = [u for u in user_list if name.lower() in u.name.lower() and family.lower() in u.family.lower()]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_username(self, username):
        try:
            user_list = file_manager.read_users()
            result = [u for u in user_list if username.lower() in u.username.lower()]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_role(self, role):
        try:
            role_validator(role)
            user_list = file_manager.read_users()
            result = [u for u in user_list if u.role == str(role).lower()]
            return True, result
        except Exception as e:
            return False, str(e)