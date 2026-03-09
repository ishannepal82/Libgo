from typing import List
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class BaseBookModel(BaseModel):
    id: UUID
    title: str
    author: str
    pages_count: int
    reviews: list[dict]
    likes: list[int]


class BooksCreate(BaseModel):
    title: str
    author: str
    pages_count: int

    model_config = ConfigDict(from_attributes=True)


class BooksUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    pages_count: int | None = None

    model_config = ConfigDict(from_attributes=True)


class BookResponse(BaseBookModel):
    pass
