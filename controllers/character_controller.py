from flask import request, jsonify, Blueprint
from services.character_service import CharacterService


class CharacterController:
    routes_bp = Blueprint('routes_character', __name__)

    @routes_bp.route('/api/v1/character', methods=['POST'])
    def create_character():
        if 'image' not in request.files:
            return 'No files sent'

        image = request.files['image']

        if image.filename == '':
            return 'No files sent'

        if request.is_json:
            new_character = request.get_json()
            response, status_code = CharacterService().create_character(new_character, image)

            return response, status_code
