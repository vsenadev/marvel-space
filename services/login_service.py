from repositories.login_repository import LoginRepository
from utils.login_utils import LoginUtils
from flask import jsonify
import bcrypt
import base64


class LoginService:

    @staticmethod
    def validate_user_to_insert(new_user):
        try:
            validate_login = LoginRepository().get_user_with_login(new_user['login'])
            validate_mail = LoginRepository().get_user_with_email(new_user['email'])

            if validate_login:
                return jsonify({"message": "Login already exists in the database"}), 409
            elif validate_mail:
                return jsonify({"message": "Mail already exists in the database"}), 409
            else:
                password = LoginUtils().encrypt_password(new_user['password'])

                LoginRepository().create_user(new_user["name"], new_user["login"], new_user["email"], password)
                return jsonify({"message": "User inserted successfully."}), 201
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    @staticmethod
    def validate_user_to_login(user_validate):
        try:
            validate = LoginRepository().get_user_with_login(user_validate['login'])

            if validate:
                validity = LoginUtils().compare_user_and_password(user_validate, validate)
                if validity:
                    jsonify({"message": "Authenticated user"}), 200
                else:
                    jsonify({"message": "Wrong username or password"}), 400

            else:
                return jsonify({"message": "User not found."}), 404
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    @staticmethod
    def user_informations(mail):
        try:
            user = LoginRepository().get_user_informations(mail)
            user["_id"] = str(user["_id"])

            return jsonify({"user": user}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    @staticmethod
    def update_user(mail, params):
        try:
            existing_login = LoginRepository().check_login(mail, params['login'])

            if existing_login:
                return jsonify({"message": "Login already exists in database"}), 409
            else:
                LoginRepository().update_user(mail, params['login'], params['name'])

                return jsonify({"message": "User successfully edited"}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    @staticmethod
    def delete_user(mail):
        try:
            validate_mail = LoginRepository().get_user_with_email(mail)

            if not validate_mail:
                return jsonify({"message": "User does not exist"}), 400
            else:
                LoginRepository().delete_user(mail)

                return jsonify({"message": "Successfully deleted user"}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

