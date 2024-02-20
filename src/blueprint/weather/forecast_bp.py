from flask import Blueprint, request, jsonify, make_response
from services.address_fetch import AddressFetch
from services.weather_fetch import get_forecast
from errors.error_handler import error_handler
from drivers.jwt_auth import token_required
from validators.address.address_validator import address_validator

forecast_bp = Blueprint("forecast", __name__, url_prefix="/forecast")

@forecast_bp.post("/get-weather")
@token_required
def get_weather():
    response = None
    try:
        address_validator(request)
        body = request.json
        cep = body["cep"]

        address_fetch = AddressFetch()
        address = address_fetch.get_address(cep)

        forecast = get_forecast(address["id"])

        formated_response = {
            "body" : {
                "address" : address,
                "forecast" : forecast
            },
            "status_code" : 200
        }

        response = make_response(formated_response["body"], formated_response["status_code"])

    except Exception as exception:
        error_response = error_handler(exception)
        response = make_response(error_response["errors"], error_response["status_code"])

    return response
