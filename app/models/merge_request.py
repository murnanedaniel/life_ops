from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class MergeRequest(Base):
    __tablename__ = 'mergerequests'
    
    id = Column(Integer, primary_key=True)
    lifeDocId = Column(Integer, ForeignKey('lifedocs.id'))
    status = Column(Enum('open', 'closed', 'merged'), default='open')
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    life_document = relationship("LifeDocument", back_populates="merge_requests")
    activities = relationship("MRActivity", back_populates="merge_request")



# class MergeRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     ai_review = db.Column(db.Text, nullable=False)
#     iteration = db.Column(db.Integer, default=0, nullable=False)
#     parent_request_id = db.Column(db.Integer, db.ForeignKey('merge_request.id'), nullable=True)
#     life_document_id = db.Column(db.Integer, db.ForeignKey('life_document.id'))
#     approval = db.Column(db.Boolean, default=False)
#     iterations = db.Column(db.Integer, default=1)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)