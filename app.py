#!/bin/python
from ttkbootstrap import Window,Label,Entry,Button,Notebook,Frame,Checkbutton,Treeview,Scrollbar,END,DoubleVar,IntVar
from ttkbootstrap.constants import WARNING,DANGER,OUTLINE,SECONDARY,INFO
from RangeSlider.RangeSlider import RangeSliderH
from mysql.connector import connect
from mysql.connector.errors import DatabaseError,ProgrammingError
app=Window(title='Login',resizable=(False,False))
#Main Window
def main_app(database):
    app.title('Listings')
    (tabs:=Notebook(app)).pack(expand=True,fill='both')
    tabs.add(property_tab:=Frame(tabs),text='Properties')
    tabs.add(client_tab:=Frame(tabs),text='Clients')
    tabs.add(agent_tab:=Frame(tabs),text='Agents')
    tabs.add(transaction_tab:=Frame(tabs),text='Transaction')
    #property tab
    def query():
        result_view.delete(*result_view.get_children())
        cursor=database.cursor()
        cursor.execute(f'select property_id,address,price,description,area from Properties where address like "%{location_entry.get()}%" and description like "%{description_entry.get()}%" and area between {round(min_area.get()*1900+100,2)} and {round(max_area.get()*1900+100,2)} and price between {round(min_area.get()*1800000+200000,2)} and {round(max_area.get()*1800000+200000,2)} order by area,price;')
        for item_id,address,price,description,area in cursor.fetchall():
            result_view.insert("",END,iid=str(item_id),values=(address,description,str(area),str(price)))
    Button(property_tab,text='New',bootstyle=OUTLINE).grid(row=0,column=0,sticky='NW')
    Label(property_tab,text='Location :').grid(row=1,column=0,sticky='E')
    (location_entry:=Entry(property_tab)).grid(row=1,column=1,sticky='NSEW')
    Label(property_tab,text='Type :').grid(row=2,column=0,sticky='E')
    (description_entry:=Entry(property_tab)).grid(row=2,column=1,sticky='W')
    Label(property_tab,text='Price :').grid(row=3,column=0,sticky='E')
    min_price=DoubleVar(value=0.0);max_price=DoubleVar(value=1.0)
    (price_slider:=RangeSliderH(property_tab,[min_price,max_price],padX=12,show_value=False)).grid(row=3,column=1,sticky='W')
    (price_label:=Label(property_tab,text='₹ 2 - 20 Lakh')).grid(row=4,column=1,sticky='NSEW')
    price_change=lambda _,__,___:price_label.configure(text=f'₹ {round(min_price.get()*18+2,2)} - {round(max_price.get()*18+2,2)} Lakh')
    min_price.trace_add('write',price_change)
    max_price.trace_add('write',price_change)
    Label(property_tab,text='Area :').grid(row=5,column=0,sticky='E')
    min_area=DoubleVar(value=0.0);max_area=DoubleVar(value=1.0)
    (area_slider:=RangeSliderH(property_tab,[min_area,max_area],padX=12,show_value=False)).grid(row=5,column=1,sticky='W')
    (area_label:=Label(property_tab,text='100 - 2000 sq feet')).grid(row=6,column=1,sticky='NSEW')
    area_change=lambda _,__,___:area_label.configure(text=f'{round(min_area.get()*1900+100,2)} - {round(max_price.get()*1900+100,2)} sq feet')
    min_area.trace_add('write',area_change)
    max_area.trace_add('write',area_change)
    available=IntVar(property_tab,value=1)
    Checkbutton(property_tab,text='Show Available',variable=available,onvalue=1,offvalue=0,state='selected',bootstyle=SECONDARY).grid(row=6,column=1,sticky='E')
    Button(property_tab,text='Find',command=query).grid(row=7,column=1,sticky='E')
    (scroll:=Scrollbar(property_tab,bootstyle=INFO)).grid(row=8,column=2,sticky='NSEW')
    (result_view:=Treeview(property_tab,column=('c1','c2','c3','c4'),show='headings',bootstyle=INFO,xscrollcommand=scroll.set)).grid(row=8,column=0,columnspan=2,sticky='NSEW')
    result_view.column('0',anchor='e')
    result_view.heading('0',text='Location')
    result_view.column('1',anchor='w')
    result_view.heading('1',text='Description')
    result_view.column('2',anchor='w')
    result_view.heading('2',text='Area (sq feet)')
    result_view.column('3',anchor='w')
    result_view.heading('3',text='Price (₹)')
    scroll.configure(command=result_view.yview)
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
