from config.database import Base
from sqlalchemy import Column, String, Integer

#Model table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    genre = Column(String)
    location = Column(String)
    description = Column(String)