from flask import request, jsonify, Blueprint
from services.character_service import CharacterService


class CharacterController:
    routes_bp = Blueprint('routes_character', __name__)
