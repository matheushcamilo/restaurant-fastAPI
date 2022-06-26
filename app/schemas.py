import email
from enum import Enum
from typing import List
from pydantic import BaseModel


class Order(BaseModel):
    description: str

class OrderResponseModel(Order):
    class Config:
        orm_mode = True

class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class Client(BaseModel):
    first_name: str = 'First Name'
    last_name: str = 'Last Name'
    gender: Gender = 'Your gender'
    email: str = 'example@example.com'
    password: str = ''

class ClientResponseModel(BaseModel):
    first_name: str
    last_name: str
    gender: str
    email: str

    class Config:
        orm_mode = True
