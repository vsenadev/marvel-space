from repositories.login_repository import LoginRepository
from utils.login_utils import LoginUtils
from flask import jsonify
import bcrypt
import base64


class LoginService:
    login_utils = LoginUtils()

    def validate_user_to_insert(self, new_user):
        try:
            validate = LoginRepository().get_user_with_login(new_user['login'])

            if validate:
                return jsonify({"message": "User already exists in the database"}), 409
            else:
                password = self.login_utils.encrypt_password(new_user['password'])

                LoginRepository().create_user(new_user["name"], new_user["login"], new_user["email"], password)
                return jsonify({"message": "User inserted successfully."}), 201
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    def validate_user_to_login(self, user_validate):
        try:
            validate = LoginRepository().get_user_with_login(user_validate['login'])

            if validate:
                validity = login_utils.compare_user_and_password(user_validate, validate)
                if validity:
                    jsonify({"message": "Authenticated user"}), 200
                else:
                    jsonify({"message": "Wrong username or password"}), 401

            else:
                return jsonify({"message": "User not found."}), 404
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500
