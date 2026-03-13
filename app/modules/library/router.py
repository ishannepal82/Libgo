from fastapi import APIRouter, Depends, HTTPException, Request
from app.modules.library.service import (
    create_library as service_create_library,
    get_library_by_id as service_get_library_by_id,
    get_my_libraries as service_get_my_libraries,
    update_library as service_update_library,
    delete_library as service_delete_library,
    LibraryNotFoundError,
    LibraryDBException,
)
from app.modules.library.schemas import LibraryCreate, LibraryUpdate, LibraryResponse
from app.dependencies.auth import require_auth
from app.core.logger import logger
from app.db.session import get_session
from uuid import UUID

library_router = APIRouter()


@library_router.post("/create-library", response_model=LibraryResponse, status_code=201)
@require_auth
def create_library(
    user, library_data: LibraryCreate, db=Depends(get_session), request: Request = None
):
    try:
        library = service_create_library(library_data, owner_id=user, db=db)
        logger.info(message="Successfully created library")
        return library
    except Exception as e:
        logger.warning(message=f"Something went wrong: {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@library_router.get(
    "/my-libraries", response_model=list[LibraryResponse], status_code=200
)
@require_auth
def get_my_libraries(user, db=Depends(get_session), request: Request = None):
    try:
        libraries = service_get_my_libraries(owner_id=user, db=db)
        logger.info(message="Successfully fetched all libraries for current user")
        return libraries
    except Exception as e:
        logger.warning(message=f"Something went wrong: {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@library_router.get(
    "/get-library/{library_id}", response_model=LibraryResponse, status_code=200
)
@require_auth
def get_library(
    user, library_id: UUID, db=Depends(get_session), request: Request = None
):
    try:
        library = service_get_library_by_id(library_id, owner_id=user, db=db)
        logger.info(message=f"Successfully fetched library with id: {library_id}")
        return library
    except LibraryNotFoundError as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(message=f"Something went wrong: {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@library_router.put("/update-library/{library_id}", response_model=LibraryResponse)
@require_auth
def update_library(
    user,
    library_id: UUID,
    library_data: LibraryUpdate,
    db=Depends(get_session),
    request: Request = None,
):
    try:
        library = service_update_library(library_id, library_data, owner_id=user, db=db)
        logger.info(message=f"Successfully updated library with id: {library_id}")
        return library
    except LibraryNotFoundError as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(message=f"Something went wrong: {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)


@library_router.delete("/delete-library/{library_id}", status_code=204)
@require_auth
def delete_library(
    user, library_id: UUID, db=Depends(get_session), request: Request = None
):
    try:
        service_delete_library(library_id, owner_id=user, db=db)
        logger.info(message=f"Successfully deleted library with id: {library_id}")
        return {"message": "Library deleted successfully"}
    except LibraryNotFoundError as e:
        logger.warning(msg=str(e))
        raise HTTPException(detail=str(e), status_code=404)
    except Exception as e:
        logger.warning(message=f"Something went wrong: {e}")
        raise HTTPException(detail="Internal Server Error", status_code=500)
