from typing import Dict, List
from src.models.entities.attendee import Attendee
from src.models.entities.event import Event
from src.models.entities.check_in import CheckIn
from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError, NoResultFound

class AttendeesRepository:
    
    def insert_attendee(self, attendeeInfo) -> Dict:
        with db_connection_handler as database: 
            try:
                attendee = (
                    Attendee(
                        id=attendeeInfo.get('id'),
                        name= attendeeInfo.get('name'),
                        email= attendeeInfo.get('email'),
                        event_id = attendeeInfo.get('event_id'),
                    )
                )
                database.session.add(attendee)
                database.session.commit()
                return attendeeInfo;
            
            except IntegrityError:
                raise Exception('Attendee already exists')
            
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_attendee_by_id(self, attendee_id: str):
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                    .query(Attendee)
                    .join(Event, Event.id == Attendee.event_id)
                    .filter(Attendee.id == attendee_id)
                    .with_entities(Attendee.name, Attendee.email, Event.title)
                    .one()
                )
                return attendee
            except NoResultFound:
                    return None
            
            
    def get_attendees_by_event_id(self, event_id: str) -> List[Attendee]:
         with db_connection_handler as database:
            try:
                attendees = (
                    database.session
                    .query(Attendee)
                    .outerjoin(CheckIn, CheckIn.attendee_id == Attendee.id)
                    # .join(Event, Event.id == Attendee.event_id)
                    .filter(Attendee.event_id == event_id)
                    .with_entities(
                        Attendee.id, 
                        Attendee.name, 
                        Attendee.email, 
                        # Event.title, 
                        CheckIn.created_at.label('checkedInAt'),
                        Attendee.created_at.label('createdAt')
                        )
                    .all()
                )
                return attendees
            except NoResultFound:
                    return None
            