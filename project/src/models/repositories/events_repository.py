
from typing import Dict
from project.src.models.entities.event import Event
from project.src.models.settings.connection import db_connection_handler

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
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
    
    def get_event_by_id(self, event_id: str) -> Event:
        with db_connection_handler as database:
            event = (
                 database.session.query(Event).filter(Event.id == event_id).one()
            )
            return event
        