from sqlalchemy import Column,Integer,String,MetaData
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Restaurant(Base):
    __tablename__='restaurants'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    price=Column(Integer())

class Customer(Base):
    __tablename__='customers'

    id=Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())    
