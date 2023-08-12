from run import create_mongo_client
from model.login_model import LoginModel
from flask import jsonify


class LoginRepository:
    def __init__(self):
        self.db = create_mongo_client()

    def create_user(self, name, login, email, password):
        new_user = LoginModel(name,login, email, password)
        collection = self.db["login"]

        collection.insert_one(new_user.__dict__)

    def get_user_with_login(self, login):
        collection = self.db["login"]
        response = collection.find_one({"login": login})

        return response
