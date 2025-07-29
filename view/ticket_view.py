from controller.ticket_controller import *
from tkinter import *
from tkinter import ttk, messagebox as msg
from model.entity.ticket import Ticket

class TicketView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Ticket Manager")
        self.win.geometry("1400x700")

        Label(self.win, text="Ticket ID").place(x=20, y=20)
        self.ticket_id = IntVar()
        Entry(self.win, textvariable=self.ticket_id, width=23,state ="readonly").place(x=150, y=20)

        Label(self.win, text="Ticket Code").place(x=20, y=60)
        self.ticket_code = StringVar()
        Entry(self.win, textvariable=self.ticket_code, width=23).place(x=150, y=60)

        Label(self.win, text="Origin").place(x=20, y=100)
        self.origin = StringVar()
        Entry(self.win, textvariable=self.origin, width=23).place(x=150, y=100)

        Label(self.win, text="Destination").place(x=20, y=140)
        self.destination = StringVar()
        Entry(self.win, textvariable=self.destination, width=23).place(x=150, y=140)

        Label(self.win, text="Airline").place(x=20, y=180)
        self.airline = StringVar()
        self.airline = ttk.Combobox(self.win, textvariable=self.airline, values=["IranAir", "Mahan", "Kish","Qeshm", "ATA"], width=20, state="readonly")
        self.airline.place(x=150, y=180)

        Label(self.win, text="Start DateTime").place(x=20, y=220)
        self.start_date_time = StringVar()
        Entry(self.win, textvariable=self.start_date_time, width=23).place(x=150, y=220)

        Label(self.win, text="End DateTime").place(x=20, y=260)
        self.end_date_time = StringVar()
        Entry(self.win, textvariable=self.end_date_time, width=23).place(x=150, y=260)

        Label(self.win, text="Price").place(x=20, y=300)
        self.price = IntVar()
        Entry(self.win, textvariable=self.price, width=23).place(x=150, y=300)

        Label(self.win, text="Seat No").place(x=20, y=340)
        self.seat_no = IntVar()
        Entry(self.win, textvariable=self.seat_no, width=23).place(x=150, y=340)

        Label(self.win, text="Sold").place(x=20, y=380)
        self.sold = BooleanVar()
        self.sold = ttk.Combobox(self.win, textvariable=self.sold, values=["True", "False"], width=20, state="readonly")
        self.sold.place(x=150, y=380)

        Button(self.win, text="Save",command=self.save_click, width=34, height=2, ).place(x=20, y=440)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=510)
        Button(self.win, text="Delete", command=self.delete_click,  width=15, height=2).place(x=155, y=510)
        Button(self.win, text="Show All", command=self.show_all_click, width=34, height=2).place(x=20, y=580)

        Label(self.win, text="Search Code").place(x=420, y=20)
        self.search_code = StringVar()
        self.search_code_text = Entry(self.win, textvariable=self.search_code, width=23)
        self.search_code_text.bind("<KeyRelease>", self.search_by_code)
        self.search_code_text.place(x=540, y=20)

        Label(self.win, text="Search Origin").place(x=420, y=60)
        self.search_origin = StringVar()
        self.search_origin_text= Entry(self.win, textvariable=self.search_origin, width=23)
        self.search_origin_text.bind("<KeyRelease>", self.search_by_origin)
        self.search_origin_text.place(x=540, y=60)

        Label(self.win, text="Search Destination").place(x=420, y=140)
        self.search_destination = StringVar()
        self.search_destination_text = Entry(self.win, textvariable=self.search_destination, width=23)
        self.search_destination_text.place(x=540, y=140)
        self.search_destination_text.bind("<KeyRelease>", self.search_by_destination)

        Label(self.win, text="Search Airline").place(x=420, y=100)
        self.search_airline = StringVar()
        self.search_airline_combo = ttk.Combobox(self.win, textvariable=self.search_airline,
                                                 values=["IranAir", "Mahan", "Kish", "Qeshm", "ATA"], width=20,
                                                 state="readonly")
        self.search_airline_combo.place(x=540, y=100)
        self.search_airline_combo.bind("<<ComboboxSelected>>", self.search_by_airline)

        Label(self.win, text="Search Start Date").place(x=780, y=60)
        self.search_start = StringVar()
        self.search_start_text = Entry(self.win, textvariable=self.search_start, width=23)
        self.search_start_text.place(x=950, y=60)
        self.search_start_text.bind("<KeyRelease>", self.search_by_start)

        Label(self.win, text="Search by End Date").place(x=780, y=100)
        self.search_end = StringVar()
        self.search_end_text = Entry(self.win, textvariable=self.search_end, width=23)
        self.search_end_text.place(x=950, y=100)
        self.search_end_text.bind("<KeyRelease>", self.search_by_end)

        Label(self.win, text="Search Sold").place(x=780, y=140)
        self.search_sold = StringVar()
        self.search_sold_combo = ttk.Combobox(self.win, textvariable=self.search_sold, values=["True", "False"],
                                              width=20, state="readonly")
        self.search_sold_combo.place(x=950, y=140)
        self.search_sold_combo.bind("<<ComboboxSelected>>", self.search_by_sold)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6,7,8,9,10), show="headings")
        self.table.heading(1, text="ID")
        self.table.heading(2, text="Code")
        self.table.heading(3, text="Origin")
        self.table.heading(4, text="Destination")
        self.table.heading(5, text="Airline")
        self.table.heading(6, text="Start DateTime")
        self.table.heading(7, text="End DateTime")
        self.table.heading(8, text="Price")
        self.table.heading(9, text="Seat No")
        self.table.heading(10, text="Sold")

        self.table.column(1, width=80)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=120)
        self.table.column(7, width=120)
        self.table.column(8, width=80)
        self.table.column(9, width=80)
        self.table.column(10, width=60)

        self.table.place(x=400, y=180, height=480)
        self.table.bind("<ButtonRelease>", self.select_ticket)

        self.reset_form()

        self.win.mainloop()

    def save_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.save(
                self.ticket_code.get(),
                self.origin.get(),
                self.destination.get(),
                self.airline.get(),
                self.start_date_time.get(),
                self.end_date_time.get(),
                self.price.get(),
                self.seat_no.get(),
                self.sold.get() in ["True", True]
        )

        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.edit(
            self.ticket_id.get(),
            self.ticket_code.get(),
            self.origin.get(),
            self.destination.get(),
            self.airline.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.price.get(),
            self.seat_no.get(),
            self.sold.get() in ["True", True]
            )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error",message )

    def delete_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.delete(
            self.ticket_code.get()
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_all_click(self):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_all()
        self.show_data_on_table(status, ticket_list)

    def select_ticket(self, event):
        ticket = Ticket(*self.table.item(self.table.focus())["values"])
        self.ticket_id.set(ticket.ticket_id)
        self.ticket_code.set(ticket.ticket_code)
        self.origin.set(ticket.origin)
        self.destination.set(ticket.destination)
        self.airline.set(ticket.airline)
        self.start_date_time.set(ticket.start_date_time)
        self.end_date_time.set(ticket.end_date_time)
        self.price.set(ticket.price)
        self.seat_no.set(ticket.seat_no)
        self.sold.set(ticket.sold)


    def reset_form(self):
        self.ticket_id.set(0)
        self.ticket_code.set("")
        self.origin.set("")
        self.destination.set("")
        self.airline.set("IranAir")
        self.start_date_time.set("")
        self.end_date_time.set("")
        self.price.set(0)
        self.seat_no.set(0)
        self.sold.set("False")

        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_all()
        self.show_data_on_table(status, ticket_list)

    def show_data_on_table(self, status, ticket_list):
        for i in self.table.get_children():
            self.table.delete(i)
        if status:
            for ticket in ticket_list:
                if ticket[-1] == "False":
                    self.table.insert("", END, values=ticket)
        else:
            msg.showerror("Error", "Failed to load tickets")

    def search_by_code(self,event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_by_ticket_code(self.search_code.get())
        self.show_data_on_table(status, ticket_list)

    def search_by_origin(self, event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_by_origin(self.search_origin.get())
        self.show_data_on_table(status, ticket_list)

    def search_by_destination(self, event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_by_destination(self.search_destination.get())
        self.show_data_on_table(status, ticket_list)

    def search_by_airline(self, event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_by_airline(self.search_airline.get())
        self.show_data_on_table(status, ticket_list)

    def search_by_start(self, event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_by_start_date_time(self.search_start.get())
        self.show_data_on_table(status, ticket_list)

    def search_by_end(self, event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_by_end_date_time(self.search_end.get())
        self.show_data_on_table(status, ticket_list)

    def search_by_sold(self, event):
        ticket_controller= TicketController()
        status, ticket_list = ticket_controller.find_by_sold(self.search_sold.get())
        self.show_data_on_table(status, ticket_list)

