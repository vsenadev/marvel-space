import requests
from flask import jsonify
from repositories.character_repository import CharacterRepository
import os
from dotenv import load_dotenv

dotenv_path = '.env'

load_dotenv(dotenv_path)


class CharacterService:

    def create_character(new_character, image):
        try:
            validate_character = CharacterRepository().validate_character(new_character['name'])

            if validate_character:
                return jsonify({"message": "Character already exists in the database"}), 409
            else:
                img_bb_api_url = 'https://api.imgbb.com/1/upload'
                data = {
                    'key': os.getenv('IMG_BB_API_KEY'),
                    'image': image
                }

                upload = requests.post(img_bb_api_url, data=data)

                # CharacterRepository().create_character(new_character['name'], new_character['biography'],
                #                                        new_character['abillities_and_powers'], new_character['affiliations'],
                #                                        new_character['first_apparition'], new_character['creators'],
                #                                        new_character['image'], new_character['height'],
                #                                        new_character['weight'], new_character['strength'],
                #                                        new_character['speed'], new_character['durability'],
                #                                        new_character['agility'], new_character['combat_experience'],
                #                                        new_character['recovery'], new_character['intelligence'],
                #                                        new_character['equipment'])

                return jsonify({"message": "Character inserted successfully"}), 201
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500
