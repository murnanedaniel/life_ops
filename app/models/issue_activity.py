from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class IssueActivity(Base):
    __tablename__ = 'issueactivities'
    
    id = Column(Integer, primary_key=True)
    issueId = Column(Integer, ForeignKey('issues.id'))
    type = Column(String)
    refId = Column(Integer)  # This can be a ForeignKey to Comment or Test, but we'll keep it generic for now
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    issue = relationship("Issue", back_populates="activities")
