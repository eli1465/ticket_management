import pickle
import os

# فایل‌ها
user_file = "user.pkl"
ticket_file = "ticket.pkl"

def file_exists(file_name):
    return os.path.exists(file_name)

# User
def read_users():
    if file_exists(user_file):
        try:
            with open(user_file, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error reading user file: {e}")
            return []
    return []

def write_users(user_list):
    try:
        with open(user_file, "wb") as file:
            pickle.dump(user_list, file)
    except Exception as e:
        print(f"Error writing user file: {e}")

# Ticket
def read_tickets():
    if file_exists(ticket_file):
        try:
            with open(ticket_file, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error reading ticket file: {e}")
            return []
    return []

def write_tickets(ticket_list):
    try:
        with open(ticket_file, "wb") as file:
            pickle.dump(ticket_list, file)
    except Exception as e:
        print(f"Error writing ticket file: {e}")