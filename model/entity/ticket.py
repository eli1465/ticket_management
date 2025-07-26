from model.tools.validation import *

class Ticket:
    def __init__(self, ticket_id, source, destination, seat_no, date, time, airline):
        self.ticket_id = ticket_id
        self.source = source
        self.destination = destination
        self.seat_no = seat_no
        self.date = date
        self.time = time
        self.airline = airline

    def __repr__(self):
        return f"Ticket({self.ticket_id}, {self.source}, {self.destination}, {self.seat_no}, {self.date}, {self.time}, {self.airline})"

    def to_tuple(self):
        return (self.ticket_id, self.source, self.destination, self.seat_no, self.date, self.time, self.airline)

    # ---- ticket_id ----
    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        id_validator(value)
        self._ticket_id = value

    # ---- source ----
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        city_validator(value)
        self._source = value

    # ---- destination ----
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        city_validator(value)
        self._destination = value

    # ---- seat_no ----
    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, value):
        seat_no_validator(value)
        self._seat_no = value

    # ---- date ----
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        date_validator(value)
        self._date = value

    # ---- time ----
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        time_validator(value)
        self._time = value

    # ---- airline ----
    @property
    def airline(self):
        return self._airline

    @airline.setter
    def airline(self, value):
        airline_validator(value)
        self._airline = value

