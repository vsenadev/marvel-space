from run import create_mongo_client
from model.reset_password_repository import ResetPassword
from flask import jsonify


class ResetPasswordRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["reset"]

    def create_request(self, email, code, date):
        new_request = ResetPassword(email, code, date)

        validate = self.collection.find_one({"email": email})

        if validate:
            user = {"email": email}
            update = {"$set": {
                "code": code,
                "date": date
            }}
            response = self.collection.update_one(user, update)

            return response
        else:
            response = self.collection.insert_one(new_request.__dict__)

            return response

    # def compare_code(self, email):
