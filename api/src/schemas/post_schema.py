# from __future__ import annotations
from typing import ForwardRef, Optional
from pydantic import BaseModel



class PostBase(BaseModel):
    title: str
    description: Optional[str] = None

class PostCreate(PostBase):
    video_url: str
    user_id: int

class PostPatch(PostBase):
    id: int

class Post(PostBase):
    id: int
    video_url: str
    user_id: int
