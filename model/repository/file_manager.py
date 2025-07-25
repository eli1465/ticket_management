import pickle
import os

# فایل‌ها
user_file= "user.dat"
ticket_file= "ticket.dat"

def file_exists(file_name):
    return os.path.exists(file_name)

#  Person

def read_users():
    if file_exists(user_file):
        try:
            with open(user_file, "rb") as file:
                return pickle.load(file)
        except:
            print(f"Error reading persons file")
            return []
    return []

def write_users(user_list):
    try:
        with open(user_file, "wb") as file:
            pickle.dump(user_list, file)
    except:
        print(f"Error writing user file")

# ticket
def read_tickets():
    if file_exists(ticket_file):
        try:
            with open(ticket_file, "rb") as file:
                return pickle.load(file)
        except:
            print(f"Error reading tickets file")
            return []
    return []

def write_tickets(ticket_list):
    try:
        with open(ticket_file, "wb") as file:
            pickle.dump(ticket_list, file)
    except:
        print(f"Error writing tickets file")