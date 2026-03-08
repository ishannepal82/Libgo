from typing import List
from uuid import UUID
from pydantic import BaseModel

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

class BookResponse(BaseBookModel):
    pass 
