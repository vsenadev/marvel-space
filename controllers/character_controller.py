from flask import request, jsonify, Blueprint
from services.character_service import CharacterService


class CharacterController:
    routes_bp = Blueprint('routes_character', __name__)

    @routes_bp.route('/character', methods=['POST'])
    def create_character():
        if request.is_json:
            new_character = request.get_json()
            response, status_code = CharacterService.create_character(new_character)

            return response, status_code
