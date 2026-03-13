from functools import wraps
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from app.modules.auth.dependencies import get_current_user as get_user
from fastapi.exceptions import HTTPException
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/staff-login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    return get_user(token)


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        request = kwargs.get("request")
        if not request:
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
        if request:
            auth_header = request.headers.get("Authorization")
            if auth_header:
                token = auth_header.split(" ")[1]
                user = get_current_user(token)
                if user:
                    print(user)
                    return f(user, *args, **kwargs)

        return HTTPException(status_code=401, detail="Unauthorized")

    return decorated
