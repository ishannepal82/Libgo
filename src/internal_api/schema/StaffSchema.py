from pydantic import BaseModel, ConfigDict
from typing import Literal
from uuid import UUID

class CreateStaff(BaseModel):
    name: str
    email: str 
    role: Literal["Admin", "Librarian", "Staff"] 
    hashed_password: str
    code: str 
    phone: str 
    is_admin: bool

class BaseStaff(BaseModel):
    id: UUID
    name: str
    email: str 
    role: Literal["Admin", "Librarian", "Staff"] 
    hashed_password: str
    code: str 
    phone: str 
    is_admin: bool


class StaffResponse(BaseStaff):
    model_config = ConfigDict(from_attributes=True)