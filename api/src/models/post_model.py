from sqlalchemy import Column, String, ForeignKey
from config import Base
from models.user_model import User
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    video_url = Column(String)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[User] = relationship("User", back_populates="posts")
    