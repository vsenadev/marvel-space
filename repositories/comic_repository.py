from run import create_mongo_client
from model.comic_model import ComicModel
from repositories.log_repository import LogRepository
from bson import ObjectId
import json


class ComicRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["comic"]
        self.log = LogRepository()

    def validate_comic(self, name):
        try:
            response = self.collection.find_one({'name': name})

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def create_comic(self, name, number, initial_final, launch, description, creators, image):
        try:
            new_comic = ComicModel(name, number, initial_final, launch, description, creators, image)
            print(new_comic)
            response = self.collection.insert_one(new_comic.__dict__)

            return response
        except Exception as e:
            self.log.log_error(f"Error creating comic: {str(e)}")

    def get_comic(self, comic_id):
        try:
            object_id = ObjectId(comic_id)
            response = self.collection.find_one({'_id': object_id}, {'_id': 0})

            response['creators'] = json.loads(response['creators'])

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_all_comics(self):
        try:
            response = []
            query = self.collection.find({}, {'description': 0, 'creators': 0})

            for find in query:
                find['_id'] = str(find['_id'])

                response.append(find)

            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")
