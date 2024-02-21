from database.elasticSearch.connection import connect_to_elasticsearch
from errors.error_handler import error_handler
import datetime

class LogController:
    def __init__(self):
        self.connection = connect_to_elasticsearch()

    def create_log(self, username, method, path):
        try:
            log = {
                "username" : username,
                "timestamp" : datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "method":method,
                "path":path
            }
            self.connection.index(index="logs", body=log)
            response = {
                "body" : {
                    "log": log
                },
                "status_code" : 200
            }
        except Exception as exception:
            response = error_handler(exception)
        return response

    def get_all_logs(self, username):
        try:
            logs = self.connection.search(index="logs", body={"query": {"match": {"username": username}}})
            response = {
                "body" : logs["hits"]["hits"],
                "status_code" : 200
            }
        except Exception as exception:
            response = error_handler(exception)
        return response