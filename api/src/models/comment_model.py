from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from config import Base
from models.post_model import Post
from.user_model import User

class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content = Column(String)
    post_id = Column(Integer)
    user_id = Column(Integer)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[User] = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped[Post] = relationship("Post", back_populates="comments")
