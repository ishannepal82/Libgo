from fastapi import APIRouter, Depends
from time import time
from src.services.books.get_all_books import get_all_books as service_get_all_books
from fastapi.responses import JSONResponse
from src.schema.BooksSchema import BooksCreate, BookResponse, BaseBookModel
from typing import List 
from src.core.logging import logger
from src.db import get_session

books_router = APIRouter()

@books_router.get('/get-all-books')
def get_all_books(db = Depends(get_session)) -> JSONResponse:
    try: 
        books = service_get_all_books(db)
        logger.info(msg="Sucessfully fetched all books")
        return JSONResponse(content=books, status_code=200)
    except Exception as e:
        logger.warning(msg=f"Something went wrong {e}")
        return JSONResponse(content="Internal Server Error", status_code=500)
     
