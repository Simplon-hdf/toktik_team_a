# from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class CommentBase(BaseModel):
    pass

class CommentCreate(CommentBase):
    content: str
    author_id: int
    post_id: int

class CommentPatch(CommentBase):
    id: int
    content: Optional[str] = None

class Comment(CommentBase):
    id: int
    content: str
    author_id: int
    post_id: int
    class Config:
        orm_mode = True

Comment.model_rebuild()