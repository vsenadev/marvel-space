import json
from bson import ObjectId
from run import create_mongo_client
from model.quiz_model import QuizModel
from model.grades_model import GradesModel
from repositories.log_repository import LogRepository


class QuizRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["quiz"]
        self.collection_result = self.db["grades"]
        self.log = LogRepository()

    def create_quiz(self, name, theme, login, question_list):
        try:
            new_user = QuizModel(name, theme, login, question_list)
            response = self.collection.insert_one(new_user.__dict__)
            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_quiz_list(self):
        try:
            response = []
            query = self.collection.find({}, {'login': 0, 'question_list': 0})

            for find in query:
                find['_id'] = str(find['_id'])

                response.append(find)

            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving quiz list: {str(e)}")

    def get_quiz(self, id_quiz):
        try:
            object_id = ObjectId(id_quiz)
            response = self.collection.find_one({"_id": object_id}, {'_id': 0, 'login': 0, 'name': 0, 'theme': 0})

            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving quiz by id: {str(e)}")

    def insert_result(self, result, user, quiz):
        try:
            new_grade = GradesModel(result, user, quiz)
            response = self.collection_result.insert_one(new_grade.__dict__)
            return response
        except Exception as e:
            self.log.log_error(f"Error insert quiz: {str(e)}")

    def get_ten_top(self, id_quiz):
        try:
            object_id = ObjectId(id_quiz)
            response = self.collection_result.find()

            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving user by email: {str(e)}")
