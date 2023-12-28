from flask import Blueprint, request
from services.comic_service import ComicService

class ComicController:
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
