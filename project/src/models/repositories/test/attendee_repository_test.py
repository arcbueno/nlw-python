from ..attendees_repository import AttendeesRepository
from project.src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Skipping new attendee')
def test_insert_attendee():
    event_id = '0e5df084-1885-4a75-bd70-27a3a0135e8f'
    attende_info = {
        'id': 'meu_attendee',
        'name': 'jose da silva',
        'email': 'email@example.com',
        'event_id': event_id 
    }
    
    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attende_info)
    print(response)

# @pytest.mark.skip(reason='Not necessary')
def test_get_attendee_by_id():
    attendee_id = 'meu_attendee'
    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_by_id(attendee_id)
    if(response is None):
        print('Attendee not found')
    else:
        print(response)
    
