from dotenv import dotenv_values
from functools import wraps
from errors.error_handler import error_handler
from flask import request
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
            return {
                "message" : "token is missing"
            }
        try:
            data = jwt.decode(token, config["JWT_KEY"])
        except Exception as exception:
            response = error_handler(exception)
        return f(*args, **kwargs)
    return decorated