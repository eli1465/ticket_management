from model.entity.ticket import Ticket
from model.repository.file_manager import *
from model.tools.validation import *

ticket_list = read_tickets()

class TicketController:
    def save(self,ticket_id,ticket_code,source, destination, airline, start_date_time,end_date_time,price ,seat_no,sold):
        try:
            id_validator(ticket_id)
            code_validator(ticket_code)
            city_validator(source)
            city_validator(destination)
            airline_validator(airline)
            datetime_validator(start_date_time)
            datetime_validator(end_date_time)
            price_validator(price)
            seat_no_validator(seat_no)
            bool_validator(sold)

            ticket = Ticket(ticket_id,ticket_code, source, destination, airline, start_date_time,end_date_time,price,seat_no,sold)
            ticket_list.append(ticket)
            write_tickets(ticket_list)
            return True, f"Ticket Saved Successfully: {ticket}"
        except:
            return False, f"Ticket Save Failed"

    def edit(self,ticket_id,ticket_code,source, destination, airline, start_date_time,end_date_time,price ,seat_no,sold):
        try:
            for index, t in enumerate(ticket_list):
                if t.ticket_id == ticket_id:
                    ticket_list[index] = Ticket(ticket_id, ticket_code, source, destination, airline, start_date_time,
                                                end_date_time, price, seat_no, sold)
                    write_tickets(ticket_list)
                    return True, f"Ticket Edited Successfully: {ticket_list[index]}"
            return False, "Ticket not found"
        except:
            return False, f"Ticket Edit Failed"

    def delete(self,ticket_id):
        try:
            for t in ticket_list:
                if t.ticket_id == ticket_id:
                    ticket_list.remove(t)
                    write_tickets(ticket_list)
                    return True, f"Ticket Removed Successfully: {id}"
            return False, "Ticket not found"
        except:
            return False, f"Ticket Remove Failed"


    def find_all(self):
        try:
            return True, ticket_list
        except:
            return False, f"Can't Load Tickets"

    def find_by_id_ (self,ticket_id):
        try:
            for ticket in ticket_list:
                if ticket.ticket_id == ticket_id:
                    return True,ticket
            return False,"Ticket not found"
        except:
            return False,f"Find Failed"