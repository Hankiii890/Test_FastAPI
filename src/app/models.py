from pydantic import BaseModel


class DataInput(BaseModel):
    phone: str
    address: str
