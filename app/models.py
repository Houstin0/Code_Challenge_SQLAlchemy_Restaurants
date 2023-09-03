from sqlalchemy import Column,Integer,String,MetaData
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Restaurant:
    __tablename__='restaurants'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    price=Column(Integer())

class Customer:
    __tablename__='customers'

    id=Column(Integer(),primary_key=True)
    first_name=(String())
    last_name=(String())    