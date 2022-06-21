from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class Client(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender 