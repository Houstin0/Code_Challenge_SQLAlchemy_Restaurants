from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant,Customer

fake=Faker()

if __name__=='__main__':

    engine=create_engine('sqlite:///restaurants.db')
    Session=sessionmaker(bind=engine)
    session=Session()
    
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.commit()

    print("seeding.....")

    restaurants=[]
    for i in range(20):
        restaurant=Restaurant(
            name=fake.name(),
            price=fake.pyint()
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)
    
    customers=[]
    for i in range(50):
        customer=Customer(
            first_name=fake.name(),
            last_name=fake.name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)