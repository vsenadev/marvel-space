from run import create_mongo_client
from model.reset_password_model import ResetPassword
from flask import jsonify


class ResetPasswordRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["reset"]

    def create_request(self, mail, code, time_limit):
        new_request = ResetPassword(mail, code, time_limit)
        validate = self.collection.find_one({"email": mail})

        if validate:
            user = {"email": mail}
            update = {"$set": {
                "code": code,
                "time_limit": time_limit
            }}
            response = self.collection.update_one(user, update)

            return response
        else:
            response = self.collection.insert_one(new_request.__dict__)

            return response

    def get_info_reset(self, mail):
        response = self.collection.find_one({"email": mail}, {"_id": 0})

        return response

    def delete_request_code(self, mail):
        self.collection.delete_one({"email": mail})
