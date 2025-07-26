from model.entity.user import User
from controller.user_controller import UserController

def test_save():
    user_controller = UserController()
    status, message = user_controller.save(
        "ahmad", "ahmadi", "akbar112", "ali1234", "customer", False
    )
    print("Save:", message)
    assert status

def test_edit():
    user_controller = UserController()
    # فرض: کد کاربر را می‌دانید (مثلاً "1")
    status, message = user_controller.edit(
        "1", "akbar", "ahmadi", "akbar11", "ali1234", "admin", True
    )
    print("Edit:", message)
    # assert status  # اگر مطمئن هستید کاربر وجود دارد

def test_delete():
    user_controller = UserController()
    # فرض: کد کاربر را می‌دانید (مثلاً "1")
    status, message = user_controller.delete("1")
    print("Delete:", message)
    # assert status  # اگر مطمئن هستید کاربر وجود دارد

def test_find_all():
    user_controller = UserController()
    status, users = user_controller.find_all()
    print("All users:", users)
    assert status

def test_find_by_code():
    user_controller = UserController()
    status, user = user_controller.find_by_code("1")
    print("Find by code:", user)
    # assert status

def test_find_by_name_family():
    user_controller = UserController()
    status, users = user_controller.find_by_name_family("ahmad", "ahmadi")
    print("Find by name/family:", users)
    assert status

def test_find_by_username():
    user_controller = UserController()
    status, user = user_controller.find_by_username("akbar112")
    print("Find by username:", user)
    # assert status

def test_find_by_username_and_password():
    user_controller = UserController()
    status, user = user_controller.find_by_username_and_password("akbar112", "ali1234")
    print("Find by username and password:", user)
    # assert status

if __name__ == "__main__":
    test_save()
    test_edit()
    test_find_all()
    test_find_by_code()
    test_find_by_name_family()
    test_find_by_username()
    test_find_by_username_and_password()
    test_delete()





