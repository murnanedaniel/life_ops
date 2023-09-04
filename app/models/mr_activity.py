from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

class MRActivity(Base):
    __tablename__ = 'mractivities'
    
    id = Column(Integer, primary_key=True)
    MRId = Column(Integer, ForeignKey('mergerequests.id'))
    type = Column(String)
    refId = Column(Integer)  # This can be a ForeignKey to Comment or Test, but we'll keep it generic for now
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    merge_request = relationship("MergeRequest", back_populates="activities")
