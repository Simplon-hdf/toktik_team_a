from sqlalchemy import Column, String
from config import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.comment_model import Comment
from models.post_model import Post

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    username = Column(String, unique = True)
    password = Column(String)
    token = Column(String, unique = True)
    comments: Mapped[list['Comment']] = relationship("Comment", back_populates="author")
    posts: Mapped[list['Post']] = relationship("Post", back_populates="author")
