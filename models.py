from sqlalchemy import create_engine , Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


#Criar conexão
db = create_engine('sqlite:///banco.db')

#Criar base DB  
Base = declarative_base()

#Tabelas DB

class User (Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    phone_number = Column('phone_number', String, nullable=False)
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

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String)
    user = Column('user', ForeignKey('users.id'))
    price = Column('price', Float)
    items = relationship('ItemOrder', cascade='all, delete')

    def __init__ (self, user, status = 'Pendente', price=0):
        self.user = user
        self.status = status
        self.price = price

    def calc_price(self):
        self.price = sum(item.unit_price * item.quantity for item in self.items)

class ItemOrder(Base):
    __tablename__ = 'items_order'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String)
    quantity = Column('quantity', Integer)
    unit_price = Column('unit_price', Float)
    order = Column('order', ForeignKey('orders.id'))


    def __init__ (self, item, unit_price, quantity, order):
        self.item = item
        self.unit_price= unit_price
        self.quantity = quantity
        self.order = order