import requests
from flask import jsonify
from repositories.comic_repository import ComicRepository
from utils.character_utils import CharacterUtils
import os
import base64
import json
from dotenv import load_dotenv

dotenv_path = '.env'

load_dotenv(dotenv_path)


class ComicService:
    def create_comic(self, new_comic, image):
        try:
            validate_comic = ComicRepository().validate_comic(new_comic['name'])

            if validate_comic:
                return jsonify({"message": "Comic already exists in the database"}), 409
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

                ComicRepository().create_comic(new_comic['name'], new_comic['number'],
                                               new_comic['initial_final'],
                                               new_comic['launch'],
                                               new_comic['description'],
                                               new_comic['creators'],
                                               upload_json['data']['image']['url'])

                return jsonify({"message": "Comic inserted successfully"}), 201
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    def get_comic(self, comic_id):
        try:
            comic = ComicRepository().get_comic(comic_id)

            return jsonify({"comic": comic}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500

    def get_all_comics(self):
        try:
            comics = ComicRepository().get_all_comics()

            return jsonify({"comics": comics}), 200
        except Exception as error:
            return jsonify({"message": "An error has occurred: {0}".format(error)}), 500
