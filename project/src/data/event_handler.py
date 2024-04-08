

from typing import Dict
import uuid
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.events_repository import EventsRepository


class EventHandler:
    def __init__(self) -> None:
        self.events_repository = EventsRepository()
        
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body['uuid'] = str(uuid.uuid4())
        
        self.events_repository.insert_event(body)
        
        return HttpResponse(body={
            'eventId': body['uuid'],
        }, status_code= 200)
    
    def get_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param.get('event_id')
        event = self.events_repository.get_event_by_id(event_id)
        if not event:
            raise Exception('Event not found')
        
        event_attendees_count = self.events_repository.count_event_attendees(event_id)
        
        return HttpResponse(body={
            'event': { 
                'id': event.id,
                'title': event.title,
                'details': event.details,
                'slug': event.slug,
                'maximumAtendees': event.maximum_attendees,
                'attendeesAmount': event_attendees_count.get('attendeesAmount')
            }
        }, status_code= 200)