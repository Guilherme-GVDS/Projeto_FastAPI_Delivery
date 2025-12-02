from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    phone_number: str
    email: str
    password: str
    admin: Optional[bool]
    
    class Config:
        from_attributes = True