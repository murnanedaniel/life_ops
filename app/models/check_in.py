from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class CheckIn(Base):
    __tablename__ = 'checkins'
    
    id = Column(Integer, primary_key=True)
    reminder_id = Column(Integer, ForeignKey('reminders.id'))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    response = Column(Text)
    status = Column(Enum('completed', 'missed'), default='missed')
