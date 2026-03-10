from pydantic import BaseModel, ConfigDict
from typing import Literal
from uuid import UUID

class StaffRegister(BaseModel):
    name: str
    email: str 
    role: Literal["Admin", "Librarian", "Staff"] 
    password: str
    code: str 
    phone: str 
    is_admin: bool

class StaffLogin(BaseModel):
    email: str 
    password: str 

class StaffUpdate(BaseModel):
    name: str | None = None
    email: str | None = None 
    role: Literal["Admin", "Librarian", "Staff"] | None = None 
    password: str | None = None
    code: str | None = None 
    phone: str | None = None 
    is_admin: bool | None = None

class BaseStaff(BaseModel):
    id: UUID
    name: str
    email: str 
    role: Literal["Admin", "Librarian", "Staff"] 
    password: str
    code: str 
    phone: str 
    is_admin: bool


class StaffResponse(BaseStaff):
    model_config = ConfigDict(from_attributes=True)