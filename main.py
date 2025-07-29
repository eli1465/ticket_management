from view.user_view import UserView
from view.ticket_view import TicketView

if __name__ == "__main__":
    print("Select interface:")
    print("1. User ManagerGUI)")
    print("2. Ticket ManagerGUI)")
    choice = input("Enter your choice please(1/2): ")

    if choice == "1":
        UserView()
    elif choice == "2":
        TicketView()
    else:
        print("Invalid choice.")