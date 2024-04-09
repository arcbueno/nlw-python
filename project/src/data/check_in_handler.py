from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.check_ins_repository import CheckInsRepository


class CheckInHandler: 
    def __init__(self) -> None:
        self.checkin_repository = CheckInsRepository()
        
    def registry(self, http_request: HttpRequest) -> HttpResponse:
        check_in_info = http_request.param['attendee_id']
        self.checkin_repository.insert_check_in(check_in_info)
        
        return HttpResponse(
            body=None,
            status_code=201
        )
        