from model.entity.user import User
from model.repository.file_manager import *
from model.repository.file_manager import read_users
from model.tools.validation import *
from model.repository.user_repository import UserRepository


user_list = read_users()


class UserController:
    def save(self, name, family, username, password, role, locked):
        try:
            user = User(None, name, family, username, password, role, locked)
            user_repo = UserRepository()
            user_repo.save(user)
            return True, f"User saved {user}"
        except Exception as e:
            return False,f"Error saving user {e}"

    def edit(self, code, name, family, username, password, role, locked):
        try:
            user = User(code, name, family, username, password, role, locked)
            user_repo = UserRepository()
            user_repo.edit(user)
            return True, f"User edited {user}"
        except Exception as e:
            return False,f"Error editing user {e}"

    def delete(self, code):
        try:
            user_repo = UserRepository()
            user_repo.delete(code)
            return True, f"User removed {code}"
        except Exception as e:
            return False,f"Error removing user {e}"

    def find_all(self):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_all()
        except Exception as e:
            return False, f"Error find all users {e}"

    def find_by_code(self, code):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_code(code)
        except Exception as e:
            return False, f"Error find user code : {code} Error :{e}"

    def find_by_name_family(self, name, family):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_name_family(name, family)
        except Exception as e:
            return False, f"Error find users name : {name} - family {family} -- Error {e}"

    def find_by_username(self, username):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_username(username)
        except Exception as e:
            return False, f"Error find users username : {username}  -- Error {e}"

    def find_by_username_and_password(self, username, password):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_username_and_password(username, password)
        except Exception as e:
            return False, f"Error find users username:password : {username}:{password}  -- Error {e}"

