from app.modules.staff.service import (
    add_staff as service_add_staff,
    get_staff as service_get_staff,
    get_all_staff as service_get_all_staff,
    remove_staff as service_remove_staff,
    edit_staff as service_edit_staff,
)

from fastapi import APIRouter, Depends, HTTPException, Request
from app.modules.auth.schemas import StaffRegister, StaffUpdate
from app.core.logger import logger
from app.db.session import get_session
from app.modules.auth.service import StaffNotFoundError
from app.dependencies.auth import require_auth


admin_router = APIRouter()


@admin_router.post("/add-staff")
@require_auth
def add_staff(
    staff_data: StaffRegister, db=Depends(get_session), request: Request = None
):
    try:
        user = request.state.user
        staff = service_add_staff(db, staff_data)
        logger.info(message="Staff added successfully")
        return staff
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)


@admin_router.get("/get-staff/{email}")
@require_auth
def get_staff(email: str, db=Depends(get_session), request: Request = None):
    try:
        user = request.state.user
        staff = service_get_staff(db, email)
        logger.info(message="Staff fetched successfully")
        return staff
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)


@admin_router.get("/get-all-staff")
@require_auth
def get_all_staff(db=Depends(get_session), request: Request = None):
    try:
        user = request.state.user
        staffs = service_get_all_staff(db)
        logger.info(message="Staffs fetched successfully")
        return staffs
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)


@admin_router.delete("/remove-staff/{email}")
@require_auth
def remove_staff(email: str, db=Depends(get_session), request: Request = None):
    try:
        user = request.state.user
        staff = service_remove_staff(db, email)
        logger.info(message="Staff removed successfully")
        return staff
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)


@admin_router.put("/edit-staff/{email}")
@require_auth
def edit_staff(
    email: str,
    staff_data: StaffUpdate,
    db=Depends(get_session),
    request: Request = None,
):
    try:
        user = request.state.user
        staff = service_edit_staff(db, email, staff_data)
        logger.info(message="Staff edited successfully")
        return staff
    except Exception as e:
        logger.error(message=str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)
