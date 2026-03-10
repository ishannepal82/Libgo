from src.internal_api.services.admin.manage_staff import (
    add_staff as service_add_staff,
    get_staff as service_get_staff,
    get_all_staff as service_get_all_staff,
    remove_staff as service_remove_staff,
    edit_staff as service_edit_staff
)

from fastapi import APIRouter, Depends
from src.internal_api.schema.StaffSchema import StaffRegister, StaffUpdate
from src.core.logging import logger
from src.db import get_session
from src.internal_api.services.auth.login_staff import StaffNotFoundError
from fastapi import HTTPException


admin_router = APIRouter()

@admin_router.post("/add-staff")
def add_staff(staff_data: StaffRegister, db = Depends(get_session)):
    try:
        staff = service_add_staff(db, staff_data)
        logger.info("Staff added successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)

@admin_router.get("/get-staff/{email}")
def get_staff(email: str, db = Depends(get_session)):
    try:
        staff = service_get_staff(db, email)
        logger.info("Staff fetched successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)

@admin_router.get("/get-all-staff")
def get_all_staff(db = Depends(get_session)):
    try:
        staffs = service_get_all_staff(db)
        logger.info("Staffs fetched successfully")
        return staffs
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)

@admin_router.delete("/remove-staff/{email}")
def remove_staff(email: str, db = Depends(get_session)):
    try:
        staff = service_remove_staff(db, email)
        logger.info("Staff removed successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)

@admin_router.put("/edit-staff/{email}")
def edit_staff(email: str, staff_data: StaffUpdate, db = Depends(get_session)):
    try:
        staff = service_edit_staff(db, email, staff_data)
        logger.info("Staff edited successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)

