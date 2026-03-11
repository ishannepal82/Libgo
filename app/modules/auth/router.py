from fastapi import APIRouter, HTTPException, Depends
from app.modules.auth.service import (
    staff_login as service_staff_login,
    admin_login as service_admin_login,
    register_staff as service_register_staff,
    StaffNotFoundError,
)
from app.core.logger import logger
from app.db.session import get_session
from app.modules.auth.schemas import StaffLogin, StaffRegister, StaffResponse

auth_router = APIRouter()


@auth_router.post("/admin-login")
def admin_login(login_data: StaffLogin, db=Depends(get_session)):
    try:
        admin = service_admin_login(db=db, login_data=login_data)
        logger.info(message="Admin Login Sucessfull!")
        return admin
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)


@auth_router.post("/staff-login")
def staff_login(login_data: StaffLogin, db=Depends(get_session)):
    try:
        staff = service_staff_login(
            db=db,
            login_data=login_data,
        )
        logger.info(message="Staff Login Sucessfull!")
        return staff
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)


@auth_router.post("/staff-register", response_model=StaffResponse)
def staff_register(staff_data: StaffRegister, db=Depends(get_session)):
    try:
        staff = service_register_staff(db_session=db, register_data=staff_data)
        logger.info(message="Staff Register Sucessfull!")
        return staff
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)
