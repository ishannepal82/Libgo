from src.core.logging import logger
from src.internal_api.repos.auth.staff import Staff
from src.utils.hash_password import hash_password
from src.internal_api.repos.auth.staff import get_staff as repo_get_staff, add_staff as repo_add_staff
def register_staff(register_data, db_session):
    try:
        staff_already_exist = repo_get_staff(db_session, register_data.email)
        if staff_already_exist:
            raise Exception("Staff already exist")
        
        staff = Staff(
            email = register_data.email,
            name = register_data.name,
            role = register_data.role,
            hashed_password = hash_password(register_data.password),
            code = register_data.code,
            phone= register_data.phone,
            is_admin=register_data.is_admin
        )
        staff = repo_add_staff(db_session, staff)
        logger.info("Staff registered successfully")
        return staff
    
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to register staff")