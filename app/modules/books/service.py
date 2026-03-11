from app.modules.books.models import (
    get_all_books as repo_get_all_books,
    create_book as repo_create_book,
    Book,
    get_book_by_id as repo_get_book_by_id,
    update_book as repo_update_book,
    delete_book as repo_delete_book,
)
from app.core.security import logger
from app.modules.books.schemas import BooksCreate, BooksUpdate
from uuid import UUID


class DBException(Exception):
    pass


def get_all_books(db):
    try:
        books = repo_get_all_books(db_session=db)
        return books
    except Exception as e:
        logger.error(str(e))
        raise DBException("Failed to fetch books from DB") from e


class NotFoundException(Exception):
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


def update_book(book_id: UUID, book_data: BooksUpdate, db):
    try:
        book = repo_get_book_by_id(book_id, db)
        if not book:
            logger.warning(f"Book not found with id: {book_id}")
            raise NotFoundException(f"Book not found with id: {book_id}")

        update_data = book_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(book, field, value)

        updated_book = repo_update_book(book, db)
        logger.info(f"Successfully updated book with id: {book_id}")
        print(updated_book)
        return updated_book
    except NotFoundException:
        raise
    except Exception as e:
        logger.error(f"Failed to update book: {e}")
        raise DBException("Failed to update book in DB") from e


class DeleteNotFoundException(Exception):
    pass


def delete_book(book_id: UUID, db):
    try:
        book = repo_get_book_by_id(book_id, db)
        if not book:
            logger.warning(f"Book not found with id: {book_id}")
            raise DeleteNotFoundException(f"Book not found with id: {book_id}")

        repo_delete_book(book, db)
        logger.info(f"Successfully deleted book with id: {book_id}")
        return {"message": "Book deleted successfully"}
    except Exception as e:
        logger.error(f"Failed to delete book: {e}")
        raise DBException("Failed to delete book from DB") from e
