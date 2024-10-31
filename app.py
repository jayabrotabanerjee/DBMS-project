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
    (delete_button:=Button(search_property,text='Delete',command=remove_property,state=DISABLED)).grid(row=0,column=1,sticky='NW')
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
    def query_client(_):
        searched=client_entry.get()
        cursor=database.cursor()
        client_view.delete(*client_view.get_children())
        cursor.execute(f'select * from Clients where name like "%{searched}%" or phone like "%{searched}%" or email like "%{searched}%";')
        for client_id,name,phone,email in cursor.fetchall():
            client_view.insert("",END,iid=client_id,values=(name,phone,email))
    def go_new_client():
        see_clients.pack_forget()
        new_client.pack(expand=True,fill='both')
    def client_back():
        new_client.pack_forget()
        see_clients.pack(expand=True,fill='both')
        query_client(None)
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
            client=item
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
    client_entry.bind('<KeyRelease>',query_client)
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
    query_client(None)
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
    #agent tab
    def add_agent():
        err_label_agent.configure(bootstyle=WARNING)
        if name_entry_agent.get()=='':err_label_agent.configure(text='No name entered')
        elif phone_entry_agent.get()=='':err_label_agent.configure(text='No phone number entered')
        elif email_entry_agent.get()=='':err_label_agent.configure(text='Not email entered')
        else:
            database.cursor.execute(
                "insert into Agents (name,phone,email) values (%s,%s,%s);",
                (name_entry_agent.get(),phone_entry_agent.get(),email_entry_agent.get())
            )
            name_entry_agent.delete(0,END)
            phone_entry_agent.delete(0,END)
            email_entry_agent.delete(0,END)
            database.commt()
            err_label_agent.configure(text='Agent registered',bootstyle=INFO)
    def remove_agent():
        cusor=database.cursor()
        cursor.execute("delete from Agents where property_id=%s",agent)
        agent_view.delete(agent)
        agent=None
        delete_agent_button.configure(state=DISABLED,bootstyle=DISABLED)
    def select_agent():
        global agent
        selected=agent_view.selection()
        item=agent_view.identify_row(event.y)
        if item not in selected:
            agent=item
            agent_view.selection_remove(*selected)
            agent_view.selection_add(item)
            delete_agent_button.configure(state=NORMAL,bootstyle=OUTLINE)
        else:
            agent=None
            agent_view.selection_remove(item)
            delete_agent_button.configure(state=DISABLED,bootstyle=DISABLED)
        return 'break'
    def agent_back():
        new_agent.pack_forget()
        see_agents.pack(expand=True,fill='both')
        query_agent(None)
    def go_new_agent():
        see_agents.pack_forget()
        new_agent.pack(expand=True,fill='both')
    def query_agent(_):
        searched=agent_entry.get()
        cursor=database.cursor()
        agent_view.delete(*agent_view.get_children())
        cursor.execute(f'select * from Agents where name like "%{searched}%" or phone like "%{searched}%" or email like "%{searched}%";')
        for agent_id,name,phone,email in cursor.fetchall():
            agent_view.insert("",END,iid=agent_id,values=(name,phone,email))
    #agent tab
    (see_agents:=Frame(agent_tab)).pack(expand=True,fill='both')
    see_agents.rowconfigure(2,weight=3)
    see_agents.columnconfigure(1,weight=4)
    Button(see_agents,text='New',command=go_new_agent,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (delete_agent_button:=Button(see_agents,text='Delete',command=remove_agent,state=DISABLED,bootstyle=DISABLED)).grid(row=0,column=1,sticky='NW')
    Label(see_agents,text='Search :').grid(row=1,column=0,sticky='E')
    (agent_entry:=Entry(see_agents)).grid(row=1,column=1,sticky='NSEW')
    agent_entry.bind('<KeyRelease>',query_agent)
    (agent_scroll:=Scrollbar(see_agents,bootstyle=INFO)).grid(row=2,column=2,sticky='NSEW')
    (agent_view:=Treeview(see_agents,column=('c1','c2','c3'),show='headings',selectmode='browse',bootstyle=INFO,xscrollcommand=agent_scroll.set)).grid(row=2,column=0,columnspan=2,sticky='NSEW')
    agent_view.column('0',anchor='e')
    agent_view.heading('0',text='Name')
    agent_view.column('1',anchor='w')
    agent_view.heading('1',text='Phone')
    agent_view.column('2',anchor='w')
    agent_view.heading('2',text='Email')
    agent_scroll.configure(command=agent_view.yview)
    agent_view.bind('<Button-1>',select_agent)
    query_agent(None)
    #new agent
    new_agent=Frame(agent_tab)
    Button(new_agent,text='<-',command=agent_back,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (err_label_agent:=Label(new_agent,text='',bootstyle=DANGER)).grid(row=0,column=1,sticky='NSEW')
    Label(new_agent,text='Name :').grid(row=1,column=0,sticky='E')
    (name_entry_agent:=Entry(new_agent)).grid(row=1,column=1,sticky='W')
    Label(new_agent,text='Phone :').grid(row=2,column=0,sticky='E')
    (phone_entry_agent:=Entry(new_agent)).grid(row=2,column=1,sticky='W')
    Label(new_agent,text='Email :').grid(row=3,column=0,sticky='E')
    (email_entry_agent:=Entry(new_agent)).grid(row=3,column=1,sticky='W')
    Button(new_agent,text='Add',command=add_agent).grid(row=4,columnspan=2,sticky='NSEW')
    #transaction rab
    def sell():
        global agent
        for tab in range(3):tabs.tab(tab,state=DISABLED)
        cursor=database.cursor()
        if client and property_:
            cursor.execute(f'select address,price,agent_id,sold from Properties where property_id={property_}')
            address,amount,agent,sold=cursor.fetchall()[0]
            cursor.execute(f'select name from Agents where agent_id={agent}')
            agent_name=cursor.fetchall()[0][0]
            cursor.execute(f'select name from Clients where client_id={client}')
            client_name=cursor.fetchall()[0][0]
            confirm_transaction.configure(state=DISABLED)
            transaction_display.configure(bootstyle=NORMAL,text=f'''
Amount : ₹{amount} only
From : {client_name}
[Id: {client}]
To : {agent_name}
[Id: {agent}]
Property : {'NA' if sold else address}
[Id: {property_}]
            ''')
        elif property_:
            cursor.execute(f'select address,price,agent_id from Properties where property_id={property_}')
            address,amount,agent=cursor.fetchall()[0]
            cursor.execute(f'select name from Agents where agent_id={agent}')
            agent_name=cursor.fetchall()[0][0]
            confirm_transaction.configure(state=DISABLED)
            transaction_display.configure(bootstyle=WARNING,text=f'''
Amount : ₹{amount} only
From : *
[Id: to be selected]
To : to be selected
[Id: {agent}]
Property : {address}
[Id: {property_}]
            ''');
        elif client:
            cursor.execute(f'select name from Clients where client_id={client}')
            client_name=cursor.fetchall()[0][0]
            confirm_transaction.configure(state=DISABLED)
            transaction_display.configure(bootstyle=WARNING,text=f'''
Amount : to be selected
From : {client_name}
[Id: {client}]
To : to be selected
[Id: to be selected]
Property : *
[Id: to ne selected]
            ''')
        else:
            confirm_transaction.configure(state=DISABLED)
            transaction_display.configure(bootstyle=WARNING,text=f'Property and Client not selected')
        see_transactions.pack_forget()
        new_transaction.pack(expand=True,fill='both')
    def transaction_back():
        new_transaction.pack_forget()
        see_transactions.pack(expand=True,fill='both')
        for tab in range(4):tabs.tab(tab,state=NORMAL)
    def query_transaction(_):
        searched=transactions_entry.get()
        cursor=database.cursor()
        transaction_view.delete(*transaction_view.get_children())
        cursor.execute(f'select transaction_id,Clients.name,Agents.name,Properties.address,price,transaction_date from Transactions join Clients on Clients.client_id=Transactions.buyer_id join Properties on Properties.property_id=Transactions.property_id join Agents on Properties.agent_id=Agents.agent_id where Clients.name like "%{searched}%" or Agents.name like "%{searched}%" or Properties.address like "%{searched}%" order by transaction_id;')
        for transaction_id,agent_name,client_name,address,amount,transaction_date in cursor.fetchall():
            transaction_view.insert("",END,iid=transaction_id,values=(transaction_id,agent_name,client_name,address,amount,transaction_date))
    def perform_transaction():
        pass
    (see_transactions:=Frame(transaction_tab)).pack(expand=True,fill='both')
    see_transactions.rowconfigure(2,weight=3)
    see_transactions.columnconfigure(1,weight=4)
    Button(see_transactions,text='New',command=sell,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    Label(see_transactions,text='Search :').grid(row=1,column=0,sticky='E')
    (transactions_entry:=Entry(see_transactions)).grid(row=1,column=1,sticky='NSEW')
    transactions_entry.bind('<KeyRelease>',query_transaction)
    (transaction_scroll:=Scrollbar(see_transactions,bootstyle=INFO)).grid(row=2,column=2,sticky='NSEW')
    (transaction_view:=Treeview(see_transactions,column=('c1','c2','c3','c4','c5','c6'),show='headings',selectmode='browse',bootstyle=INFO,xscrollcommand=transaction_scroll.set)).grid(row=2,column=0,columnspan=2,sticky='NSEW')
    transaction_view.column('0',anchor='e')
    transaction_view.heading('0',text='Id')
    transaction_view.column('1',anchor='w')
    transaction_view.heading('1',text='From')
    transaction_view.column('2',anchor='w')
    transaction_view.heading('2',text='To')
    transaction_view.column('3',anchor='w')
    transaction_view.heading('3',text='For')
    transaction_view.column('4',anchor='w')
    transaction_view.heading('4',text='Amount')
    transaction_view.column('5',anchor='w')
    transaction_view.heading('5',text='Date')
    transaction_scroll.configure(command=transaction_view.yview)
    transaction_view.bind('<Button-1>',select_client)
    query_transaction(None)
    #new transaction
    (new_transaction:=Frame(transaction_tab))
    Button(new_transaction,text='<-',command=transaction_back,bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    (transaction_display:=Label(new_transaction)).grid(column=1,row=1)
    (confirm_transaction:=Button(new_transaction,text='Confirm',command=perform_transaction)).grid(column=0,row=2)
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
