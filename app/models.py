from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine('sqlite:///restaurants.db')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

restaurant_customer=Table(
    'restaurant_customers',
    Base.metadata,
    Column('restaurant_id',ForeignKey('restaurants.id'),primary_key=True),
    Column('customer_id',ForeignKey('customers.id'),primary_key=True),
    extend_existing=True
)

class Restaurant(Base):
    __tablename__='restaurants'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    price=Column(Integer())
    reviews=relationship('Review',backref=backref('restaurant'))
    customers=relationship('Customer',secondary=restaurant_customer,back_populates='restaurants')

    def __repr__(self):
        return f'Restaurant Name: {self.name} Price: {self.price}'
    
    def restaurant_reviews(self):
        return self.reviews 

    def restaurant_customers(self):
         return[review.customer for review in self.reviews]
        


class Customer(Base):
    __tablename__='customers'

    id=Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    reviews=relationship('Review',backref=backref('customer'))
    restaurants=relationship('Restaurant',secondary=restaurant_customer,back_populates='customers')

    def __repr__(self):
        return f'First Name: {self.first_name} Last Name {self.last_name}'

    def customer_reviews(self):
        return self.reviews
    
    def customer_restaurants(self):
        return [review.restaurant for review in self.reviews]
    
    def customer_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def customer_favor

class Review(Base):
    __tablename__='reviews'

    id=Column(Integer(),primary_key=True)
    comment=Column(String())
    star_rating=Column(Integer())
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))
    customer_id=Column(Integer(),ForeignKey('customers.id'))

    def __repr__(self):
        return f'Review: {self.comment} star_rating {self.star_rating}'  
    
    def review_customer(self):
        return self.customer
    
    def Review_restaurant(self):
        return self.restaurant