class ComicController:
    @routes_bp.route('/api/v1/comic', methods=['POST'])
    def create_comic():
        if request.is_json:
            new_comic = request.get_json()
            response, status_code = LoginService().validate_user_to_insert(new_user)

            return response, status_code
