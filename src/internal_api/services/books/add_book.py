from src.internal_api.repos.books.books_repo import (create_book as repo_create_book, Book)
from src.core.logging import logger
from src.internal_api.schema.BooksSchema import BooksCreate

class DBException(Exception):
    pass

def add_book(book_data: BooksCreate, db):
    try:
        new_book = Book(
            title=book_data.title,
            author=book_data.author,
            pages_count=book_data.pages_count,
            reviews=[],
            likes=[],
        )
        created_book = repo_create_book(book=new_book, db_session=db)
        logger.info(f"Successfully created book with id: {created_book.id}")
        return created_book
    except Exception as e:
        logger.error(f"Failed to create book: {e}")
        raise DBException("Failed to create book in DB") from e
