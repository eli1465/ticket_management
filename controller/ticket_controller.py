from model.repository import file_manager
from model.entity.ticket import Ticket
from model.tools.validation import *

class TicketController:
    def save(self, ticket_id, ticket_code, origin, destination, airline,
             start_date_time, end_date_time, price, seat_no, sold):
        try:
            ticket_id_validator(ticket_id)
            ticket_code_validator(ticket_code)
            city_validator(origin)
            city_validator(destination)
            airline_validator(airline)
            datetime_validator(start_date_time)
            datetime_validator(end_date_time)
            price_validator(price)
            seat_no_validator(seat_no)
            bool_validator(sold)

            ticket_list = file_manager.read_tickets()
            for t in ticket_list:
                if t.ticket_code == ticket_code:
                    return False, "Ticket code already exists."

            ticket = Ticket(ticket_id, ticket_code, origin, destination, airline,
                            start_date_time, end_date_time, price, seat_no, sold)

            ticket_list.append(ticket)
            file_manager.write_tickets(ticket_list)
            return True, "Ticket saved successfully."

        except Exception as e:
            return False, str(e)

    def edit(self, ticket_id, ticket_code, origin, destination, airline,
             start_date_time, end_date_time, price, seat_no, sold):
        try:
            ticket_code_validator(ticket_code)
            city_validator(origin)
            city_validator(destination)
            airline_validator(airline)
            datetime_validator(start_date_time)
            datetime_validator(end_date_time)
            price_validator(price)
            seat_no_validator(seat_no)
            bool_validator(sold)

            ticket_list = file_manager.read_tickets()
            for i in range(len(ticket_list)):
                if ticket_list[i].ticket_id == ticket_id:
                    ticket_list[i] = Ticket(ticket_id, ticket_code, origin, destination, airline,
                                            start_date_time, end_date_time, price, seat_no, sold)
                    file_manager.write_tickets(ticket_list)
                    return True, "Ticket updated successfully."

            return False, "Ticket not found."

        except Exception as e:
            return False, str(e)

    def delete(self, ticket_id):
        try:
            ticket_id_validator(ticket_id)
            ticket_list = file_manager.read_tickets()
            for t in ticket_list:
                if t.ticket_id == ticket_id:
                    ticket_list.remove(t)
                    file_manager.write_tickets(ticket_list)
                    return True, "Ticket deleted."
            return False, "Ticket not found."
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            ticket_list = file_manager.read_tickets()
            return True, ticket_list
        except Exception as e:
            return False, str(e)

    def find_by_ticket_code(self, ticket_code):
        try:
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.ticket_code == ticket_code and not t.sold]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_origin(self, origin):
        try:
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.origin == origin and not t.sold]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_destination(self, destination):
        try:
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.destination == destination and not t.sold]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_airline(self, airline):
        try:
            airline_validator(airline)
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.airline == airline and not t.sold]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_start_date_time(self, start_date_time):
        try:
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.start_date_time == start_date_time and not t.sold]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_end_date_time(self, end_date_time):
        try:
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.end_date_time == end_date_time and not t.sold]
            return True, result
        except Exception as e:
            return False, str(e)

    def find_by_sold(self, sold):
        try:
            bool_validator(sold)
            sold_value = str(sold).lower() == "true"
            ticket_list = file_manager.read_tickets()
            result = [t for t in ticket_list if t.sold == sold_value]
            return True, result
        except Exception as e:
            return False, str(e)