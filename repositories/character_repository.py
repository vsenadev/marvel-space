from run import create_mongo_client
from model.character_model import CharacterModel
from repositories.log_repository import LogRepository
from bson import ObjectId
import json


class CharacterRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["character"]
        self.log = LogRepository()

    def validate_character(self, name):
        try:
            response = self.collection.find_one({'name': name})

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def create_character(self, name, biography, abilities_and_powers, affiliations, first_apparition, creators, image,
                         height, weight, strenght, speed, durability, agility, combat_experience, recovery,
                         intelligence, equipment, created_by):
        try:
            new_character = CharacterModel(name, biography, abilities_and_powers, affiliations, first_apparition,
                                           creators, image, height, weight, strenght, speed, durability, agility,
                                           combat_experience, recovery, intelligence, equipment, created_by)

            response = self.collection.insert_one(new_character.__dict__)

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_character(self, character_id):
        try:
            object_id = ObjectId(character_id)
            response = self.collection.find_one({'_id': object_id}, {'_id': 0})

            response['abilities_and_powers'] = json.loads(response['abilities_and_powers'])
            response['affiliations'] = json.loads(response['affiliations'])
            response['creators'] = json.loads(response['creators'])

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_character_with_filter(self, field):
        try:
            response = []
            query = self.collection.find().sort(field, -1)

            for find in query:
                find['_id'] = str(find['_id'])
                find['abilities_and_powers'] = json.loads(find['abilities_and_powers'])
                find['affiliations'] = json.loads(find['affiliations'])
                find['creators'] = json.loads(find['creators'])

                response.append(find)

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_all_characters(self):
        try:
            response = []
            query = self.collection.find()

            for find in query:
                find['_id'] = str(find['_id'])
                find['abilities_and_powers'] = json.loads(find['abilities_and_powers'])
                find['affiliations'] = json.loads(find['affiliations'])
                find['creators'] = json.loads(find['creators'])

                response.append(find)

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_character_for_battle(self, character_id):
        try:
            object_id = ObjectId(character_id)
            response = self.collection.find_one({'_id': object_id}, {'_id': 0, 'biography': 0, 'image': 0, 'first_apparition': 0, 'created_by': 0, 'creators': 0})

            response['abilities_and_powers'] = json.loads(response['abilities_and_powers'])
            response['abilities_and_powers'] = len(response['abilities_and_powers'])
            response['affiliations'] = json.loads(response['affiliations'])
            response['affiliations'] = len(response['affiliations'])

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")
