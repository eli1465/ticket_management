from controller.user_controller import UserController

user_controller = UserController()

# Test Save
status, message = user_controller.save(1, "John", "Doe", "1990-01-01", "john123", "pass123", "admin", False)
if status:
    print("Save:", message)
else:
    print("Save Error:", message)

# Test Edit
status, message = user_controller.edit(1, "John", "Smith", "1990-01-01", "john123", "pass456", "admin", False)
if status:
    print("Edit:", message)
else:
    print("Edit Error:", message)

#  Test Find All
status, users = user_controller.find_all()
if status:
    print("Find All:")
    for u in users:
        print(u)
else:
    print("Find All Error:", users)

# ---------- Test Find by Name and Family ----------
status, users = user_controller.find_by_name_family("John", "Smith")
if status:
    print("Find by Name and Family:")
    for u in users:
        print(u)
else:
    print("Find by Name and Family Error:", users)

# ---------- Test Find by Username ----------
status, users = user_controller.find_by_username("john")
if status:
    print("Find by Username:")
    for u in users:
        print(u)
else:
    print("Find by Username Error:", users)

# ---------- Test Find by Role ----------
status, users = user_controller.find_by_role("admin")
if status:
    print("Find by Role:")
    for u in users:
        print(u)
else:
    print("Find by Role Error:", users)

# ---------- Test Delete ----------
status, message = user_controller.delete(1)
if status:
    print("Delete:", message)
else:
    print("Delete Error:", message)