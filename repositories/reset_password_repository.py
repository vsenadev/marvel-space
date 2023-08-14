from run import create_mongo_client
from model.reset_password_repository import ResetPassword
from flask import jsonify


class ResetPasswordRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["reset"]

    def create_request(self, email, password, code, date):
        new_request = ResetPassword(email, password, code, date)

        validate = self.validate_attempt(email)

        if validate:

        else:
            response = self.collection.insert_one(new_request.__dict__)


    def validate_attempt(self, email):
        return self.collection.find({ email: email })

    def compare_code(self, email):

