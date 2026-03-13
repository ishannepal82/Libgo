from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional


class Library(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    address: str
    owner_id: str
