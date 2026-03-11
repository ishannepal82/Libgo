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


def create_book(book: Book, db_session):
    db_session.add(book)
    db_session.commit()
    db_session.refresh(book)
    return book


def get_all_books(db_session):
    books = db_session.query(Book).all()
    return books


def get_book_by_id(book_id: UUID, db_session):
    book = db_session.query(Book).filter(Book.id == book_id).first()
    return book


def update_book(book: Book, db_session):
    db_session.commit()
    db_session.refresh(book)
    return book


def delete_book(book: Book, db_session):
    db_session.delete(book)
    db_session.commit()
