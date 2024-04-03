# Определение класса DataInput
from pydantic import BaseModel


class DataInput(BaseModel):
    phone: str
    address: str
