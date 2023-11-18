from flask import request, jsonify, Blueprint
from services.quiz_service import QuizService


class QuizController:
    routes_bp = Blueprint('routes_quiz', __name__)

    @routes_bp.route('/api/v1/quiz', methods=['POST'])
    def create_quiz():
        if request.is_json:
            new_quiz = request.get_json()
            response, status_code = QuizService().insert_quiz(new_quiz)

            return response, status_code

    @routes_bp.route('/api/v1/login', methods=['PUT'])
    def authenticate_user():
        if request.is_json:
            user_request = request.get_json()
            response, status_code = LoginService().validate_user_to_login(user_request)

            return response, status_code

    @routes_bp.route('/api/v1/login/request/<string:mail>', methods=['GET'])
    def request_code(mail):

        response, status_code = ResetPasswordService().request_code(mail)

        return response, status_code

    @routes_bp.route('/api/v1/login/informations/<string:mail>', methods=['GET'])
    def user_informations(mail):

        response, status_code = LoginService().user_informations(mail)

        return response, status_code

    @routes_bp.route('/api/v1/login/decode/<string:mail>', methods=['PUT'])
    def validate_code(mail):
        if request.is_json:
            parameters_request = request.get_json()
            response, status_code = ResetPasswordService().validate_code(mail, parameters_request)

            return response, status_code

    @routes_bp.route('/api/v1/login/change/password/<string:mail>', methods=['PUT'])
    def change_password(mail):
        if request.is_json:
            password = request.get_json()
            response, status_code = ResetPasswordService().change_password(mail, password)

            return response, status_code

    @routes_bp.route('/api/v1/login/update/user/<string:mail>', methods=['PUT'])
    def update_user(mail):
        if request.is_json:
            parameters_request = request.get_json()
            response, status_code = LoginService().update_user(mail, parameters_request)

            return response, status_code

    @routes_bp.route('/api/v1/login/delete/<string:mail>', methods=['DELETE'])
    def delete_user(mail):
        response, status_code = LoginService().delete_user(mail)

        return response, status_code
