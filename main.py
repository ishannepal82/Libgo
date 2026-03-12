from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from app.modules.books.router import books_router
from app.modules.email.router import email_router
from app.modules.auth.router import auth_router
from app.modules.staff.router import admin_router
from app.modules.chat.routes import chat_router

from app.db.session import create_all_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_tables()
    yield


app = FastAPI(
    title="LibGo",
    version="1.0",
    debug=True,
    description="A powerful Library management system to manage the transactions of library effiiently and effectively",
    lifespan=lifespan,
)

app.include_router(
    books_router, prefix="/books", tags=["books", "burrow", "add"]
    )

app.include_router(
    email_router, prefix="/email", tags=["email", "send"]
    )

app.include_router(
    auth_router, prefix="/auth", tags=["auth", "login", "register"]
    )

app.include_router(
    admin_router, prefix="/admin", tags=["admin", "staff", "remove", "edit"]
)

app.include_router(
    chat_router, prefix="/chat", tags=["chat", "messages"]
)


@app.get("/")
async def root():
    return {"message": "Welcome to LibGo API!"}




def main():
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
