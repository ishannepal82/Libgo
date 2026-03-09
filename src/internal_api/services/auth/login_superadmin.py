from src.internal_api.repos.auth.staff import get_staff
from src.core.logging import logger

class AdminNotFoundError(Exception):
    pass 
class StaffNotFoundError(Exception):
    pass

def admin_login(db, login_data):
    try: 
        email = login_data.get("email")
        password = login_data.get("password")

        if not email or not password:
            raise ValueError("Email and password are required")
        
        staff = get_staff(db, email)
        if not staff:
            raise StaffNotFoundError("Staff not found")
        
        if not staff.is_admin:
            raise ValueError("You are not an admin")
        
        if staff.hashed_password != password:
            raise ValueError("Invalid password")
        
        logger.info("Admin logged in successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise Exception("Admin login failed")
    