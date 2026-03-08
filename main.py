from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.api.v1.books import books_router

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

@app.get("/")
async def root():
    return {"message": "Welcome to the Database Processing Engine API!"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000)

