from pydantic import BaseModel, ConfigDict
from typing import Optional







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

class RegisterSchema(UserBase):
    username: str

class RegisterSchemaWithToken(RegisterSchema):
    token: str

class User(UserBase):
    id: int
    token: str
    comments: list[Comment] = []
    posts: list[Post] = []
    model_config = ConfigDict(from_attributes=True)

User.model_rebuild()
