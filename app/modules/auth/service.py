from app.core.security import logger
from app.modules.auth.models import (
    Staff,
    get_staff as repo_get_staff,
    add_staff as repo_add_staff,
)
from app.utils.hash_password import hash_password
from app.core.config import settings


class StaffNotFoundError(Exception):
    pass


def staff_login(db, login_data, auth):
    try:
        email = login_data.get("email")
        password = login_data.get("password")

        if not email or not password:
            raise ValueError("Email and password are required")

        staff = repo_get_staff(db, email)
        if not staff:
            raise StaffNotFoundError("Staff not found")

        if staff.hashed_password != password:
            raise ValueError("Invalid password")

        logger.info("Admin logged in successfully")

        toekn = auth.create_access_token(subject=staff.email)
        return {"access_token": toekn, "token_type": "bearer"}
    except Exception as e:
        logger.error(str(e))
        raise Exception("Admin login failed")


class AdminNotFoundError(Exception):
    pass


def admin_login(db, login_data, auth):
    try:
        email = login_data.get("email")
        password = login_data.get("password")

        if not email or not password:
            raise ValueError("Email and password are required")

        staff = repo_get_staff(db, email)
        if not staff:
            raise StaffNotFoundError("Staff not found")

        if not staff.is_admin:
            raise ValueError("You are not an admin")

        if staff.hashed_password != password:
            raise ValueError("Invalid password")

        logger.info("Admin logged in successfully")
        access_token = auth.create_access_token(subject=staff.email)
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        logger.error(str(e))
        raise Exception("Admin login failed")


def register_staff(register_data, db_session):
    try:
        staff_already_exist = repo_get_staff(db_session, register_data.email)
        if staff_already_exist:
            raise Exception("Staff already exist")

        staff = Staff(
            email=register_data.email,
            name=register_data.name,
            role=register_data.role,
            hashed_password=hash_password(register_data.password),
            code=register_data.code,
            phone=register_data.phone,
            is_admin=register_data.is_admin,
        )
        staff = repo_add_staff(db_session, staff)
        logger.info("Staff registered successfully")
        return staff

    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to register staff")
