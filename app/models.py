from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref

Base=declarative_base()

class Restaurant(Base):
    __tablename__='restaurants'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    price=Column(Integer())
    reviews=relationship('Review',backref=backref('restaurant'))

    def __repr__(self):
        return f'Restaurant Name: {self.name}'
    
class Customer(Base):
    __tablename__='customers'

    id=Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    reviews=relationship('Review',backref=backref('customer'))

    def __repr__(self):
        return f'Customer first Name: {self.first_name}' 

class Review(Base):
    __tablename__='reviews'

    id=Column(Integer(),primary_key=True)
    comment=Column(String())
    star_rating=Column(Integer())
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))
    customer_id=Column(Integer(),ForeignKey('customers.id'))

    def __repr__(self):
        return f'Review: {self.comment}'  