from enum import Enum
from typing import List
from pydantic import BaseModel


class Order(BaseModel):
    description: str

class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class Client(BaseModel):
    first_name: str
    last_name: str
    gender: Gender