# LibGo - Library Management System

LibGo is a powerful Library Management System built with FastAPI, designed to manage library transactions efficiently and effectively. It provides a RESTful API for managing books, staff, authentication, and email notifications.

## Tech Stack

- **Framework**: FastAPI (async Python web framework)
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Server**: Uvicorn (ASGI server)
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt

## Project Structure

```
LibGo/
├── main.py                          # Application entry point
├── pyproject.toml                   # Project configuration & dependencies
├── uv.lock                          # Locked dependencies
├── .env                             # Environment variables
├── Dockerfile                       # Docker configuration
├── .python-version                  # Python version
├── .gitignore                       # Git ignore patterns
├── books.db                         # SQLite database file
└── app/
    ├── main.py                      # FastAPI application setup
    ├── db/
    │   ├── __init__.py
    │   ├── base.py                  # SQLAlchemy base class
    │   └── session.py               # Database session & table creation
    ├── core/
    │   ├── __init__.py
    │   ├── config.py                # Application configuration
    │   └── security.py              # Security utilities & logging
    ├── dependencies/
    │   ├── __init__.py
    │   └── auth.py                  # Authentication dependency
    ├── utils/
    │   ├── __init__.py
    │   └── hash_password.py         # Password hashing utility
    └── modules/
        ├── __init__.py
        ├── auth/                    # Authentication module
        │   ├── models.py            # Staff/Admin models
        │   ├── schemas.py            # Pydantic schemas
        │   ├── router.py             # API endpoints
        │   └── service.py            # Business logic
        ├── books/                   # Books management module
        │   ├── models.py            # Book models
        │   ├── schemas.py           # Pydantic schemas
        │   ├── router.py            # API endpoints
        │   └── service.py           # Business logic
        ├── staff/                   # Staff management module
        │   ├── models.py
        │   ├── schemas.py
        │   ├── router.py
        │   └── service.py
        └── email/                   # Email notification module
            ├── router.py
            └── service.py
```

## Key Components

### `app/main.py`
- FastAPI application setup with lifespan event handler
- Registers all routers with appropriate prefixes
- Runs on `http://127.0.0.1:8000`

### Database (`app/db/`)
- SQLite database connection using SQLAlchemy
- Session management for database operations
- Automatic table creation on application startup

### Modules

| Module | Prefix | Description |
|--------|--------|-------------|
| Auth | `/auth` | Authentication (login, register) |
| Books | `/books` | Book CRUD operations |
| Staff | `/admin` | Staff management |
| Email | `/email` | Email notifications |

## API Endpoints

### Authentication (`/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/admin-login` | Admin login |
| POST | `/auth/staff-login` | Staff login |
| POST | `/auth/staff-register` | Register new staff |

### Books (`/books`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/get-all-books` | Retrieve all books |
| POST | `/books/add-book` | Add a new book |
| PUT | `/books/update-book/{book_id}` | Update a book |
| DELETE | `/books/delete-book/{book_id}` | Delete a book |

### Staff/Admin (`/admin`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/get-all-staff` | Retrieve all staff |
| PUT | `/admin/update-staff/{staff_id}` | Update staff details |
| DELETE | `/admin/delete-staff/{staff_id}` | Delete a staff member |

### Email (`/email`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/email/send` | Send email notification |

### General

| Method | Endpoint | Description |
|--------|----------|-------------|
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

3. **Configure environment variables**:
   Create a `.env` file with necessary variables (database URL, secret keys, etc.)

4. **Run the application**:
   ```bash
   python -m app.main
   # Or:
   # uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```

5. **Access the API**:
   - API docs: `http://127.0.0.1:8000/docs`
   - Alternative docs: `http://127.0.0.1:8000/redoc`

## Docker Support

Build and run with Docker:
```bash
docker build -t libgo .
docker run -p 8000:8000 libgo
```

## Current Features

- **Full CRUD Operations**: Create, Read, Update, Delete books
- **Authentication**: JWT-based login for staff and admin
- **Staff Management**: Register, update, and delete staff members
- **Email Notifications**: Send email notifications
- **Logging**: Custom logging for all operations

## Development Notes

- The project follows a modular architecture: Router → Service → Model
- JWT-based authentication with role separation (Admin/Staff)
- Passwords are securely hashed using bcrypt
- All endpoints use dependency injection for database sessions
- Custom logging implemented via `app/core/security.py`

## Future Enhancements

Potential improvements for the project:
- Book borrowing/return functionality
- User membership management
- Advanced search and filtering
- Pagination for listings
- Email templates
- Docker Compose for multi-container setup
- PostgreSQL support for production
