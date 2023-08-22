from repositories.login_repository import LoginRepository
from utils.reset_password_utils import ResetPasswordUtils
from flask import jsonify

class ResetPasswordService:
    reset_password_utils = ResetPasswordUtils()

    def request_code(self, email):
        validate = LoginRepository().get_user_with_email(email)

        if validate:
            send_request = self.reset_password_utils.validate_attempt(email)

            if send_request:
                return jsonify({"message": "Step by step to reset password sent to your email."}), 200
            else:
                return jsonify({"message": "Erro ao enviar e-mail"}), 404
        else:
            return jsonify({"message": "User not found."}), 404

    def create_request(self, email, password, code, date):
        new_request = ResetPassword(email, password, code, date)

        # validate = self.validate_attempt(email)
        #
        # if validate:
        #
        # else:
        #     response = self.collection.insert_one(new_request.__dict__)