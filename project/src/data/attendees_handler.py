from typing import Dict
import uuid
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.attendees_repository import AttendeesRepository
from src.models.repositories.events_repository import EventsRepository


class AttendeeHandler:
    def __init__(self) -> None:
        self.attendees_repository = AttendeesRepository()
        self.events_repository = EventsRepository()
        
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param.get('event_id')
        
        event_attendees_count = self.events_repository.count_event_attendees(event_id)
        if(event_attendees_count['attendeesAmount'] and event_attendees_count['maxAttendees'] < event_attendees_count['attendeesAmount']):
            raise Exception('Event is full')
        
        body['id'] = str(uuid.uuid4())
        body['event_id']= event_id
        self.attendees_repository.insert_attendee(body)
        
        return HttpResponse(body=None, status_code= 201)
   
    def get_attendees_by_id(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param.get('attendee_id')
        
        attendee =  self.attendees_repository.get_attendee_by_id(attendee_id)
        
        if not attendee:
            raise Exception('Attendee not found')
        
        return HttpResponse(body={
            'attendee': {
                'email': attendee.email,
                'name': attendee.name,
                'eventTitle': attendee.title,
            }
            }, status_code= 201)
        
    def get_attendees_by_event_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param.get('event_id')
        attendees = self.attendees_repository.get_attendees_by_event_id(event_id)
        if not attendees: 
            raise Exception('No attendees found for event')
        
        formatted_attendees = []
        for attendee in attendees:
            formatted_attendees.append(
                {
                    'id': attendee.id,
                    'name': attendee.name,
                    'email': attendee.email,
                    'checkedInAt': attendee.checkedInAt,
                    'createdAt': attendee.createdAt,
                }
        )
            
        return HttpResponse(body={
            'attendees': formatted_attendees,
        }, status_code=200)