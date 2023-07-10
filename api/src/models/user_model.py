from sqlalchemy import Column, Integer, String
from config import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String)
    password = Column(String)
    token = Column(String, unique=True)