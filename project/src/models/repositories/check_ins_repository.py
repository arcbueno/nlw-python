
from typing import Dict
import uuid
from src.models.entities.check_in import CheckIn
from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError, NoResultFound

class CheckInsRepository:
    def insert_check_in(self, attendee_id:str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIn(
                        id = str(uuid.uuid4()),
                        attendee_id = attendee_id,
                    )
                )
                database.session.add(check_in)
                database.session.commit()
                
                return attendee_id
            
            # except IntegrityError:
            #     raise Exception('CheckIn already done')
            
            except Exception as exception:
                database.session.rollback()
                raise exception
            
            
    #TODO: Create get all users checked in event
            