from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID


class Auth:
    def __init__(self, secret: str = "secret"):
        self.secret = secret

    def create_access_token(
        self, subject: str, expires_delta: Optional[timedelta] = None
    ) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=30)
        return f"token_{subject}_{expire}"


auth = Auth()
