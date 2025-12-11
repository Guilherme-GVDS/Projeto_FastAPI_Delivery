from pydantic import BaseModel
from typing import Optional, List

class UserSchema(BaseModel):
    name: str
    phone_number: str
    email: str
    password: str
    admin: Optional[bool]
    
    class Config:
        from_attributes = True
        
class OrderSchema(BaseModel):
    id_user: int

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True    

class ItemOrderSchema(BaseModel):
    item: str
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True    

class ResponseOrderSchema(BaseModel):
    id: int
    status: str
    price: float
    items: List[ItemOrderSchema]

    class Config:
        from_attributes = True  