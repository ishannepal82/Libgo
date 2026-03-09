from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import BackgroundTasks
from fastapi import HTTPException
from src.services.email.write_email import write_email as service_write_email

email_router = APIRouter()

@email_router.post("/write-email")
async def write_email(background_tasks: BackgroundTasks):
    try:
        await service_write_email(
            subject = "LibGo Testing", body="Hello from Fastapi", 
            background_tasks=background_tasks,
            email_to = "ishannepal04@gmail.com"
        )
        return JSONResponse(content="Email sent successfully", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send email")
    