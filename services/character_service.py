import requests
from flask import jsonify
from repositories.character_repository import CharacterRepository
import os
import base64
from dotenv import load_dotenv

dotenv_path = '.env'

load_dotenv(dotenv_path)


class CharacterService:

    def create_character(self, new_character, image):
        try:
            validate_character = CharacterRepository().validate_character(new_character['name'])

            if validate_character:
                return jsonify({"message": "Character already exists in the database"}), 409
            else:
                image_bytes = image.read()
                image_base64 = base64.b64encode(image_bytes).decode('utf-8')

                img_bb_api_url = 'https://api.imgbb.com/1/upload'
                data = {
                    'key': os.getenv('IMG_BB_KEY'),
                    'image': image_base64
                }
                upload = requests.post(img_bb_api_url, data=data)
                upload_json = upload.json()

                CharacterRepository().create_character(new_character['name'], new_character['biography'],
                                                       new_character['abillities_and_powers'],
                                                       new_character['affiliations'],
                                                       new_character['first_apparition'],
                                                       new_character['creators'],
                                                       upload_json['data']['image']['url'], new_character['height'],
                                                       new_character['weight'], new_character['strength'],
                                                       new_character['speed'], new_character['durability'],
                                                       new_character['agility'],
                                                       new_character['combat_experience'],
                                                       new_character['recovery'], new_character['intelligence'],
                                                       new_character['equipment'])

                return jsonify({"message": "Character inserted successfully"}), 201
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500
