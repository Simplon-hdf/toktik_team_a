from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    video_url = Column(String)
    user_id =  Column(Integer)
    # user_id =  Column(Integer, ForeignKey("user.id"))
    # user = relationship("User", back_populates="post")
