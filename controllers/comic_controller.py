from flask import Blueprint, request
from services.comic_service import ComicService


class ComicController:
    routes_bp = Blueprint('routes_comic', __name__)

    @routes_bp.route('/api/v1/comic', methods=['POST'])
    def create_comic():
        if 'image' not in request.files:
            return 'No files sent', 400

        image = request.files['image']

        if image.filename == '':
            return 'No files sent', 400

        form_data = request.form.to_dict()

        response, status_code = ComicService().create_comic(form_data, image)

        return response, status_code

    @routes_bp.route('/api/v1/comic/<string:comic_id>', methods=['GET'])
    def get_comic(comic_id):
        response, status_code = ComicService().get_comic(comic_id)

        return response, status_code

    @routes_bp.route('/api/v1/comic', methods=['GET'])
    def get_all_comics():
        response, status_code = ComicService().get_all_comics()

        return response, status_code
