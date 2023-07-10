from typing import List, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from passlib.context import CryptContext

T = TypeVar('T')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

class LoginSchema(BaseModel):
    email: str | None = None
    password: str | None = None

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    id: int | None = None
    email: str | None = None
    username: str | None = None
    password: str | None = None
    token: str | None = None

    class Config:
        orm_mode = True