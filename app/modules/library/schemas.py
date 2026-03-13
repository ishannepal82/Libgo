from pydantic import BaseModel, ConfigDict
from uuid import UUID


class LibraryCreate(BaseModel):
    name: str
    address: str

    model_config = ConfigDict(from_attributes=True)


class LibraryUpdate(BaseModel):
    name: str | None = None
    address: str | None = None

    model_config = ConfigDict(from_attributes=True)


class LibraryResponse(BaseModel):
    id: UUID
    name: str
    address: str
    owner_id: str

    model_config = ConfigDict(from_attributes=True)
