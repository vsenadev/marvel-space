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
