from fastapi import APIRouter, Depends
from src.internal_api.services.books.get_all_books import get_all_books as service_get_all_books
from src.internal_api.services.books.add_book import add_book as service_add_book
from src.internal_api.services.books.update_book import (
    update_book as service_update_book,
    NotFoundException,
)
from src.internal_api.services.books.delete_book import (
    delete_book as service_delete_book,
    NotFoundException as DeleteNotFoundException,
)
from uuid import UUID
from fastapi.responses import JSONResponse
from src.internal_api.schema.BooksSchema import BooksCreate, BooksUpdate, BookResponse
from fastapi import HTTPException
from src.core.logging import logger
from src.db import get_session

books_router = APIRouter()


@books_router.get("/get-all-books", response_model=list[BookResponse], status_code=200)
def get_all_books(db=Depends(get_session)):
    try:
        books = service_get_all_books(db)
        logger.info(msg="Sucessfully fetched all books")
        return books
    except Exception as e:
        logger.warning(msg=f"Something went wrong {e}")
        return HTTPException(detail="Internal Server Error", status_code=500)


@books_router.post("/add-book", response_model=BookResponse, status_code=201)
def add_book(book_data: BooksCreate, db=Depends(get_session)):
    try:
        book = service_add_book(book_data, db)
        logger.info(msg="Successfully created book")
        return book
    except Exception as e:
        logger.warning(msg=f"Something went wrong {e}")
        return HTTPException(detail="Internal Server Error", status_code=500)


@books_router.put("/update-book/{book_id}", response_model=BookResponse)
def update_book(book_id: str, book_data: BooksUpdate, db=Depends(get_session)):
    try:
        book = service_update_book(UUID(book_id), book_data, db)
        logger.info(msg=f"Successfully updated book with id: {book_id}")
        return book
    except NotFoundException as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(msg=f"Something went wrong {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@books_router.delete("/delete-book/{book_id}", status_code=204)
def delete_book(book_id: str, db=Depends(get_session)):
    try:
        service_delete_book(UUID(book_id), db)
        logger.info(msg=f"Successfully deleted book with id: {book_id}")
        return JSONResponse(
            content={"message": "Book deleted successfully"}, status_code=200
        )
    except DeleteNotFoundException as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(msg=f"Something went wrong {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)
