from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class Issue(Base):
    __tablename__ = 'issues'
    
    id = Column(Integer, primary_key=True)
    lifeDocId = Column(Integer, ForeignKey('lifedocs.id'))
    status = Column(Enum('open', 'closed'), default='open')
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    life_document = relationship("LifeDocument", back_populates="issues")
    activities = relationship("IssueActivity", back_populates="issue")
