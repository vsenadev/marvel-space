from run import create_mongo_client
from model.character_model import CharacterModel
from repositories.log_repository import LogRepository


class CharacterRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["character"]
        self.log = LogRepository()

    def validate_character(self, name):
        try:
            response = self.collection.find_one({'name': name})
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def create_character(self, name, biography, abilities_and_powers, affiliations, first_apparition, creators, image,
                         height, weight, strenght, speed, durability, agility, combat_experience, recovery,
                         intelligence, equipment):
        try:
            new_character = CharacterModel(name, biography, abilities_and_powers, affiliations, first_apparition,
                                           creators, image, height, weight, strenght, speed, durability, agility,
                                           combat_experience, recovery, intelligence, equipment)
            response = self.collection.insert_one(new_character.__dict__)

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")
