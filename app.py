from flask_cors import CORS
from flask import Flask, Blueprint
from controllers.login_controller import LoginController
from repositories.reset_password_repository import ResetPasswordRepository
import schedule
import threading

app = Flask(__name__)
CORS(app)

app.register_blueprint(LoginController.routes_bp)


def clear_reset_code():
    print("Tarefa de limpeza de códigos de redefinição executada com sucesso")
    ResetPasswordRepository().clear_codes()


schedule.every().day.at("02:15").do(clear_reset_code)


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()

    app.run(host='0.0.0.0', port=3050)
