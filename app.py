#!/bin/python
from ttkbootstrap import Window,Label,Entry,Button,Notebook,Frame,Checkbutton,Treeview,Scrollbar,END,DoubleVar,IntVar
from ttkbootstrap.constants import WARNING,DANGER,OUTLINE,SECONDARY,INFO,SUCCESS,DISABLED,NORMAL
from RangeSlider.RangeSlider import RangeSliderH
from mysql.connector import connect
from mysql.connector.errors import DatabaseError,ProgrammingError
from re import compile
valid_float=compile(r'^[0-9]+(\.[0-9]*)?$')
app=Window(title='Login',resizable=(False,False))
#selections
agent:str=None
property_:str=None
client:int=None
#Main Window
def main_app(database):
    app.title('Listings')
    (tabs:=Notebook(app)).pack(expand=True,fill='both')
    tabs.add(property_tab:=Frame(tabs),text='Properties')
    tabs.add(client_tab:=Frame(tabs),text='Clients')
    tabs.add(agent_tab:=Frame(tabs),text='Agents')
    tabs.add(transaction_tab:=Frame(tabs),text='Transactions')
    #property tab
    def query():
        cursor=database.cursor()
        show_all=available.get()==0
        result_view.delete(*result_view.get_children())
        cursor.execute(f'select property_id,address,price,description,area,sold from Properties where address like "%{location_entry.get()}%" and description like "%{description_entry.get()}%" and area between {round(min_area.get()*1900+100,2)} and {round(max_area.get()*1900+100,2)} and price between {round(min_area.get()*1800000+200000,2)} and {round(max_area.get()*1800000+200000,2)} order by area,price;')
        for item_id,address,price,description,area,sold in cursor.fetchall():
            if show_all or not bool(sold):
                result_view.insert("",END,iid=item_id,values=(address,description,str(area),str(price)))
    def select_property(event):
        global property_
        selected=result_view.selection()
        item=result_view.identify_row(event.y)
        if item not in selected:
            property_=item
            result_view.selection_remove(*selected)
            result_view.selection_add(item)
            delete_button.configure(state=NORMAL,bootstyle=OUTLINE)
        else:
            property_=None
            result_view.selection_remove(item)
            delete_button.configure(state=DISABLED,bootstyle=DISABLED)
        return 'break'
    def go_new_property():
        result_view.delete(*result_view.get_children())
        search_property.pack_forget()
        new_property.pack(expand=True,fill='both')
    def remove_property():
        cusor=database.cursor()
        cursor.execute("delete from Properties where property_id=%s",property_)
        result_view.delete(property_)
        property_=None
        delete_button.configure(state=DISABLED,bootstyle=DISABLED)
    def property_back():
        new_property.pack_forget()
        search_property.pack(expand=True,fill='both')
    def add_property():
        err_label_property.configure(bootstyle=WARNING)
        if address_entry.get()=='':err_label_property.configure(text='No address entered')
        elif type_entry.get()=='':err_label_property.configure(text='No description entered')
        elif valid_float.search(price_entry.get())==None:err_label_property.configure(text='Not a valid price')
        elif valid_float.search(area_entry.get())==None:err_label_property.configure(text='Not a valid area')
        elif agent==None:err_label_property.configure(text='No agent selected')
        else:
            database.cursor().execute(
                "insert into Properties (agent_id,address,price,area,description,listing_date,sold) values (%s,%s,%s,%s,%s,%s,false);",
                (
                    agent,
                    address_entry.get(),
                    round(float(price_entry.get()),2),
                    round(float(area_entry.get()),2),
                    description_entry.get(),
                    datetime.now().strftime('%Y-%m-%d')
                )
            )
            address_entry.delete(0,END)
            type_entry.delete(0,END)
            price_entry.delete(0,END)
            area_entry.delete(0,END)
            type_entry.delete(0,END)
            database.commit()
            err_label_property.configure(text='Property registered',bootstyle=INFO)
    (search_property:=Frame(property_tab)).pack(expand=True,fill='both')
    Button(search_property,text='New',command=go_new_property,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (delete_button:=Button(search_property,text='Delete',command=remove_property,state=DISABLED,bootstyle=DISABLED)).grid(row=0,column=1,sticky='NW')
    Label(search_property,text='Location :').grid(row=1,column=0,sticky='E')
    (location_entry:=Entry(search_property)).grid(row=1,column=1,sticky='NSEW')
    Label(search_property,text='Type :').grid(row=2,column=0,sticky='E')
    (description_entry:=Entry(search_property)).grid(row=2,column=1,sticky='W')
    Label(search_property,text='Price :').grid(row=3,column=0,sticky='E')
    min_price=DoubleVar(value=0.0);max_price=DoubleVar(value=1.0)
    (price_slider:=RangeSliderH(search_property,[min_price,max_price],padX=12,show_value=False)).grid(row=3,column=1,sticky='W')
    (price_label:=Label(search_property,text='₹ 2 - 20 Lakh')).grid(row=4,column=1,sticky='NSEW')
    price_change=lambda _,__,___:price_label.configure(text=f'₹ {round(min_price.get()*18+2,2)} - {round(max_price.get()*18+2,2)} Lakh')
    min_price.trace_add('write',price_change)
    max_price.trace_add('write',price_change)
    Label(search_property,text='Area :').grid(row=5,column=0,sticky='E')
    min_area=DoubleVar(value=0.0);max_area=DoubleVar(value=1.0)
    (area_slider:=RangeSliderH(search_property,[min_area,max_area],padX=12,show_value=False)).grid(row=5,column=1,sticky='W')
    (area_label:=Label(search_property,text='100 - 2000 sq feet')).grid(row=6,column=1,sticky='NSEW')
    area_change=lambda _,__,___:area_label.configure(text=f'{round(min_area.get()*1900+100,2)} - {round(max_price.get()*1900+100,2)} sq feet')
    min_area.trace_add('write',area_change)
    max_area.trace_add('write',area_change)
    available=IntVar(search_property,value=1)
    Checkbutton(search_property,text='Show Available',variable=available,onvalue=1,offvalue=0,state='selected',bootstyle=SECONDARY).grid(row=6,column=1,sticky='E')
    Button(search_property,text='Find',command=query).grid(row=7,column=1,sticky='E')
    (scroll:=Scrollbar(search_property,bootstyle=INFO)).grid(row=8,column=2,sticky='NSEW')
    (result_view:=Treeview(search_property,column=('c1','c2','c3','c4'),show='headings',selectmode='browse',bootstyle=INFO,xscrollcommand=scroll.set)).grid(row=8,column=0,columnspan=2,sticky='NSEW')
    result_view.column('0',anchor='e')
    result_view.heading('0',text='Location')
    result_view.column('1',anchor='w')
    result_view.heading('1',text='Description')
    result_view.column('2',anchor='w')
    result_view.heading('2',text='Area (sq feet)')
    result_view.column('3',anchor='w')
    result_view.heading('3',text='Price (₹)')
    scroll.configure(command=result_view.yview)
    result_view.bind('<Button-1>',select_property)
    #new property
    new_property=Frame(property_tab)
    Button(new_property,text='<-',command=property_back,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (err_label_property:=Label(new_property,text='',bootstyle=DANGER)).grid(row=0,column=1,sticky='NSEW')
    Label(new_property,text='Address :').grid(row=1,column=0,sticky='E')
    (address_entry:=Entry(new_property)).grid(row=1,column=1,sticky='W')
    Label(new_property,text='Area(sq feet) :').grid(row=2,column=0,sticky='E')
    (area_entry:=Entry(new_property)).grid(row=2,column=1,sticky='W')
    Label(new_property,text='Description :').grid(row=3,column=0,sticky='E')
    (type_entry:=Entry(new_property)).grid(row=3,column=1,sticky='W')
    Label(new_property,text='Price(₹) :').grid(row=4,column=0,sticky='E')
    (price_entry:=Entry(new_property)).grid(row=4,column=1,sticky='W')
    Button(new_property,text='Add',command=add_property).grid(row=5,columnspan=2,sticky='NSEW')
    #client tab
    def query_client():
        searched=client_entry.get()
        cursor=database.cursor()
        client_view.delete(*client_view.get_children())
        cursor.execute(f'select * from Clients where name like "%{searched}%" or phone like "%{searched}%" or email like "%{searched}%";')
        for client_id,name,phone,email in cursor.fetchall():
            result_view.insert("",END,iid=client_id,values=(name,phone,email))
    def go_new_client():
        see_clients.pack_forget()
        new_client.pack(expand=True,fill='both')
    def client_back():
        new_client.pack_forget()
        see_clients.pack(expand=True,fill='both')
    def add_client():
        err_label_client.configure(bootstyle=WARNING)
        if name_entry_client.get()=='':err_label_client.configure(text='No name entered')
        elif phone_entry_client.get()=='':err_label_client.configure(text='No phone number entered')
        elif email_entry_client.get()=='':err_label_client.configure(text='Not email entered')
        else:
            database.cursor.execute(
                "insert into Clients (name,phone,email) values (%s,%s,%s);",
                (name_entry_client.get(),phone_entry_client.get(),email_entry_client.get())
            )
            name_entry_client.delete(0,END)
            phone_entry_client.delete(0,END)
            email_entry_client.delete(0,END)
            database.commt()
            err_label_client.configure(text='Client registered',bootstyle=INFO)
    def remove_client():
        cusor=database.cursor()
        cursor.execute("delete from Clients where property_id=%s",client)
        client_view.delete(client)
        client=None
        delete_client_button.configure(state=DISABLED,bootstyle=DISABLED)
    def select_client(event):
        global client
        selected=client_view.selection()
        item=client_view.identify_row(event.y)
        if item not in selected:
            client=int(item)
            client_view.selection_remove(*selected)
            client_view.selection_add(item)
            delete_client_button.configure(state=NORMAL,bootstyle=OUTLINE)
        else:
            client=None
            client_view.selection_remove(item)
            delete_client_button.configure(state=DISABLED,bootstyle=DISABLED)
        return 'break'
    (see_clients:=Frame(client_tab)).pack(expand=True,fill='both')
    see_clients.rowconfigure(2,weight=3)
    see_clients.columnconfigure(1,weight=4)
    Button(see_clients,text='New',command=go_new_client,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (delete_client_button:=Button(see_clients,text='Delete',command=remove_client,state=DISABLED,bootstyle=DISABLED)).grid(row=0,column=1,sticky='NW')
    Label(see_clients,text='Search :').grid(row=1,column=0,sticky='E')
    (client_entry:=Entry(see_clients)).grid(row=1,column=1,sticky='NSEW')
    (client_scroll:=Scrollbar(see_clients,bootstyle=INFO)).grid(row=2,column=2,sticky='NSEW')
    (client_view:=Treeview(see_clients,column=('c1','c2','c3'),show='headings',selectmode='browse',bootstyle=INFO,xscrollcommand=client_scroll.set)).grid(row=2,column=0,columnspan=2,sticky='NSEW')
    client_view.column('0',anchor='e')
    client_view.heading('0',text='Name')
    client_view.column('1',anchor='w')
    client_view.heading('1',text='Phone')
    client_view.column('2',anchor='w')
    client_view.heading('2',text='Email')
    client_scroll.configure(command=client_view.yview)
    client_view.bind('<Button-1>',select_client)
    query_client()
    #new client
    new_client=Frame(client_tab)
    Button(new_client,text='<-',command=client_back,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (err_label_client:=Label(new_client,text='',bootstyle=DANGER)).grid(row=0,column=1,sticky='NSEW')
    Label(new_client,text='Name :').grid(row=1,column=0,sticky='E')
    (name_entry_client:=Entry(new_client)).grid(row=1,column=1,sticky='W')
    Label(new_client,text='Phone :').grid(row=2,column=0,sticky='E')
    (phone_entry_client:=Entry(new_client)).grid(row=2,column=1,sticky='W')
    Label(new_client,text='Email :').grid(row=3,column=0,sticky='E')
    (email_entry_client:=Entry(new_client)).grid(row=3,column=1,sticky='W')
    Button(new_client,text='Add',command=add_client).grid(row=4,columnspan=2,sticky='NSEW')
    #client tab
    #new client
    #transaction rab
    #new transaction
#Login window
def login(*_):
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
        main_app(db)#move to next window
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
