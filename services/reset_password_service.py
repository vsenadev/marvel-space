from repositories.login_repository import LoginRepository
from utils.reset_password_utils import ResetPasswordUtils
from utils.login_utils import LoginUtils
from repositories.reset_password_repository import ResetPasswordRepository
from flask import jsonify


class ResetPasswordService:
    def __init__(self):
        self.reset_password_utils = ResetPasswordUtils()
        self.reset_password_repository = ResetPasswordRepository()
        self.login_utils = LoginUtils()

    def request_code(self, email):
        try:
            validate_mail = LoginRepository().get_user_with_email(email)

            if validate_mail:
                send_request, code = self.reset_password_utils.validate_attempt(email)

                if send_request:
                    time_limit = self.reset_password_utils.get_time_limit()
                    self.reset_password_repository.create_request(email, code, time_limit)
                    return jsonify({"message": "Step by step to reset password sent to your email."}), 200
                else:
                    return jsonify({"message": "Error sending email."}), 404
            else:
                return jsonify({"message": "User not found."}), 404
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    def validate_code(self, mail, params):
        try:
            user = self.reset_password_repository.get_info_reset(mail)
            validate_time_limit = self.reset_password_utils.validate_time_limit(user['time_limit'])
            validate_code = self.reset_password_utils.compare_codes(params['code'], user['code'])

            if not validate_time_limit:
                return jsonify({"message": "Time limit exceeded, please request a new code."}), 400
            elif not validate_code:
                return jsonify({"message": "Code entered is incorrect."}), 400
            else:
                self.reset_password_repository.delete_request_code(mail)
                return jsonify({"message": "Correct information, you will be redirected to change your password."}), 200

        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    def change_password(self, mail, password):
        try:
            password_encrypted = self.login_utils.encrypt_password(password['password'])

            self.reset_password_repository.change_password(mail, password_encrypted)

            return jsonify({"message": "Password update successfully."}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500
