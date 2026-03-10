from src.core.logging import logger
from src.internal_api.repos.auth.staff import Staff
from src.utils.hash_password import hash_password
def register_staff(register_data, db_session):
    try:
        staff = Staff(
            email = register_data.email,
            name = register_data.name,
            role = register_data.role,
            hashed_password = hash_password(register_data.password),
            code = register_data.code,
            phone= register_data.phone,
            is_admin=register_data.is_admin
        )
        db_session.add(staff)
        db_session.commit()
        return staff
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to register staff")