from ..tools.validation import *

class Ticket:
    def __init__(self, id, source, destination, seat_no, date, time, airline):
        self.id = id
        self.source = source
        self.destination = destination
        self.seat_no = seat_no
        self.date = date
        self.time = time
        self.airline = airline

    def __repr__(self):
        return f"Ticket {self.id} - {self.source} to {self.destination} ({self.date} {self.time})"

    def to_tuple(self):
        return self.id, self.source, self.destination, self.seat_no, self.date, self.time, self.airline

    # ---- id ----
    def get_id(self):
        return self._id

    def set_id(self, value):
        id_validator(value)
        self._id = value

    id = property(get_id, set_id)

    # ---- source ----
    def get_source(self):
        return self._source

    def set_source(self, value):
        city_validator(value)
        self._source = value

    source = property(get_source, set_source)

    # ---- destination ----
    def get_destination(self):
        return self._destination

    def set_destination(self, value):
        city_validator(value)
        self._destination = value

    destination = property(get_destination, set_destination)

    # ---- seat_no ----
    def get_seat_no(self):
        return self._seat_no

    def set_seat_no(self, value):
        seat_no_validator(value)
        self._seat_no = value

    seat_no = property(get_seat_no, set_seat_no)

    # ---- date ----
    def get_date(self):
        return self._date

    def set_date(self, value):
        date_validator(value)
        self._date = value

    date = property(get_date, set_date)

    # ---- time ----
    def get_time(self):
        return self._time

    def set_time(self, value):
        time_validator(value)
        self._time = value

    time = property(get_time, set_time)

    # ---- airline ----
    def get_airline(self):
        return self._airline

    def set_airline(self, value):
        airline_validator(value)
        self._airline = value

    airline = property(get_airline, set_airline)