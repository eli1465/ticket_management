from model.entity.ticket import Ticket

ticket_list = []

class TicketController:
    def save(self, id, source, destination, seat_no, date, time, airline):
        try:
            ticket = Ticket(id, source, destination, seat_no, date, time, airline)
            ticket_list.append(ticket)
            return True, f"Ticket Saved Successfully: {ticket}"
        except Exception as e:
            return False, f"Ticket Save Failed\n{e}"

    def edit(self, id, source, destination, seat_no, date, time, airline):
        try:
            ticket = Ticket(id, source, destination, seat_no, date, time, airline)
            # In real use: replace existing ticket by ID
            return True, f"Ticket Edited Successfully: {ticket}"
        except Exception as e:
            return False, f"Ticket Edit Failed\n{e}"

    def delete(self, id):
        try:
            # remove from list by ID
            return True, f"Ticket Removed Successfully - {id}"
        except Exception as e:
            return False, f"Ticket Remove Failed\n{e}"

    def find_all(self):
        try:
            return True, ticket_list
        except Exception as e:
            return False, f"Can't Load Tickets\n{e}"