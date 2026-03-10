from src.core.logging import logger
from src.internal_api.repos.auth.staff import (
    add_staff as repo_add_staff,
    remove_staff as repo_remove_staff,
    edit_staff as repo_edit_staff,
    get_staff as repo_get_staff,
    get_all_staffs as repo_get_all_staffs)
from src.internal_api.schema.StaffSchema import StaffRegister, StaffUpdate
from src.internal_api.services.auth.login_staff import StaffNotFoundError


def add_staff(db, staff_data: StaffRegister):
    try:
        staff_already_exist = repo_get_staff(db, staff_data.email)
        if staff_already_exist:
            raise Exception("Staff already exist")
        
        staff = repo_add_staff(db, **staff_data)
        logger.info("Staff added successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to add staff")

def get_all_staff(db):
    try:
        staffs = repo_get_all_staffs(db)
        return staffs
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to fetch staffs")

def get_staff(db, email):
    try:
        staff = repo_get_staff(db, email)
        return staff
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to fetch staff")
    
def remove_staff(db, email):
    try:
        staff = repo_get_staff(db, email)
        if not staff:
            raise StaffNotFoundError("Staff not found")
        
        repo_remove_staff(db, staff)
        logger.info("Staff removed successfully")
        return staff
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to remove staff")

def edit_staff(db, email, staff_data: StaffUpdate):
    
    try:
        staff = repo_get_staff(db, email)

        if not staff:
            raise StaffNotFoundError("Staff not found")
        
        update_data = staff_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(staff, field, value)

        staff = repo_edit_staff(db, email, update_data)
        logger.info("Staff edited successfully")
        return staff
    
    except Exception as e:
        logger.error(str(e))
        raise Exception("Failed to edit staff")

    