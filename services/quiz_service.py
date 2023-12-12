from repositories.quiz_repository import QuizRepository
from repositories.login_repository import LoginRepository
from utils.quiz_utils import QuizUtils
from flask import jsonify
import bcrypt
import base64


class QuizService:

    @staticmethod
    def insert_quiz(new_quiz):
        try:
            validity = LoginRepository().get_user_with_username(new_quiz["login"])
            if validity:
                QuizRepository().create_quiz(new_quiz["name"], new_quiz["theme"], new_quiz["login"], new_quiz["question_list"])
                return jsonify({"message": "Quiz inserted successfully."}), 201
            else:
                return jsonify({"message": "User not found."}), 404
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    @staticmethod
    def get_quiz_list():
        try:
            quiz_list = QuizRepository().get_quiz_list()

            return jsonify({"quiz": quiz_list}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    def make_quiz(self, id_quiz, response, user):
        try:
            quiz = QuizRepository().get_quiz(id_quiz)

            if quiz:
                result_quiz = QuizUtils().validate_responses(quiz, response)
                insert_grade = QuizRepository().insert_result(result_quiz, user, id_quiz)

                response = QuizRepository().get_ten_top(id_quiz)
                print(response)
                return jsonify({"result": result_quiz, "ten_top": response}), 200
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

