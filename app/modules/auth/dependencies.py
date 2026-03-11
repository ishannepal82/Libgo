from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from app.core.logger import logger
from app.core.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGRORITHM = settings.ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
def get_current_user(token: str = Depends(oauth2_scheme)):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGRORITHM])
        return payload["sub"]
    except ExpiredSignatureError:
        logger.warning("Token has expired")
        raise Exception("Token has expired")
    except JWTError:
        logger.warning("Invalid token")
        raise Exception(detail="Invalid token")
