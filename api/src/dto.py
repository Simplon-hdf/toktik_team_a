from pydantic import BaseModel
from passlib.context import CryptContext
from typing import Optional, ForwardRef
from .models import CommentSchema, PostSchema, UserSchema



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

class UserSchema(UserBase):
    id: int
    email: str
    username: str
    password: str
    token: str
    comments: list[CommentSchema] = []
    posts: list[PostSchema] = []
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

UserSchema.model_rebuild()



class PostBase(BaseModel):
    description:  Optional[str] = None


class PostCreate(PostBase):
    title: str
    video_url: str
    author_id: Optional[int] = None

class PostPatch(PostBase):
    title: str

class PostSchema(PostBase):
    id: int
    title: str
    video_url: str
    author_id: int
    comments: list[CommentSchema] = []
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

PostSchema.model_rebuild()




class CommentBase(BaseModel):
    pass

class CommentCreate(CommentBase):
    content: str
    author_id: int
    post_id: int

class CommentPatch(CommentBase):
    content: Optional[str] = None

class CommentSchema(CommentBase):
    id: int
    content: str
    author_id: int
    post_id: int
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

CommentSchema.model_rebuild()
