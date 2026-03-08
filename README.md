# LibGo - Library Management System

LibGo is a powerful Library Management System built with FastAPI, designed to manage library transactions efficiently and effectively. It provides a RESTful API for managing books, including their metadata such as titles, authors, page counts, reviews, and likes.

## Tech Stack

- **Framework**: FastAPI (async Python web framework)
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Database**: SQLite (file-based: `books.db`)
- **Server**: Uvicorn (ASGI server)
- **Data Validation**: Pydantic

## Project Structure

```
LibGo/
├── main.py                          # FastAPI application entry point
├── pyproject.toml                   # Project configuration & dependencies
├── .gitignore                       # Git ignore patterns
├── books.db                         # SQLite database file
└── src/
    ├── db.py                        # Database engine, session, and table creation
    ├── core/
    │   ├── config.py                # Application configuration (placeholder)
    │   └── logging.py               # Custom logging utility
    ├── schema/
    │   └── BooksSchema.py           # Pydantic schemas for request/response validation
    ├── api/v1/
    │   └── books.py                  # API router with book endpoints
    ├── services/books/
    │   └── get_all_books.py          # Business logic layer for books
    └── repos/books/
        └── books_repo.py             # Data access layer with Book model and CRUD
```

## Key Components

### `main.py`
- FastAPI application setup with lifespan event handler
- Creates database tables on startup
- Registers the books router at `/books` prefix
- Runs on `http://127.0.0.1:8000`

### Database (`src/db.py`)
- SQLite database connection using SQLModel
- Session management for database operations
- Automatic table creation via SQLModel metadata

### Models & Schemas (`src/repos/books/books_repo.py`, `src/schema/BooksSchema.py`)
- **Book Model**: UUID primary key, title, author, pages_count, reviews (JSON), likes (JSON)
- **BooksCreate**: Schema for creating new books
- **BookResponse**: Schema for book responses

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/get-all-books` | Retrieve all books from the library |
| GET | `/` | Root endpoint - Welcome message |

## Installation & Setup

1. **Create and activate virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r pyproject.toml
   # Or using uv:
   # uv sync
   ```

3. **Run the application**:
   ```bash
   python main.py
   # Or:
   # uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

4. **Access the API**:
   - API docs: `http://127.0.0.1:8000/docs`
   - Alternative docs: `http://127.0.0.1:8000/redoc`

## Current Features

- **Get All Books**: Retrieves a list of all books in the database with their complete information including UUID, title, author, page count, reviews, and likes.

## Development Notes

- The project follows a layered architecture: API → Service → Repository
- Custom logging is implemented via `src/core/logging.py`
- Database tables are automatically created on application startup
- UUID is used for unique book identifiers

## Future Enhancements

Potential improvements for the project:
- Complete CRUD operations (Create, Read, Update, Delete books)
- User authentication and authorization
- Book borrowing/return functionality
- Advanced search and filtering
- Pagination for book listings
- Input validation enhancements
