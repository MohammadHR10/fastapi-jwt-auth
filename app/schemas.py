from pydantic import BaseModel, EmailStr
from typing import Optional

class UserAuth(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    username: str
    is_active: bool = True

    class Config:
        from_attributes = True

class SystemUser(UserOut):
    pass

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenPayload(BaseModel):
    sub: str
    exp: int