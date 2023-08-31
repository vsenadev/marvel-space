from run import create_mongo_client
from model.reset_password_model import ResetPassword
from flask import jsonify


class ResetPasswordRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["reset"]

    def create_request(self, email, code, time_limit):
        new_request = ResetPassword(email, code, time_limit)

        validate = self.collection.find_one({"email": email})

        if validate:
            user = {"email": email}
            date_limit = {"time_limit": time_limit}
            update = {"$set": {
                "code": code,
                "time_limit": date_limit
            }}
            response = self.collection.update_one(user, update)

            return response
        else:
            response = self.collection.insert_one(new_request.__dict__)

            return response

