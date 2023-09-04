from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    passwordHash = Column(String, nullable=False)
    lifeDocId = Column(Integer, ForeignKey('lifedocs.id'))
    
    life_document = relationship("LifeDocument", uselist=False, back_populates="user")
