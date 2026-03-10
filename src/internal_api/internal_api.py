from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn 

from src.internal_api.api.v1.books import books_router
from src.internal_api.api.v1.write_email import email_router

from src.db import create_all_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_tables()
    yield

app = FastAPI(title="LibGo", 
              version="1.0", 
              debug=True, 
              description="A powerful Library management system to manage the transactions of library effiiently and effectively",
              lifespan=lifespan)

app.include_router(books_router, prefix="/books", tags=['books', 'burrow', 'add'])

app.include_router(email_router, prefix="/email", tags=['email', 'send'])


@app.get("/")
async def root():
    return {"message": "Welcome to LibGo API!"}

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)

