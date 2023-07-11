# from typing import TypeVar
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import ForwardRef


# T = TypeVar('T')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
Comment = ForwardRef('Comment')
Post = ForwardRef('Post')

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    password: str
    email: str

class Hasher():
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

class LoginSchema(UserBase):
    email: str
    password: str
    class Config:
        orm_mode = True

class UserSchema(UserBase):
    id: int 
    email: str 
    username: str
    password: str
    token: str
    comments: list[Comment] = []
    posts: list[Post] = []
    class Config:
        orm_mode = True

UserSchema.model_rebuild()