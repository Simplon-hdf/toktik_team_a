# from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from typing import ForwardRef


Comment = ForwardRef('Comment')

class PostBase(BaseModel):
    description:  Optional[str] = None


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
    class Config:
        orm_mode = True

Post.model_rebuild()