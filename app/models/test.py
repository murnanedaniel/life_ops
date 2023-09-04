from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class Test(Base):
    __tablename__ = 'tests'
    
    id = Column(Integer, primary_key=True)
    status = Column(Enum('pass', 'fail'), default='fail')
    type = Column(String)
    results = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
