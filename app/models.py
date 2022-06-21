from .database import Base
from sqlalchemy import Column, String, Integer, UniqueConstraint

class Client(Base):
    __tablename__ = 'clients'

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name'),
      )

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)



