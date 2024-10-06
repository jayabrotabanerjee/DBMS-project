#!/bin/python
from ttkbootstrap import Window,Label,Entry,Button,Notebook,Frame,END
from ttkbootstrap.constants import WARNING,DANGER
from mysql.connector import connect
from mysql.connector.errors import DatabaseError,ProgrammingError
app=Window(title='Login',resizable=(False,False))
#Main Window
def main_app():
    app.title('Listings')
    (tabs:=Notebook(app)).pack(expand=True,fill='both')
    tabs.add(property_tab:=Frame(tabs),text='Properties')
    tabs.add(client_tab:=Frame(tabs),text='Clients')
    tabs.add(agent_tab:=Frame(tabs),text='Agents')
    tabs.add(transaction_tab:=Frame(tabs),text='Transaction')
#Login window
def login(*_):
    global db
    try:
        db=connect(
            host='localhost',
            user=username_entry.get(),
            password=password_entry.get(),
            database='RealEstateDB',
            collation='utf8mb4_unicode_520_ci'
        )
        for i in app.winfo_children():
            i.destroy()
        main_app()#move to next window
    except ProgrammingError:
        err_label.config(text='Access Denied',bootstyle=DANGER)
        username_entry.delete(0,END)
        password_entry.delete(0,END)
    except DatabaseError:
        err_label.config(text='Server not running',bootstyle=WARNING)
(err_label:=Label(app)).grid(row=0,column=0,columnspan=2)
Label(app,text='User :').grid(row=1,column=0,sticky='E')
(username_entry:=Entry(app)).grid(row=1,column=1)
Label(app,text='Password :').grid(row=2,column=0,sticky='E')
(password_entry:=Entry(app,show='*')).grid(row=2,column=1)
password_entry.bind('<Return>',login)
Button(app,text='Login',command=login).grid(row=3,column=0,columnspan=2)
app.mainloop()
