from flask import request, jsonify, Blueprint
from services.login_service import LoginService


class LoginController:
    routes_bp = Blueprint('routes', __name__)

    @routes_bp.route('/login', methods=['POST'])
    def create_user():
        if request.is_json:
            new_user = request.get_json()
            result, status_code = LoginService().validate_user_to_insert(new_user)
            return result, status_code

    @routes_bp.route('/login', methods=['PUT'])
    def authenticate_user():
        if request.is_json:
            user_request = request.get_json()
            result, status_code = LoginService().validate_user_to_login(user_request)

            return result, status_code