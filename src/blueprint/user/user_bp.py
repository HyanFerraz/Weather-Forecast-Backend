from flask import Blueprint, request, jsonify, make_response
from validators.user_validator import user_body_validator
from errors.error_handler import error_handler
from controller.user_controller import UserController
from drivers.jwt_auth import token_required

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.post("/signup")
def signup():
    response = None
    try:
        user_body_validator(request)
        body = request.json
        username = body["username"]
        password = body["password"]

        user_controller = UserController()
        formated_response = user_controller.create_new_user(username, password)
        response = make_response(formated_response["body"], formated_response["status_code"])
    except Exception as exception:
        error_response = error_handler(exception)
        response = make_response(error_response["errors"], error_response["status_code"])

    return response

@user_bp.post("/login")
def login():
    response = None
    try:
        user_body_validator(request)
        body = request.json
        username = body["username"]
        password = body["password"]

        user_controller = UserController()
        formated_response = user_controller.login(username, password)

        response = make_response(formated_response["body"], formated_response["status_code"])

        if formated_response["status_code"] == 200:
            token = formated_response["body"]["token"]
            response.set_cookie("token", token)
        

    except Exception as exception:
        error_response = error_handler(exception)
        response = make_response(error_response["errors"], error_response["status_code"])

    return response

@user_bp.get("/logout")
@token_required
def logout():
    response = make_response({
        "message" : "User Logged out"
    })
    response.set_cookie("token", "", expires=0)
    return response
