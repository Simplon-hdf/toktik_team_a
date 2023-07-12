from pydantic import BaseModel, ConfigDict
from passlib.context import CryptContext
from typing import Optional



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





class CommentBase(BaseModel):
    pass

class CommentCreate(CommentBase):
    content: str
    author_id: int
    post_id: int

class CommentPatch(CommentBase):
    content: Optional[str] = None

class Comment(CommentBase):
    id: int
    content: str
    author_id: int
    post_id: int
    model_config = ConfigDict(from_attributes=True)

Comment.model_rebuild()





class PostBase(BaseModel):
    description: Optional[str] = None

class PostCreate(PostBase):
    title: str
    video_url: str
    author_id: Optional[int] = None

class PostPatch(PostBase):
    title: str

class Post(PostBase):
    id: int
    title: str
    video_url: str
    author_id: int
    comments: list[Comment] = []
    model_config = ConfigDict(from_attributes=True)

Post.model_rebuild()





class UserBase(BaseModel):
    password: str
    email: str

class Hasher():
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

class RegisterSchema(UserBase):
    username: str

# class UserPost(UserBase):
#     username: str

class User(UserBase):
    id: int
    # email: str
    # username: str
    # password: str
    token: str
    comments: list[Comment] = []
    posts: list[Post] = []
    model_config = ConfigDict(from_attributes=True)

User.model_rebuild()
