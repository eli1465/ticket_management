import re
#  User
def user_id_validator(user_id):
    if type(user_id) != int:
        raise ValueError("User ID must be an integer")
    if user_id <= 0:
        raise ValueError("User ID must be a positive number")

def name_validator(name):
    if type(name) != str:
        raise ValueError("Name must be a string")
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Name must be 3-30 characters, letters and spaces only")

def family_validator(family):
    if type(family) != str:
        raise ValueError("Family must be a string")
    if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
        raise ValueError("Family must be 3-30 characters, letters and spaces only")

def username_validator(username):
    if type(username) != str:
        raise ValueError("Username must be a string")
    if not re.match(r"^[a-zA-Z]\s{3,30}$", username):
        raise ValueError("Username must be 3-30 characters with no spaces")

def password_validator(password):
    if type(password) != str:
        raise ValueError("Password must be a string")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters")

def bool_validator(value):
    if type(value) != bool:
        raise ValueError("Value must be True or False")

def birth_date_validator(birth_date):
    if type(birth_date) != str:
        raise ValueError("Birth date must be a string")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", birth_date):
        raise ValueError("Birth date must be in YYYY-MM-DD format")

def role_validator(role):
    if str(role).lower() not in ['customer', 'admin']:
        raise ValueError("Invalid role. Must be 'customer' or 'admin'")
#ticket
def ticket_id_validator(ticket_id):
    if type(ticket_id) != int:
        raise ValueError("Ticket ID must be an integer")
    if ticket_id <= 0:
        raise ValueError("Ticket ID must be a positive number")

def ticket_code_validator(ticket_code):
    if type(ticket_code) != str:
        raise ValueError("Ticket code must be a string")
    if not re.match(r"^[a-zA-Z0-9\-]{3,20}$", ticket_code):
        raise ValueError("Ticket code must be 3-20 characters (letters, numbers, hyphen)")

def city_validator(city):
    if type(city) != str:
        raise ValueError("City must be a string")
    if not re.match(r"^[a-zA-Z\s]{2,50}$", city):
        raise ValueError("City must be 2-50 characters, letters and spaces only")

def airline_validator(airline):
    if type(airline) != str:
        raise ValueError("Airline must be a string")
    if not re.match(r"^[a-zA-Z0-9\s]{2,50}$", airline):
        raise ValueError("Airline must be 2-50 characters, letters, numbers and spaces")

def datetime_validator(datetime_value):
    if type(datetime_value) != str:
        raise ValueError("Datetime must be a string")
    if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", datetime_value):
        raise ValueError("Datetime must be in format YYYY-MM-DD HH:MM")

def price_validator(price):
    if type(price) != float and type(price) != int:
        raise ValueError("Price must be a number")
    if price < 0:
        raise ValueError("Price cannot be negative")

def seat_no_validator(seat_no):
    if type(seat_no) != int:
        raise ValueError("Seat number must be an integer")
    if seat_no < 1 or seat_no > 300:
        raise ValueError("Seat number must be between 1 and 300")

def sold_validator(value):
    if type(value) != bool:
        raise ValueError("Sold must be a boolean")




