from flask import Blueprint, jsonify, request

from src.data.attendees_handler import AttendeeHandler
from src.http_types.http_request import HttpRequest

attendee_route_bp = Blueprint('attendee_route', __name__)

@attendee_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendee(event_id):
    attendee_handler = AttendeeHandler()
    http_request = HttpRequest(param= {'event_id': event_id}, body=request.json)
    http_response = attendee_handler.register(http_request=http_request)
    
    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route('/attendees/<attendee_id>', methods=['GET'])
def get_attendee_by_id(attendee_id):
    attendee_handler = AttendeeHandler()
    http_request = HttpRequest(param= {'attendee_id': attendee_id}, )
    http_response = attendee_handler.get_attendees_by_id(http_request=http_request)
     
    return jsonify(http_response.body), http_response.status_code
