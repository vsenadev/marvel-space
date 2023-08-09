from repositories.login_repository import LoginRepository
from flask import jsonify
import bcrypt
import base64

class LoginService:
    def validate_user_to_insert(self, new_user):
        validate = LoginRepository().get_user_with_login(new_user['login'])

        if validate:
            return jsonify({"message": "User already exists in the database"}), 409
        else:
            password = new_user["password"].encode('utf-8')
            encrypted = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, encrypted)
            string_hash = base64.b64encode(hashed).decode('utf-8')

            LoginRepository().create_user(new_user["name"], new_user["login"], new_user["email"], string_hash)
            return jsonify({"message": "User inserted successfully."}), 201

