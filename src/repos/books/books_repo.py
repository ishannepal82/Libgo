from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional
from uuid import UUID, uuid4

class Book(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    author: str
    pages_count: int
    reviews: list = Field(sa_column=Column(JSON))
    likes: list = Field(sa_column=Column(JSON))



# CRUD Operations 
def create_book(book: Book, db_session): 
    db_session.add(book)   
    db_session.commit()
    db_session.refresh(book)
    # What does the refresh does?
    # The refresh method is used to update the state of the book object with the latest data from the database after it has been committed. This is particularly useful when the database generates values for certain fields (like auto-incrementing IDs or timestamps) that are not known until after the commit. By calling refresh, you ensure that the book object reflects any changes made by the database, such as assigned IDs or updated timestamps. 
    return book

def get_all_books(db_session):
    books = db_session.query(Book).all()
    return books 