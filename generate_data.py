#!/bin/python
from faker import Faker
from random import randint,uniform,choice
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
for _ in range(50,100):
    cursor.execute(
        "insert into Properties (agent_id,address,price,area,description,listing_date) values (%s,%s,%s,%s,%s,%s)",
        (
            randint(1,agents-1),
            fake.address(),
            round(uniform(200000,2000000),2),
            round(uniform(100,2000),2),
            choice((f'{randint(1,6)}BHK','Land','Orchard',f'{randint(2,6)} story')),
            datetime.utcfromtimestamp(randint(1381048278,1728223285)).strftime('%Y-%m-%d')
        )
    )
db.commit()
