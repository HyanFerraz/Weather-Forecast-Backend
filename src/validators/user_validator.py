from cerberus import Validator
from errors.error_handler import HttpUnprocessableEntityError

def user_body_validator(request) -> None:
    body_validator = Validator({
        "username": { "type": "string", "required": True, "empty": False },
        "password": { "type": "string", "required": True, "empty": False }
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)