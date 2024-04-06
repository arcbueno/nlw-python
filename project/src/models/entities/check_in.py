from project.src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIn(Base):
    __tablename__ = 'check_ins'
    
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendee_id = Column(String, ForeignKey('attendees.id'), nullable=False)
    
    def __repr__(self):
        return f'CheckIn [attendee_id={self.attendee_id}]'