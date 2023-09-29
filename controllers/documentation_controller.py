from flask import Blueprint, send_from_directory


class DocumentationController:
    routes_bp = Blueprint('routes_documentation', __name__)

    @routes_bp.route('/documentation')
    def main_page():
        return send_from_directory('./documentation', 'index.html')

    @routes_bp.route('/reset')
    def reset():
        return send_from_directory('./documentation/static', 'reset.css')

    @routes_bp.route('/style')
    def style():
        return send_from_directory('./documentation/static', 'style.css')

    @routes_bp.route('/main')
    def javascript():
        return send_from_directory('./documentation/static', 'main.js')
