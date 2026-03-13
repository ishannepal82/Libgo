from app.modules.library.models import Library
from uuid import UUID


def create_library(library: Library, db_session):
    db_session.add(library)
    db_session.commit()
    db_session.refresh(library)
    return library


def get_library_by_id(library_id: UUID, db_session):
    library = db_session.query(Library).filter(Library.id == library_id).first()
    return library


def get_all_libraries(db_session):
    libraries = db_session.query(Library).all()
    return libraries


def get_libraries_by_owner(owner_id: str, db_session):
    libraries = db_session.query(Library).filter(Library.owner_id == owner_id).all()
    return libraries


def update_library(library: Library, db_session):
    db_session.commit()
    db_session.refresh(library)
    return library


def delete_library(library: Library, db_session):
    db_session.delete(library)
    db_session.commit()
