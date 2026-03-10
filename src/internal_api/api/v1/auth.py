from fastapi import APIRouter, HTTPException, Depends
from src.internal_api.services.auth.login_staff import (staff_login as service_staff_login)
from src.internal_api.services.auth.login_superadmin import (admin_login as service_admin_login)
from src.internal_api.services.auth.register_staff import (register_staff as service_register_staff)
from src.core.logging import logger
from src.db import get_session
from fastapi_jwt_auth import AuthJWT
from src.internal_api.schema.StaffSchema import (StaffLogin, StaffRegister, StaffResponse)

auth_router = APIRouter()

@auth_router.post("/admin-login")
def admin_login(login_data: StaffLogin, db=Depends(get_session)):
    try: 
        admin = service_admin_login(db=db, login_data=login_data)
        logger.info("Admin Login Sucessfull!")
        return admin
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)
    
@auth_router.post("/staff-login")
def staff_login(login_data: StaffLogin, db = Depends(get_session)):
    try: 

        staff = service_staff_login(db=db, login_data=login_data, auth=AuthJWT())
        logger.info("Staff Login Sucessfull!")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)
    
@auth_router.post("/staff-register", response_model=StaffResponse)
def staff_register(staff_data: StaffRegister, db = Depends(get_session)):
    try: 
        staff = service_register_staff(
            db_session=db,
            register_data=staff_data
        )
        logger.info("Staff Register Sucessfull!")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(detail="Internal Server Error", status_code=500)