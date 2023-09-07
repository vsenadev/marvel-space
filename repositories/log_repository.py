from run import create_mongo_client
from model.login_model import LoginModel
from flask import jsonify


class LogRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["logs"]

    def log_error(self, message):
        log_entry = {
            "timestamp": datetime.datetime.now(),
            "message": message,
        }
        self.log_collection.insert_one(log_entry)
