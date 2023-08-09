from flask_cors import CORS
from flask import Flask, Blueprint
from controllers.login_controller import LoginController

app = Flask(__name__)
CORS(app)

app.register_blueprint(LoginController.routes_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3050)