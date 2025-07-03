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

def id_validator(id):
    if not (type(id) == int and id > 0):
        raise ValueError("Invalid ID")

def city_validator(city):
    if not (type(city) == str and 2 <= len(city) <= 30):
        raise ValueError("Invalid city")

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