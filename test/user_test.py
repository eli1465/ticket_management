from model.entity.user import User


# user_1 = User(3, "mohsen" , "alipour", "ALI", "ali123", "employee", 1)
# print(user_1.to_tuple())
# user_1.address = "Tehran"
# user_1.name = "alireza"
#
# print(user_1)
from controller.user_controller import UserController
user_controller = UserController()

# user_repo = UserRepository()

# Test Passed
# user_repo.save(user_1)
status, message = user_controller.save("ahmad", "ahmadi", "akbar112", "ali123", "employee", 1)
print(message)

# Test Passed
# user_repo.edit(user_1)
# status, message = user_controller.edit(41, "akbar", "ahmadi", "akbar11", "ali123", "employee", 1)

# Test Passed
# user_repo.delete(1001)
# status, message = user_controller.delete(41)

# Test Passed
# print(user_repo.find_all())

# Test Passed
# print(user_repo.find_by_code(33))

# Test Passed
# print(user_repo.find_by_name_family("", "r"))

# Test Passed
# print(user_repo.find_by_username("ahmad"))

# Test Passed
# print(user_repo.find_by_username_and_password("ahmad", "ahmad123"))





