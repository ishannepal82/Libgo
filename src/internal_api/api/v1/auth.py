from fastapi import APIRouter
from fastapi import HTTPException

auth_router = APIRouter()

@auth_router.post("/admin-login")
def admin_login():
    try: 
        return {"message": "Admin login successful"}
    except Exception as e:
        raise HTTPException(detail="Internal Server Error", status_code=500)
    
@auth_router.post("/staff-login")
def staff_login():
    try: 
        return {"message": "Staff login successful"}
    except Exception as e:
        raise HTTPException(detail="Internal Server Error", status_code=500)
    
@auth_router.post("/staff-register")
def staff_register():
    try: 
        return {"message": "Staff registration successful"}
    except Exception as e:
        raise HTTPException(detail="Internal Server Error", status_code=500)