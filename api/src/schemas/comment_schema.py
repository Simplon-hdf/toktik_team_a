# from __future__ import annotations
from typing import ForwardRef, Optional
from pydantic import BaseModel



class CommentBase(BaseModel):
    pass

class CommentCreate(CommentBase):
    content: str
    user_id: int
    post_id: int

class CommentPatch(CommentBase):
    id: int
    content: Optional[str] = None

class Comment(CommentBase):
    id: int
    content: str
    user_id: int
    post_id: int
