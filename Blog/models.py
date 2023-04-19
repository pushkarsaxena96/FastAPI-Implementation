from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationships, relationship


class Blog(Base):
    __tablename__ = 'blogs_detail'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("user_access_detail.id"))


    creator = relationship("User",back_populates="blogs")    

class User(Base):
    __tablename__ = 'user_access_detail'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)    
    password = Column(String)    

    blogs = relationship("Blog", back_populates="creator")


