from flask import request, jsonify, Blueprint
from services.quiz_service import QuizService


class QuizController:
    routes_bp = Blueprint('routes_quiz', __name__)

    @routes_bp.route('/api/v1/quiz', methods=['POST'])
    def create_quiz():
        if request.is_json:
            new_quiz = request.get_json()
            response, status_code = QuizService().insert_quiz(new_quiz)

            return response, status_code

    @routes_bp.route('/api/v1/login', methods=['PUT'])
    def authenticate_user():
        if request.is_json:
            user_request = request.get_json()
            response, status_code = LoginService().validate_user_to_login(user_request)

            return response, status_code

    @routes_bp.route('/api/v1/quiz/list', methods=['GET'])
    def get_quiz_list():
        response, status_code = QuizService().get_quiz_list()

        return response, status_code

    @routes_bp.route('/api/v1/quiz/make/<string:id_quiz>', methods=['PUT'])
    def make_quiz(id_quiz):
        if request.is_json:
            answers = request.get_json()

            response, status_code = QuizService().make_quiz(id_quiz, answers['response'], answers['user'])

            return response, status_code
