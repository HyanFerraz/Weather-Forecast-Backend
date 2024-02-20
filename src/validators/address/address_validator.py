from cerberus import Validator
from errors.error_handler import HttpUnprocessableEntityError

def address_validator(request) -> None:
    body_validator = Validator({
        "cep": { "type": "string", "required": True, "empty": False },
    })

    is_valid = body_validator.validate(request.json)
    if is_valid is False:
        raise HttpUnprocessableEntityError(body_validator.errors)