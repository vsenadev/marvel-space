from flask import request, jsonify, Blueprint
from services.login_service import LoginService
from services.reset_password_service import ResetPasswordService


class LoginController:
    routes_bp = Blueprint('routes', __name__)

    @routes_bp.route('/login', methods=['POST'])
    def create_user():
        if request.is_json:
            new_user = request.get_json()
            response, status_code = LoginService().validate_user_to_insert(new_user)

            return response, status_code

    @routes_bp.route('/login', methods=['PUT'])
    def authenticate_user():
        if request.is_json:
            user_request = request.get_json()
            response, status_code = LoginService().validate_user_to_login(user_request)

            return response, status_code

    @routes_bp.route('/login/request/<string:mail>', methods=['GET'])
    def request_code(mail):

        response, status_code = ResetPasswordService().request_code(mail)

        return response, status_code

    @routes_bp.route('/login/informations/<string:mail>', methods=['GET'])
    def user_informations(mail):

        response, status_code = LoginService().user_informations(mail)

        return response, status_code



    @routes_bp.route('/login/decode/<string:mail>', methods=['PUT'])
    def validate_code(mail):
        if request.is_json:
            parameters_request = request.get_json()
            response, status_code = ResetPasswordService().validate_code(mail, parameters_request)

            return response, status_code

    @routes_bp.route('/login/change/password/<string:mail>', methods=['PUT'])
    def change_password(mail):
        if request.is_json:
            password = request.get_json()
            response, status_code = ResetPasswordService().change_password(mail, password)

            return response, status_code
