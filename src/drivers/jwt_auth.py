from dotenv import dotenv_values
from functools import wraps
from errors.error_handler import error_handler
from flask import request, make_response
import jwt
import datetime

config = dotenv_values(".env")

def create_jwt_token(username: str) -> str:
    return jwt.encode({
        "username": username,
        "exp" : datetime.datetime.now() + datetime.timedelta(minutes=1)
    },
    config["JWT_KEY"]
    )


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("token")
        if not token:
            formated_response = {
                "body" : {
                    "message" : "token is missing"
                },
                "status_code" : 401
            }
            return make_response(formated_response["body"], formated_response["status_code"])
        try:
            data = jwt.decode(token, config["JWT_KEY"])
        except Exception as exception:
            response = error_handler(exception)
        return f(*args, **kwargs)
    return decorated