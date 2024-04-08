
from typing import Dict
from src.models.entities.attendee import Attendee
from src.models.entities.event import Event
from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError, NoResultFound

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                event = Event(
                id = eventsInfo.get('uuid'),
                title=eventsInfo.get('title'),
                details=eventsInfo.get('details'),
                slug=eventsInfo.get('slug'),
                maximum_attendees=eventsInfo.get('maximum_attendees'),
                )
                database.session.add(event)
                database.session.commit()
                
                return eventsInfo
            
            except IntegrityError:
                raise Exception('Event already exists')
            
            except Exception as exception:
                database.session.rollback()
                raise exception
            
            
    
    def get_event_by_id(self, event_id: str) -> Event:
        
        with db_connection_handler as database:
            try:
                event = (
                    database.session.query(Event).filter(Event.id == event_id).one()
                )
                return event
            except NoResultFound:
                    return None
    
            
    def count_event_attendees(self, event_id: str) -> Dict:
          with db_connection_handler as database:
            
            event_count = (
                database.session
                .query(Event)
                .join(Attendee, Event.id == Attendee.event_id)
                .filter(Event.id == event_id).with_entities(Event.maximum_attendees, Attendee.id).all()
            )
            
            if not len(event_count):
                return {
                    'maxAttendees':0,
                    'attendeesAmount': 0
                }
            
            return {
                    'maxAttendees': event_count[0].maximum_attendees,
                    'attendeesAmount': len(event_count),
            }
                  
            
            
        