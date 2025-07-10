import re

def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name)):
        raise ValueError("Invalid name")

def family_validator(family):
    if not (type(family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", family)):
        raise ValueError("Invalid family")

def age_validator(age):
    if not (type(age) == int and 0 < age < 150):
        raise ValueError("Invalid age")

def id_validator(person_id):
    if not (type(person_id) == int and 1 <= person_id):
        raise ValueError("Invalid ID")

def username_validator(username):
    if not (type(username) == str and 3 <= len(username) <= 30):
        raise ValueError("Invalid username")

def password_validator(password):
    if not (type(password) == str and len(password) >= 6):
        raise ValueError("Invalid password")

def bool_validator(value):
    if str(value).lower() not in ['true', 'false']:
        raise ValueError("Invalid boolean value (true/false only)")

def role_validator(role):
    if role not in ['customer', 'admin']:
        raise ValueError("Invalid role. Must be 'customer' or 'admin'")

#ticket
def city_validator(city):
    if not (type(city) == str and 2 <= len(city) <= 30):
        raise ValueError("Invalid city")
def code_validator(code):
    if not (type(code) == str and 3 <= len(code) <= 20):
        raise ValueError("Invalid ticket code")

def datetime_validator(dt):
    import re
    if not (type(dt) == str and re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', dt)):
        raise ValueError("Invalid datetime format (YYYY-MM-DD HH:MM)")

def price_validator(price):
    if not (type(price) == int and price > 0):
        raise ValueError("Invalid price")

def seat_no_validator(seat_no):
    if not (type(seat_no) == int and seat_no > 0):
        raise ValueError("Invalid seat number")

def seat_no_validator(seat_no):
    if not (type(seat_no) == int and 1 <= seat_no <= 300):
        raise ValueError("Invalid seat number")

def date_validator(date):
    if not (type(date) == str and re.match(r"\d{4}-\d{2}-\d{2}$", date)):
        raise ValueError("Invalid date (YYYY-MM-DD)")

def time_validator(time):
    if not (type(time) == str and re.match(r"\d{2}:\d{2}$", time)):
        raise ValueError("Invalid time (HH:MM)")

def airline_validator(name):
    if not (type(name) == str and 2 <= len(name) <= 50):
        raise ValueError("Invalid airline")