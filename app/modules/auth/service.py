from app.core.logger import logger
from app.modules.auth.repo import (
    Staff,
    get_staff as repo_get_staff,
    add_staff as repo_add_staff,
)
from app.utils.hash_password import hash_password, check_password
from app.core.config import settings
from app.modules.auth.security import create_token


class StaffNotFoundError(Exception):
    pass


def staff_login(db, login_data):
    try:
        email = login_data.get("email")
        password = login_data.get("password")

        if not email or not password:
            raise ValueError("Email and password are required")

        staff = repo_get_staff(db, email)
        if not staff:
            raise StaffNotFoundError("Staff not found")
        print(staff)
        
        match = check_password(password, staff.hashed_password)
        if not match:
            raise ValueError("Invalid password")

        logger.info("Admin logged in successfully")

        token = create_token(login_data.email)
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        logger.error(str(e))
        raise Exception("Staff login failed")


def admin_login(db, login_data):
    try:
        email = login_data.email
        password = login_data.password

        if not email or not password:
            raise ValueError("Email and password are required")

        staff = repo_get_staff(db, email)
        if not staff:
            raise StaffNotFoundError("Admin not found")

        if not staff.is_admin:
            raise ValueError("You are not an admin")
        
        match = check_password(password, staff.hashed_password)
        if not match:
            raise ValueError("Invalid password")

        logger.info("Admin logged in successfully")
        access_token = create_token(email=login_data.email)
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
