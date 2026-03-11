from fastapi import APIRouter, Depends
from app.modules.books.service import (
    get_all_books as service_get_all_books,
    add_book as service_add_book,
    update_book as service_update_book,
    NotFoundException,
    delete_book as service_delete_book,
    DeleteNotFoundException,
)
from uuid import UUID
from fastapi.responses import JSONResponse
from app.modules.books.schemas import BooksCreate, BooksUpdate, BookResponse
from fastapi import HTTPException
from app.core.logger import logger
from app.db.session import get_session

books_router = APIRouter()


@books_router.get("/get-all-books", response_model=list[BookResponse], status_code=200)
def get_all_books(db=Depends(get_session)):
    try:
        books = service_get_all_books(db)
        logger.info(message="Sucessfully fetched all books")
        return books
    except Exception as e:
        logger.warning(message=f"Something went wrong {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@books_router.post("/add-book", response_model=BookResponse, status_code=201)
def add_book(book_data: BooksCreate, db=Depends(get_session)):
    try:
        book = service_add_book(book_data, db)
        logger.info(msg="Successfully created book")
        return book
    except Exception as e:
        logger.warning(message=f"Something went wrong {e}")
        return HTTPException(detail="Internal Server Error", status_code=500)


@books_router.put("/update-book/{book_id}", response_model=BookResponse)
def update_book(book_id: UUID, book_data: BooksUpdate, db=Depends(get_session)):
    try:
        book = service_update_book(book_id, book_data, db)
        logger.info(message=f"Successfully updated book with id: {book_id}")
        return book
    except NotFoundException as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(message=f"Something went wrong: {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@books_router.delete("/delete-book/{book_id}", status_code=204)
def delete_book(book_id: str, db=Depends(get_session)):
    try:
        service_delete_book(UUID(book_id), db)
        logger.info(message=f"Successfully deleted book with id: {book_id}")
        return JSONResponse(
            content={"message": "Book deleted successfully"}, status_code=200
        )
    except DeleteNotFoundException as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(message=f"Something went wrong {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)
