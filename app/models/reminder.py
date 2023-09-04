from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum
import datetime

class Reminder(Base):
    __tablename__ = 'reminders'
    
    id = Column(Integer, primary_key=True)
    type = Column(String)
    time = Column(String)
    day = Column(String)
    frequency = Column(String)
    status = Column(Enum('active', 'inactive'), default='active')
    associated_MR_or_Issue_id = Column(Integer)  # This can be a ForeignKey to MergeRequest or Issue, but we'll keep it generic for now
