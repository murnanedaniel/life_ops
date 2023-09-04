from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class LifeDocument(Base):
    __tablename__ = 'lifedocs'
    
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'))
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="life_document")
    merge_requests = relationship("MergeRequest", back_populates="life_document")
    issues = relationship("Issue", back_populates="life_document")


# class LifeDocument(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     merge_requests = db.relationship('MergeRequest', backref='life_document')