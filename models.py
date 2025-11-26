from sqlalchemy import create_engine , Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base


#Criar conexão
db = create_engine('sqlite:///banco.db')

#Criar base DB  
Base = declarative_base()

#Tabelas DB

class User (Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    phone_number = Column('phone_number', Integer, nullable=False)
    email = Column('email', String, nullable=False)
    password = Column('password', String, nullable=False)
    admin = Column('admin', Boolean, default = False)

    def __init__(self, name, phone_number, email, password, admin = False):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.admin = admin

class Order(Base):
    __tablename__ = 'orders'

    '''    order_status = {
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado'),
        ('Entregue', 'Entregue')
    }'''

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String)
    user = Column('user', ForeignKey('users.id'))
    price = Column('price', Float)
    #items

    def __init__ (self, user, status = 'Pendente', price=0):
        self.user = user
        self.status = status
        self.price = price

class Item(Base):
    __tablename__ = 'items'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String)
    unit_price = Column('unit_price', Float)

    def __init__ (self, item, unit_price):
        self.item = item
        self.unit_price= unit_price