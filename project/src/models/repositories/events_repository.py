
from typing import Dict
from project.src.models.entities.event import Event
from project.src.models.settings.connection import db_connection_handler
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
            
            
        