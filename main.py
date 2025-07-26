from view.user_view import UserView
from view.ticket_view import TicketView

if __name__ == "__main__":
    print("Select interface:")
    print("1. User Managment(GUI)")
    print("2. Ticket Managment(GUI)")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        UserView()
    elif choice == "2":
        TicketView()
    else:
        print("Invalid choice.")