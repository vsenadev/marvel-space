from repositories.reset_password_service import ResetPasswordService
from repositories.login_repository import LoginRepository
from utils.reset_password_utils import ResetPasswordUtils
from flask import jsonify

class ResetPasswordService:
    reset_password_utils = ResetPasswordUtils()

    def request_code(self, email):
        validate = LoginRepository.find_by_email(email)

        if validate:
            # CONFIGURAR DISPARO DE E-MAIL
            call_generate_code = self.reset_password_utils.generate_code
            return jsonify({"message": "Step by step to reset password sent to your email."}), 200

    def create_request(self, email, password, code, date):
        new_request = ResetPassword(email, password, code, date)

        validate = self.validate_attempt(email)

        if validate:

        else:
            response = self.collection.insert_one(new_request.__dict__)