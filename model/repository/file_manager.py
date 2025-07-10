import pickle
import os

# فایل‌ها
person_file= "person.dat"
ticket_file= "ticket.dat"

def file_exists(file_name):
    return os.path.exists(file_name)

#  Person

def read_persons():
    if file_exists(person_file):
        try:
            with open(person_file, "rb") as file:
                return pickle.load(file)
        except:
            print(f"Error reading persons file")
            return []
    return []

def write_persons(person_list):
    try:
        with open(person_file, "wb") as file:
            pickle.dump(person_list, file)
    except:
        print(f"Error writing persons file")

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