from controller.ticket_controller import TicketController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

class TicketView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Ticket Manager")
        self.win.geometry("900x600")

        self.ticket_controller = TicketController()

        # id
        Label(self.win, text="ID").place(x=20, y=20)
        self.id = IntVar()
        Entry(self.win, textvariable=self.id, width=23).place(x=120, y=20)

        # source
        Label(self.win, text="Source").place(x=20, y=70)
        self.source = StringVar()
        Entry(self.win, textvariable=self.source, width=23).place(x=120, y=70)

        # destination
        Label(self.win, text="Destination").place(x=20, y=120)
        self.destination = StringVar()
        Entry(self.win, textvariable=self.destination, width=23).place(x=120, y=120)

        # seat_no
        Label(self.win, text="Seat No").place(x=20, y=170)
        self.seat_no = StringVar()
        Entry(self.win, textvariable=self.seat_no, width=23).place(x=120, y=170)

        # date
        Label(self.win, text="Date (YYYY-MM-DD)").place(x=20, y=220)
        self.date = StringVar()
        Entry(self.win, textvariable=self.date, width=23).place(x=120, y=220)

        # time
        Label(self.win, text="Time (HH:MM)").place(x=20, y=270)
        self.time = StringVar()
        Entry(self.win, textvariable=self.time, width=23).place(x=120, y=270)

        # airline
        Label(self.win, text="Airline").place(x=20, y=320)
        self.airline = StringVar()
        Entry(self.win, textvariable=self.airline, width=23).place(x=120, y=320)

        # دکمه‌ها
        Button(self.win, text="Save", command=self.save_click, width=34, height=2).place(x=20, y=450)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=520)
        Button(self.win, text="Delete", command=self.delete_click, width=15, height=2).place(x=152, y=520)
        Button(self.win, text="Show All", command=self.show_all_click).place(x=20, y=550)
        # جدول
        self.table = ttk.Treeview(self.win, columns=[1,2,3,4,5,6,7], show="headings")
        self.table.heading(1, text="ID")
        self.table.heading(2, text="Source")
        self.table.heading(3, text="Destination")
        self.table.heading(4, text="Seat No")
        self.table.heading(5, text="Date")
        self.table.heading(6, text="Time")
        self.table.heading(7, text="Airline")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=80)
        self.table.column(5, width=100)
        self.table.column(6, width=80)
        self.table.column(7, width=100)

        self.table.place(x=300, y=100, height=460)
        self.table.bind("<<TreeviewSelect>>", self.on_table_select)

        self.reset_form()
        self.refresh_tree()
        self.win.mainloop()

    def save_click(self):
        status, message = self.ticket_controller.save(
            self.id.get(),
            self.source.get(),
            self.destination.get(),
            self.seat_no.get(),
            self.date.get(),
            self.time.get(),
            self.airline.get()
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
            self.refresh_tree()
        else:
            msg.showerror("Save Error", message)

    def delete_click(self):
        status, message = self.ticket_controller.delete(self.id.get())
        if status:
            msg.showinfo("Delete", message)
            self.reset_form()
            self.refresh_tree()
        else:
            msg.showerror("Delete Error", message)

    def edit_click(self):
        status, message = self.ticket_controller.edit(
            self.id.get(),
            self.source.get(),
            self.destination.get(),
            self.seat_no.get(),
            self.date.get(),
            self.time.get(),
            self.airline.get()
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
            self.refresh_tree()
        else:
            msg.showerror("Edit Error", message)

   
    def refresh_tree(self):
        status, r = self.ticket_controller.find_all()
        if status:
            for item in self.table.get_children():
                self.table.delete(item)
            for ticket in r:
                self.table.insert("", END, values=ticket.to_tuple())

    def reset_form(self):
        self.id.set("")
        self.source.set("")
        self.destination.set("")
        self.seat_no.set("")
        self.date.set("")
        self.time.set("")
        self.airline.set("")

    def show_all_click(self):
        self.refresh_tree()

    def on_table_select(self, event):
        selected = self.table.focus()
        if not selected:
            return
        values = self.table.item(selected, "values")
        if not values:
            return
        self.id.set(values[0])
        self.source.set(values[1])
        self.destination.set(values[2])
        self.seat_no.set(values[3])
        self.date.set(values[4])
        self.time.set(values[5])
        self.airline.set(values[6])

   