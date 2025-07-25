from controller.user_controller import UserController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

class UserView:
    def __init__(self):
        self.win = Tk()
        self.win.title("user_view")
        self.win.geometry("900x600")


        #code
        Label(self.win ,text ="Code").place(x=20,Y=20)
        self.code = IntVar()
        Entry(self.win ,textvariable=self.code,width=23,state="readonly").place(x=120,y=20)

        #name
        Label(self.win, text="Name").place(x=20, Y=70)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name, width=23).place(x=120, y=70)

        #family
        Label(self.win, text="Family").place(x=20, Y=120)
        self.family= StringVar()
        Entry(self.win, textvariable=self.family, width=23).place(x=120, y=120)

        #username
        Label(self.win, text="Username").place(x=20, Y=170)
        self.user_name= StringVar()
        Entry(self.win, textvariable=self.user_name, width=23).place(x=120, y=170)

        #password
        Label(self.win, text="Password").place(x=20, Y=220)
        self.password = StringVar()
        Entry(self.win, textvariable=self.password , width=23).place(x=120, y=220)

        #role
        Label(self.win, text="Role").place(x=20, Y=270)
        self. role = StringVar()
        Entry(self.win, textvariable=self.role, width=23).place(x=120, y=270)

        #locked
        Label(self.win, text="locked").place(x=20, Y=320)
        self.locked = BooleanVar()
        Checkbutton(self.win, text="locked",variable=self.locked).place(x=120, y=320)

        #search_by_name_family
        Label(self.win, text="search by Name").place(x=300, Y=20)
        self.search_name= StringVar()
        self.search_name_text =Entry(self.win, textvariable= self.search_name, width=23, fg="gray64")
        self.search_name_text.bind("<keyRelease>",self.search_name_family)
        self.search_name_text.place(x=420,y=20)

        Label(self.win, text="search by Family").place(x=550, Y=20)
        self.search_family = StringVar()
        self.search_family_text =Entry(self.win, textvariable= self.search_family, width=23, fg="gray64")
        self.search_family_text.bind("<keyRelease>", self.search_name_family)
        self.search_family_text.place(x=670, y=20)

        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5,6,7],show="headings")
        self.table.heading(1,text= "code")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Username")
        self.table.heading(5, text="Password")
        self.table.heading(6, text="Role")
        self.table.heading(7, text="Locked")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=60)

        self.table.tag_configure("ok", background="Lightgreen")
        self.table.tag_configure("Locked", background="pink")
        self.table.bind("<ButtonRelease>",self.select_user)
        self.table.place(x=300,y=100,height=460)

        Button(self.win,text= "save",command= self.save_click,width= 34,height= 2).place(x=20,y=450)
        Button(self.win, text="Edit", command=self.edit_click, width=15, height=2).place(x=20, y=520)
        Button(self.win, text="Delete", command=self.delete_click, width=15, height=2).place(x=152, y=520)

        self.reset_form()
        self.win.mainloop()

    def save_click(self):
        user_controller= UserController()
        status,message= user_controller.save(
            self.name.get(),
            self.family.get(),
            self.user_name.get(),
            self.password.get(),
            self.role.get(),
            self.locked.get()
        )
        if status:
            msg.showinfo("save",message)
            self.reset_form()
        else:
            msg.showerror("Save Error",message)

    def edit_click(self):
        user_controller = UserController()
        status, message = user_controller.edit(
            self.name.get(),
            self.family.get(),
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
            self.code.get()
            )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self,status,user_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)
            for user in user_list:
                self.table.insert(
                    "",
                    END,
                    values=user,
                    tags="locked"if user[6] else "OK"
                )
        else:
            msg.showerror("Error","Error getting users data")

    def reset_form(self):
        self.code.set(0)
        self.name.set("")
        self.family.set("")
        self.user_name.set("")
        self.password.set("")
        self.role.set("")
        self.locked.set(False)
        user_controller= UserController()
        status,user_list= user_controller.find_all()
        self.show_data_on_table(status,user_list)

    def search_name_family(self,event):
        user_controller= UserController()
        status, user_list = user_controller.find_by_name_family(self.search_name.get(),self.search_family.get())
        self.show_data_on_table(status, user_list)

    def select_user(self,event):
        user= User(* self.table.item(self.table.focus())["values"])
        self.code.set(user.code)
        self.name.set(user.name)
        self.family.set(user.family)
        self.user_name.set(user.username)
        self.password.set(user.password)
        self.role.set(user.role)
        self.locked.set(bool(user.locked))



