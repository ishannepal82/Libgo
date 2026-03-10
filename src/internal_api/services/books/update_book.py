from src.internal_api.repos.books.books_repo import get_book_by_id, update_book as repo_update_book
from src.core.logging import logger
from src.internal_api.schema.BooksSchema import BooksUpdate


class NotFoundException(Exception):
    pass


class DBException(Exception):
    pass


def update_book(book_id: str, book_data: BooksUpdate, db):
    try:
        book = get_book_by_id(book_id, db)
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
