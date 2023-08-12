import bcrypt
import base64
from flask import jsonify


class LoginUtils:
    def verify_password(self, input_password, hashed_password):
        password = input_password.encode('utf-8')
        hashed = base64.b64decode(hashed_password.encode('utf-8'))
        return bcrypt.checkpw(password, hashed)

    def compare_user_and_password(self, input_object, data_object):
        check = self.verify_password(input_object['password'], data_object['password'])
        if input_object['login'] == data_object['login'] and check:
            return jsonify({"message": "Authenticated user"}), 200
        else:
            return jsonify({"message": "Wrong username or password"}), 401
