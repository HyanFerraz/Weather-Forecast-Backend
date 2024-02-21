from typing import Dict
from database.mongoDB.connection import MongoConnection
from errors.error_handler import error_handler
from drivers.hash_password import hash_password, verify_password
from drivers.jwt_auth import create_jwt_token
import datetime

class UserController:
    def __init__(self):
        self.connection = MongoConnection()

    def create_new_user(self, username: str, password: str) -> Dict:
        try:
            collection = self.connection.connect()
            hashed_password = hash_password(password)
            if collection.find_one({"username" : username}) is None:
                collection.insert_one({
                    "username" : username,
                    "password" : hashed_password
                })
                response = {
                    "body" : {
                        "message" : "User Created"
                    }, 
                    "status_code" : 200
                }
            else:
                response = {
                    "body" : {
                        "message" : "User Already Exists"
                    },
                    "status_code" :  409
                }
        except Exception as exception:
            response = error_handler(exception)
        
        self.connection.disconnect()
        return response

    def login(self, username: str, password: str) -> Dict:
        try:
            collection = self.connection.connect()
            user = collection.find_one({"username" : username}) 
            if user:
                hashed_password = user["password"]
                is_correct = verify_password(password, hashed_password)
                if is_correct:
                    user_info = create_jwt_token(user["username"])
                    response = {
                        "body" : {
                            "username":user_info["username"],
                            "token" : user_info["token"],
                            "exp" : datetime.datetime.now() + datetime.timedelta(hours=1),
                        },
                        "status_code" : 200
                    }
                else:
                    response = {
                        "body" : {
                            "message" : "Incorrect Username/Password"
                        },
                        "status_code" : 401
                    }
            else:
                response = {
                    "body" : {
                        "message" : "Incorrect Username/Password"
                    },
                    "status_code" : 401
                }
        except Exception as exception:
            response = error_handler(exception)
        
        self.connection.disconnect()
        return response