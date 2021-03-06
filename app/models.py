from .database import Base
from sqlalchemy import Column, String, Integer, UniqueConstraint, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = 'clients'

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name'),
      )

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    email = Column(EmailType)
    password = Column(String)

    orders = relationship('Order', back_populates='client')

class Order(Base):
  __tablename__ = 'orders'

  id = Column(Integer, primary_key=True, index=True)
  description = Column(String)
  client_id = Column(Integer, ForeignKey('clients.id'))

  client = relationship('Client', back_populates='orders')




