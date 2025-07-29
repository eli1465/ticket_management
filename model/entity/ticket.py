from model.tools.validation import *

class Ticket:
    def __init__(self, ticket_id, ticket_code, origin, destination, airline,
                 start_date_time, end_date_time, price, seat_no, sold):
        self.ticket_id = ticket_id
        self.ticket_code = ticket_code
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.price = price
        self.seat_no = seat_no
        self.sold = sold

    def __str__(self):
        return f"{self.ticket_code}: {self.origin} → {self.destination}, {self.airline}, {self.start_date_time}"

    def __repr__(self):
        return f"Ticket({self.ticket_id}, {self.ticket_code}, {self.origin}, {self.destination})"

    def to_tuple(self):
        return (self.ticket_id, self.ticket_code, self.origin, self.destination,
                self.airline, self.start_date_time, self.end_date_time,
                self.price, self.seat_no, self.sold)

    # ---------- ticket_id ----------
    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        ticket_id_validator(value)
        self._ticket_id = value

    # ---------- ticket_code ----------
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        ticket_code_validator(value)
        self._ticket_code = value

    # ---------- origin ----------
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        city_validator(value)
        self._origin = value

    # ---------- destination ----------
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        city_validator(value)
        self._destination = value

    # ---------- airline ----------
    @property
    def airline(self):
        return self._airline

    @airline.setter
    def airline(self, value):
        airline_validator(value)
        self._airline = value

    # ---------- start_date_time ----------
    @property
    def start_date_time(self):
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        datetime_validator(value)
        self._start_date_time = value

    # ---------- end_date_time ----------
    @property
    def end_date_time(self):
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        datetime_validator(value)
        self._end_date_time = value

    # ---------- price ----------
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value

    # ---------- seat_no ----------
    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, value):
        seat_no_validator(value)
        self._seat_no = value

    # ---------- sold ----------
    @property
    def sold(self):
        return self._sold

    @sold.setter
    def sold(self, value):
        sold_validator(value)
        self._sold = value