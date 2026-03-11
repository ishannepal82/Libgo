from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional
from uuid import UUID, uuid4


class Staff(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    role: str
    is_admin: bool = False
    email: str
    code: str
    hashed_password: str
    phone: str


def get_all_staffs(db):
    return db.query(Staff).all()


def get_staff(db, email):
    return db.query(Staff).filter(Staff.email == email).first()


def remove_staff(db, staff):
    db.delete(staff)
    db.commit()


def edit_staff(db, data):
    db.commit()
    db.refresh(data)
    return data


def add_staff(db, staff):
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff
