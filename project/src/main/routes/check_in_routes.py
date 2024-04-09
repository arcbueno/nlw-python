from flask import Blueprint, jsonify, request

from src.data.check_in_handler import CheckInHandler
from src.data.event_handler import EventHandler
from src.http_types.http_request import HttpRequest

checkin_route_bp = Blueprint('checkin_route', __name__)

@checkin_route_bp.route('/attendees/<attendee_id>/checkin', methods=['POST'])
def create_checkin(attendee_id):
    check_in_handler = CheckInHandler()
    http_request = HttpRequest(param={'attendee_id': attendee_id})
    
    http_response = check_in_handler.registry(http_request=http_request)
    
    return jsonify(http_response.body), http_response.statucks_code
    