import re

def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name)):
        raise ValueError("Invalid name")

def family_validator(family):
    if not (isinstance(family, str) and re.match(r"^[a-zA-Z\s]{3,30}$", family)):
        raise ValueError("Invalid family")

def id_validator(id):
    if not (isinstance(id, int) and id > 0):
        raise ValueError("Invalid ID (must be positive integer)")

def username_validator(username):
    if not (isinstance(username, str) and 3 <= len(username) <= 30):
        raise ValueError("Invalid username")

def password_validator(password):
    if not (type(password) == str and len(password) >= 6):
        raise ValueError("Invalid password")

def bool_validator(value):
    if not (isinstance(value, bool) or str(value).lower() in ['true', 'false']):
        raise ValueError("Invalid boolean value (true/false only)")

def role_validator(role):
    if str(role).lower() not in ['customer', 'admin']:
        raise ValueError("Invalid role. Must be 'customer' or 'admin'")

# ticket
def city_validator(city):
    if not (isinstance(city, str) and re.match(r"^[a-zA-Z\s]{2,50}$", city)):
        raise ValueError("Invalid city")

def code_validator(code):
    if not (type(code) == str and 3 <= len(code) <= 20):
        raise ValueError("Invalid ticket code")

def datetime_validator(dt):
    import re
    if not (type(dt) == str and re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', dt)):
        raise ValueError("Invalid datetime format (YYYY-MM-DD HH:MM)")

def seat_no_validator(seat_no):
    if not (type(seat_no) == int and 1 <= seat_no <= 300):
        raise ValueError("Invalid seat number")

def date_validator(date):
    if not (type(date) == str and re.match(r"\d{4}-\d{2}-\d{2}$", date)):
        raise ValueError("Invalid date (YYYY-MM-DD)")

def time_validator(time):
    if not (isinstance(time, str) and re.match(r"^\d{2}:\d{2}$", time)):
        raise ValueError("Invalid time (HH:MM)")

def airline_validator(airline):
    if not (isinstance(airline, str) and 2 <= len(airline) <= 50):
        raise ValueError("Invalid airline name")