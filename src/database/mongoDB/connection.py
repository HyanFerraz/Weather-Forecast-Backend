from pymongo import MongoClient
from errors.error_handler import error_handler
from drivers.dot_env_loader import get_dotenv_values

config = get_dotenv_values()

class MongoConnection():
    def __init__(self):
        self.client = MongoClient(
            f"mongodb://{config['MONGO_USER']}:{config['MONGO_PASSWORD']}@mongo_container:{config['MONGO_PORT']}/"
            )

    def connect(self):
        try:
            if self.client["forecast_users"] is not None:
                database = self.client["forecast_users"]
                collection = database["user_collection"]
                return collection
        except Exception as exception:
            response = error_handler(exception)

    def disconnect(self):
        try:
            self.client.close
        except Exception as exception:
            response = error_handler(exception)