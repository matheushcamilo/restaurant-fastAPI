from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class Client(BaseModel):
    first_name: str
    last_name: str
    gender: Gender 