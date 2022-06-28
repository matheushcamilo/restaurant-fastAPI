from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    description: str

class Order(OrderBase):
    client_id: Optional[int]

class OrderResponseModel(OrderBase):
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
    orders: List[OrderResponseModel]

    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class LoginResponseModel(BaseModel):
    first_name: str
    last_name: str
    email: str   

class Token(BaseModel):
    access_token: str
    token_type: str    

class TokenData(BaseModel):
    email: Optional[str] = None    