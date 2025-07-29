from controller.user_controller import UserController
from tkinter import *
from tkinter import ttk, messagebox as msg
from model.entity.user import User

class UserView:
    def __init__(self):
        self.win = Tk()
        self.win.title("User Manager")
        self.win.geometry("1150x600")

        self.user_controller = UserController()

        Label(self.win, text="ID").place(x=20, y=20)
        self.user_id = IntVar()
        Entry(self.win, textvariable=self.user_id, width=23).place(x=120, y=20)

        Label(self.win, text="Name").place(x=20, y=70)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name, width=23).place(x=120, y=70)

        Label(self.win, text="Family").place(x=20, y=120)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family, width=23).place(x=120, y=120)

        Label(self.win, text="Username").place(x=20, y=170)
        self.user_name = StringVar()
        Entry(self.win, textvariable=self.user_name, width=23).place(x=120, y=170)

        Label(self.win, text="Password").place(x=20, y=220)
        self.password = StringVar()
        Entry(self.win, textvariable=self.password, width=23, show="*").place(x=120, y=220)

        Label(self.win, text="Birth Date").place(x=20, y=270)
        self.birth_date = StringVar()
        Entry(self.win, textvariable=self.birth_date, width=23).place(x=120, y=270)

        Label(self.win, text="Role").place(x=20, y=320)
        self.role = StringVar()
        self.role_combo = ttk.Combobox(self.win, textvariable=self.role, width=20, values=["customer", "admin"])
        self.role_combo.place(x=120, y=320)

        Label(self.win, text="Locked").place(x=20, y=370)
        self.locked = BooleanVar()
        Checkbutton(self.win, variable=self.locked).place(x=120, y=370)


        Label(self.win, text="Search by Name").place(x=400, y=20)
        self.search_name = StringVar()
        self.search_name_text = Entry(self.win, textvariable=self.search_name, width=23, fg="gray64")
        self.search_name_text.bind("<KeyRelease>", self.search_name_family)
        self.search_name_text.place(x=530, y=20)

        Label(self.win, text="Search by Family").place(x=750, y=20)
        self.search_family = StringVar()
        self.search_family_text = Entry(self.win, textvariable=self.search_family, width=23, fg="gray64")
        self.search_family_text.bind("<KeyRelease>", self.search_name_family)
        self.search_family_text.place(x=870, y=20)

        Label(self.win, text="Search by Username").place(x=400, y=70)
        self.search_username = StringVar()
        Entry(self.win, textvariable=self.search_username, width=23).place(x=530, y=70)

        Label(self.win, text="Search by Role").place(x=750, y=70)
        self.search_role = StringVar()
        self.search_role_combo = ttk.Combobox(self.win, textvariable=self.search_role, values=["customer", "admin"], width=20)
        self.search_role_combo.place(x=870, y=70)


        self.table = ttk.Treeview(self.win, columns=[1,2,3,4,5,6,7,8], show="headings")
        self.table.heading(1, text="ID")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Username")
        self.table.heading(5, text="Password")
        self.table.heading(6, text="BirthDate")
        self.table.heading(7, text="Role")
        self.table.heading(8, text="Locked")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=60)

        self.table.tag_configure("ok", background= "light green")
        self.table.tag_configure("locked", background="pink")
        self.table.bind("<ButtonRelease>", self.select_user)
        self.table.place(x=400, y=120, height=450)

        #Button
        Button(self.win, text="Save", command=self.save_click, width=10, height=2).place(x=20, y=420)
        Button(self.win, text="Edit", command=self.edit_click, width=10,  height=2).place(x=120, y=420)
        Button(self.win, text="Delete", command=self.delete_click, width=10,  height=2).place(x=220, y=420)


        self.reset_form()

        self.win.mainloop()

    def save_click(self):
        user_controller = UserController()
        status, message = user_controller.save(
            self.user_id.get(),
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.user_name.get(),
            self.password.get(),
            self.role.get(),
            self.locked.get()
            )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        user_controller = UserController()
        status, message = user_controller.edit(
                self.user_id.get(),
                self.name.get(),
                self.family.get(),
                self.birth_date.get(),
                self.user_name.get(),
                self.password.get(),
                self.role.get(),
                self.locked.get()
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        user_controller = UserController()
        status, message = user_controller.delete(
            self.user_id.get()
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def select_user(self,event=NONE):
        user = User(*self.table.item(self.table.focus())["values"])
        self.user_id.set(user.user_id)
        self.name.set(user.name)
        self.family.set(user.family)
        self.user_name.set(user.username)
        self.password.set(user.password)
        self.birth_date.set(user.birth_date)
        self.role_combo.set(user.role)
        self.locked.set(bool(user.locked))

    def reset_form(self):
        self.user_id.set(0)
        self.name.set("")
        self.family.set("")
        self.user_name.set("")
        self.password.set("")
        self.birth_date.set("")
        self.role.set("")
        self.role_combo.set("")
        self.locked.set(False)
        user_controller = UserController()
        status, user_list = user_controller.find_all()
        self.show_data_on_table(status, user_list)

    def show_data_on_table(self, status, user_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)
            for user in user_list:
                tag = "locked" if user[7] else "ok"
                self.table.insert("", END, values=user, tags=tag)
        else:
            msg.showerror("Error", "Error getting users data")

    def search_name_family(self, event):
        user_controller = UserController()
        status, user_list = user_controller.find_by_name_family(
            self.search_name.get(), self.search_family.get()
        )
        self.show_data_on_table(status, user_list)