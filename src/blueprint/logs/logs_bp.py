from flask import Blueprint, request, jsonify, make_response
from drivers.jwt_auth import token_required
from controller.log.log_controller import LogController
from errors.error_handler import error_handler

logs_bp = Blueprint("logs", __name__, url_prefix="/logs")

@logs_bp.get("/")
@token_required
def get_logs():
    logger = LogController()
    try:    
        username = request.cookies.get("username")
        logger.create_log(username, request.method, request.path)
        formated_response = logger.get_all_logs(username)

        response = make_response(formated_response["body"], formated_response["status_code"])
        
    except Exception as exception:
        error_response = error_handler(exception)
        response = make_response(error_response["errors"], error_response["status_code"])

    return response
