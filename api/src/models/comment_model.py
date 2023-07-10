from sqlalchemy import Column, ForeignKey, String, Integer, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from config import Base
from.user_model import User

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    post_id = Column(Integer)
    user_id = Column(Integer)



    # id: int = Column(Integer, Identity(), primary_key=True, index=True, )
    # content = Column(String, unique=True)

    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # user: Mapped[User] = relationship("User", back_populates="comments")

    # post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    # post: Mapped[User] = relationship("Post", back_populates="comments")
