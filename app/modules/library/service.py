from app.modules.library.repo import (
    create_library as repo_create_library,
    get_library_by_id as repo_get_library_by_id,
    get_all_libraries as repo_get_all_libraries,
    get_libraries_by_owner as repo_get_libraries_by_owner,
    update_library as repo_update_library,
    delete_library as repo_delete_library,
)
from app.modules.library.models import Library
from app.modules.library.schemas import LibraryCreate, LibraryUpdate
from app.core.logger import logger
from uuid import UUID


class LibraryNotFoundError(Exception):
    pass


class LibraryDBException(Exception):
    pass


def create_library(library_data: LibraryCreate, owner_id: str, db):
    try:
        new_library = Library(
            name=library_data.name,
            address=library_data.address,
            owner_id=owner_id,
        )
        created_library = repo_create_library(library=new_library, db_session=db)
        logger.info(f"Successfully created library with id: {created_library.id}")
        return created_library
    except Exception as e:
        logger.error(f"Failed to create library: {e}")
        raise LibraryDBException("Failed to create library in DB") from e


def get_library_by_id(library_id: UUID, owner_id: str, db):
    try:
        library = repo_get_library_by_id(library_id, db)
        if not library:
            logger.warning(f"Library not found with id: {library_id}")
            raise LibraryNotFoundError(f"Library not found with id: {library_id}")

        if library.owner_id != owner_id:
            logger.warning(f"Library {library_id} does not belong to user {owner_id}")
            raise LibraryNotFoundError(f"Library not found with id: {library_id}")

        return library
    except LibraryNotFoundError:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch library: {e}")
        raise LibraryDBException("Failed to fetch library from DB") from e


def get_my_libraries(owner_id: str, db):
    try:
        libraries = repo_get_libraries_by_owner(owner_id, db)
        return libraries
    except Exception as e:
        logger.error(f"Failed to fetch libraries: {e}")
        raise LibraryDBException("Failed to fetch libraries from DB") from e


def update_library(library_id: UUID, library_data: LibraryUpdate, owner_id: str, db):
    try:
        library = repo_get_library_by_id(library_id, db)
        if not library:
            logger.warning(f"Library not found with id: {library_id}")
            raise LibraryNotFoundError(f"Library not found with id: {library_id}")

        if library.owner_id != owner_id:
            logger.warning(f"Library {library_id} does not belong to user {owner_id}")
            raise LibraryNotFoundError(f"Library not found with id: {library_id}")

        update_data = library_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(library, field, value)

        updated_library = repo_update_library(library, db)
        logger.info(f"Successfully updated library with id: {library_id}")
        return updated_library
    except LibraryNotFoundError:
        raise
    except Exception as e:
        logger.error(f"Failed to update library: {e}")
        raise LibraryDBException("Failed to update library in DB") from e


def delete_library(library_id: UUID, owner_id: str, db):
    try:
        library = repo_get_library_by_id(library_id, db)
        if not library:
            logger.warning(f"Library not found with id: {library_id}")
            raise LibraryNotFoundError(f"Library not found with id: {library_id}")

        if library.owner_id != owner_id:
            logger.warning(f"Library {library_id} does not belong to user {owner_id}")
            raise LibraryNotFoundError(f"Library not found with id: {library_id}")

        repo_delete_library(library, db)
        logger.info(f"Successfully deleted library with id: {library_id}")
        return {"message": "Library deleted successfully"}
    except LibraryNotFoundError:
        raise
    except Exception as e:
        logger.error(f"Failed to delete library: {e}")
        raise LibraryDBException("Failed to delete library from DB") from e
