from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func

class CheckIn(Base):
    __tablename__ = 'check_ins'
    
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendee_id = Column(Text, ForeignKey('attendees.id',), name='attendeeId', nullable=False)
    
    def __repr__(self):
        return f'CheckIn [attendee_id={self.attendee_id}]'