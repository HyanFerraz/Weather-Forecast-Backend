from flask import Blueprint
from blueprint.user.user_bp import user_bp
from blueprint.weather.forecast_bp import forecast_bp

api_bp = Blueprint("api", __name__, url_prefix="/api")

api_bp.register_blueprint(user_bp)
api_bp.register_blueprint(forecast_bp)
