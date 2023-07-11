from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .config import Base



class UserSchema(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    username = Column(String, unique = True)
    password = Column(String)
    token = Column(String, unique = True)
    comments: Mapped[list['CommentSchema']] = relationship("CommentSchema", back_populates="author")
    posts: Mapped[list['PostSchema']] = relationship("PostSchema", back_populates="author")



class PostSchema(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    video_url = Column(String)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[UserSchema] = relationship("UserSchema", back_populates="posts")
    comments: Mapped[list['CommentSchema']] = relationship("CommentSchema", back_populates="post")



class CommentSchema(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content = Column(String)
    post_id = Column(Integer)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[UserSchema] = relationship("UserSchema", back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped[PostSchema] = relationship("PostSchema", back_populates="comments")
