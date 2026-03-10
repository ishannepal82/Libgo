from src.internal_api.repos.auth.staff import get_staff
from src.core.logging import logger

class StaffNotFoundError(Exception):
    pass

def staff_login(db, login_data, auth):
    try: 
        email = login_data.get("email")
        password = login_data.get("password")

        if not email or not password:
            raise ValueError("Email and password are required")
        
        staff = get_staff(db, email)
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
    