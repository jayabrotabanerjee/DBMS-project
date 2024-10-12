#!/bin/python
from faker import Faker
from random import randint,uniform,shuffle
from numpy.random import choice
from datetime import datetime
from key import db
cursor=db.cursor()
fake=Faker('en_IN').unique
#create agents
agents=randint(5,10)
for _ in range(agents):
    cursor.execute(
        "insert into Agents (name,phone,email) values (%s,%s,%s)",
        (fake.name(),fake.phone_number(),fake.email())
    )
db.commit()
#create properties
properties=randint(50,200)
available=list()
for property_id in range(randint(50,200)):
    cursor.execute(
        "insert into Properties (agent_id,address,price,area,description,listing_date,sold) values (%s,%s,%s,%s,%s,%s,%s);",
        (
            randint(1,agents-1),
            fake.address().replace('\n',' '),
            round(uniform(200000,2000000),2),
            round(uniform(100,2000),2),
            choice((f'{randint(1,6)}BHK','Land','Orchard',f'{randint(2,6)} story')),
            datetime.utcfromtimestamp(listed_at:=randint(1381048278,1728223285)).strftime('%Y-%m-%d'),
            str(sold:=choice((1,0),p=(0.8,0.2)))
        )
    )
    if sold:available.append((property_id,listed_at))
#creat clients
clients=randint(20,50)
for _ in range(clients):
    cursor.execute(
        "insert into Clients (name,phone,email) value (%s,%s,%s);",
        (fake.name(),fake.phone_number(),fake.email())
    )
db.commit()
#create transactions
shuffle(available)
for property_id,listed_at in available:
    cursor.execute(
        "insert into Transactions (property_id,transaction_date,buyer_id) values (%s,%s,%s);",
        (
            property_id,
            datetime.utcfromtimestamp(randint(listed_at,1728223285)).strftime('%Y-%m-%d'),
            randint(0,clients)
        )
    )
db.commit()
