from typing import Dict
from project.src.models.entities.attendee import Attendee
from project.src.models.entities.event import Event
from project.src.models.settings.connection import db_connection_handler
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
            
            