from src.repos.books.books_repo import get_all_books as repo_get_all_books
from src.core.logging import logger

# Exceptions Class 
class DBException(Exception):
    pass
def get_all_books(db):
    try: 
        books = repo_get_all_books(db_session=db)
        return books
    except Exception as e: 
        logger.error(e)
        raise DBException("Failed to fetch books from DB") from e
