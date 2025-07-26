from model.entity.ticket import Ticket
from model.repository.file_manager import *
from model.tools.validation import *

ticket_list = read_tickets()

class TicketController:
    def save(self,ticket_id,source, destination,seat_no,date,time,airline):
        try:
            id_validator(ticket_id)
            city_validator(source)
            city_validator(destination)
            seat_no_validator(seat_no)
            datetime_validator(date)
            datetime_validator(time)
            airline_validator(airline)

            ticket = Ticket(ticket_id,source, destination,seat_no,date,time,airline)
            ticket_list.append(ticket)
            write_tickets(ticket_list)
            return True, f"Ticket Saved Successfully: {ticket}"
        except Exception as e:
            return False, f"Ticket Save Failed {e}"

    def edit(self,ticket_id,source, destination,seat_no,date,time,airline):
        try:
            for index, t in enumerate(ticket_list):
                if t.ticket_id == ticket_id:
                    ticket_list[index] = Ticket(ticket_id,source, destination,seat_no,date,time,airline)
                    write_tickets(ticket_list)
                    return True, f"Ticket Edited Successfully: {ticket_list[index]}"
            return False, "Ticket not found"
        except Exception as e:
            return False, f"Ticket Edit Failed {e}"

    def delete(self,ticket_id):
        try:
            for t in ticket_list:
                if t.ticket_id == ticket_id:
                    ticket_list.remove(t)
                    write_tickets(ticket_list)
                    return True, f"Ticket Removed Successfully: {ticket_id}"
            return False, "Ticket not found"
        except Exception as e:
            return False, f"Ticket Remove Failed {e}"

    def find_all(self):
        try:
            return True, ticket_list
        except Exception as e:
            return False, f"Can't Load Tickets {e}"

    def find_by_id_ (self,ticket_id):
        try:
            for ticket in ticket_list:
                if ticket.ticket_id == ticket_id:
                    return True,ticket
            return False,"Ticket not found"
        except Exception as e:
            return False,f"Find Failed {e}"