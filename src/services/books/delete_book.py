from src.repos.books.books_repo import get_book_by_id, delete_book as repo_delete_book
from src.core.logging import logger

class NotFoundException(Exception):
    pass

class DBException(Exception):
    pass

def delete_book(book_id: str, db):
    try:
        book = get_book_by_id(book_id, db)
        if not book:
            logger.warning(f"Book not found with id: {book_id}")
            raise NotFoundException(f"Book not found with id: {book_id}")

        repo_delete_book(book, db)
        logger.info(f"Successfully deleted book with id: {book_id}")
        return {"message": "Book deleted successfully"}
    except NotFoundException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete book: {e}")
        raise DBException("Failed to delete book from DB") from e
