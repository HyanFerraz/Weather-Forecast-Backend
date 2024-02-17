from typing import Dict
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def error_handler(error: Exception) -> Dict:
    if isinstance(error, HttpUnprocessableEntityError):    
        return {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            , 
            "status_code" : error.status_code
        }
    
    return {
            "errors": [{
                    "title": "Server Error",
                    "detail": str(error)
            }]
        , 
        "status_code" :  500
    }