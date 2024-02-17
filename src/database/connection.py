from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

class Connection():
    def __init__(self):
        self.client = MongoClient(config["DATABASE_URI"])

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