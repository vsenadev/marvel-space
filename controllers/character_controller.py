from flask import request, jsonify, Blueprint
from services.character_service import CharacterService


class CharacterController:
    routes_bp = Blueprint('routes_character', __name__)

    @routes_bp.route('/api/v1/character', methods=['POST'])
    def create_character():
        if 'image' not in request.files:
            return 'No files sent', 400

        image = request.files['image']

        if image.filename == '':
            return 'No files sent', 400

        form_data = request.form.to_dict()

        response, status_code = CharacterService().create_character(form_data, image)

        return response, status_code

    @routes_bp.route('/api/v1/character/<string:character_id>', methods=['GET'])
    def get_character(character_id):
        response, status_code = CharacterService().get_character(character_id)

        return response, status_code

    @routes_bp.route('/api/v1/character/filter/<string:field>', methods=['GET'])
    def get_character_with_filter(field):
        response, status_code = CharacterService().get_character_with_filter(field)

        return response, status_code

    @routes_bp.route('/api/v1/character', methods=['GET'])
    def get_all_characters():
        response, status_code = CharacterService().get_all_characters()

        return response, status_code

    @routes_bp.route('/api/v1/character/battle', methods=['POST'])
    def battle():
        if request.is_json:
            battle_body = request.get_json()
            response, status_code = CharacterService().battle(battle_body)

            return response, status_code
