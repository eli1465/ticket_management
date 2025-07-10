from controller.ticket_controller import TicketController
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from view import *
from model.repository.file_manager import *

class TicketView:
    def save_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.save(
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
        else:
            msg.showerror("Save Error", message)

    def __init__(self):
        win=TK()
        win.geometry("300x400")

        self.id = IntVar()
        self.source = StringVar()
        self.destination = StringVar()
        self.seat_no = IntVar()
        self.date = StringVar()
        self.time = StringVar()
        self.airline = StringVar()

        Entry(win, textvariable=self.id).pack()
        Entry(win, textvariable=self.source).pack()
        Entry(win, textvariable=self.destination).pack()
        Entry(win, textvariable=self.seat_no).pack()
        Entry(win, textvariable=self.date).pack()
        Entry(win, textvariable=self.time).pack()
        Entry(win, textvariable=self.airline).pack()

        Button(win, text="Save", command=self.save_click).pack()
        win.mainloop()