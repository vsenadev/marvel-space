from run import create_mongo_client
from model.login_model import LoginModel
from flask import jsonify


class LoginRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["login"]

    def create_user(self, name, login, email, password):
        new_user = LoginModel(name,login, email, password)

        response = self.collection.insert_one(new_user.__dict__)

        return response

    def get_user_with_login(self, login):
        response = self.collection.find_one({"login": login})

        return response

    def get_user_with_email(self, email):
        response = self.collection.find_one({"email": email})

        return response