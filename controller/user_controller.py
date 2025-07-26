from model.entity.user import User
from model.repository.file_manager import read_users, write_users
from model.tools.validation import *


class UserController:
    def save(self, name, family, username, password, role, locked):
        try:
            # اعتبارسنجی ورودی‌ها (در صورت نیاز)
            user_list = read_users()
            # تولید یک کد یکتا برای کاربر (مثلاً با استفاده از طول لیست یا uuid)
            code = str(len(user_list) + 1)
            user = User(code, name, family, username, password, role, locked)
            user_list.append(user)
            write_users(user_list)
            return True, f"User saved: {user}"
        except Exception as e:
            return False, f"Error saving user: {e}"

    def edit(self, code, name, family, username, password, role, locked):
        try:
            user_list = read_users()
            for index, u in enumerate(user_list):
                if u.user_code == code:
                    user_list[index] = User(code, name, family, username, password, role, locked)
                    write_users(user_list)
                    return True, f"User edited: {user_list[index]}"
            return False, "User not found"
        except Exception as e:
            return False, f"Error editing user: {e}"

    def delete(self, code):
        try:
            user_list = read_users()
            for u in user_list:
                if u.user_code == code:
                    user_list.remove(u)
                    write_users(user_list)
                    return True, f"User removed: {code}"
            return False, "User not found"
        except Exception as e:
            return False, f"Error removing user: {e}"

    def find_all(self):
        try:
            user_list = read_users()
            return True, user_list
        except Exception as e:
            return False, f"Error finding all users: {e}"

    def find_by_code(self, code):
        try:
            user_list = read_users()
            for u in user_list:
                if u.user_code == code:
                    return True, u
            return False, "User not found"
        except Exception as e:
            return False, f"Error finding user by code: {e}"

    def find_by_name_family(self, name, family):
        try:
            user_list = read_users()
            result = [u for u in user_list if u.name == name and u.family == family]
            return True, result
        except Exception as e:
            return False, f"Error finding users by name and family: {e}"

    def find_by_username(self, username):
        try:
            user_list = read_users()
            for u in user_list:
                if u.username == username:
                    return True, u
            return False, "User not found"
        except Exception as e:
            return False, f"Error finding user by username: {e}"

    def find_by_username_and_password(self, username, password):
        try:
            user_list = read_users()
            for u in user_list:
                if u.username == username and u.password == password:
                    return True, u
            return False, "User not found"
        except Exception as e:
            return False, f"Error finding user by username and password: {e}"

