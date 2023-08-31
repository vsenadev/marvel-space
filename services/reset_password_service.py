from repositories.login_repository import LoginRepository
from utils.reset_password_utils import ResetPasswordUtils
from repositories.reset_password_repository import ResetPasswordRepository
from flask import jsonify


class ResetPasswordService:
    def __init__(self):
        self.reset_password_utils = ResetPasswordUtils()
        self.reset_password_repository = ResetPasswordRepository()

    def request_code(self, email):
        try:
            validate = LoginRepository().get_user_with_email(email)

            if validate:
                send_request, code = self.reset_password_utils.validate_attempt(email)

                if send_request:
                    time_limit = self.reset_password_utils.get_time_limit()
                    self.reset_password_repository.create_request(email, code, time_limit)
                    return jsonify({"message": "Step by step to reset password sent to your email."}), 200
                else:
                    return jsonify({"message": "Error sending email"}), 404
            else:
                return jsonify({"message": "User not found."}), 404
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500
