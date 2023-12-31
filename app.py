from flask_cors import CORS
from flask import Flask, Blueprint, send_from_directory
from controllers.documentation_controller import DocumentationController
from controllers.login_controller import LoginController
from controllers.character_controller import CharacterController
from controllers.quiz_controller import QuizController
from controllers.comic_controller import ComicController
from repositories.reset_password_repository import ResetPasswordRepository
import schedule
import threading
import time

app = Flask(__name__)
CORS(app)

app.register_blueprint(DocumentationController.routes_bp)
app.register_blueprint(LoginController.routes_bp)
app.register_blueprint(CharacterController.routes_bp)
app.register_blueprint(QuizController.routes_bp)
app.register_blueprint(ComicController.routes_bp)


def clear_reset_code():
    ResetPasswordRepository().clear_codes()


schedule.every().day.at("23:59").do(clear_reset_code)


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()
    DebugController = True
    app.run(host='192.168.100.71', port=3050)
