from model.entity.user import User
from controller.user_controller import UserController

print("<<< User Class Manual Test >>>")

user = User(1, "Ali", "Ahmadi", "2000-01-01", "ali123", "pass123", "admin", False)
print("Full Name:", user.full_name())
print("String:", user)
print("Tuple:", user.to_tuple())

print("\n<<< UserController Manual Test >>>")
user_controller = UserController()

# Save
status, message = user_controller.save(1, "Ali", "Ahmadi", "2000-01-01", "ali123", "pass123", "admin", False)
if status:
    print("User saved:", message)
else:
    print("Save failed:", message)

# Edit
status, message = user_controller.edit(1, "Ali", "Ahmadi", "2000-01-01", "ali123", "newpass", "admin", False)
if status:
    print("User edited:", message)
else:
    print("Edit failed:", message)

# Find by username
status, users = user_controller.find_by_username("ali")
if status:
    print("Users found by username:", len(users))
else:
    print("Find by username failed:", users)

# Find by role
status, users = user_controller.find_by_role("admin")
if status:
    print("Users found by role:", len(users))
else:
    print("Find by role failed:", users)

# Find by name and family
status, users = user_controller.find_by_name_family("Ali", "Ahmadi")
if status:
    print("Users found by name/family:", len(users))
else:
    print("Find by name/family failed:", users)

# Find all
status, users = user_controller.find_all()
if status:
    print("All users:", len(users))
else:
    print("Find all failed:", users)

# Delete
status, message = user_controller.delete(1)
if status:
    print("User deleted:", message)
else:
    print("Delete failed:", message)