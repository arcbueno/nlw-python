from ..events_repository import EventsRepository
from project.src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Skipping new event')
def test_insert_event():
    event = {
        'uuid': 'testeuuid2',
        'title': 'test title',
        'slug': 'test slug',
        'maximum_attendees': 20 
    }
    
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason='Not necessary')
def test_get_event_by_id():
    event_id = 'testeuuid'
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    if(response is None):
        print('Event not found')
    else:
        print(response.title)
    
