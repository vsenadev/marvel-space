from run import create_mongo_client
from model.quiz_model import QuizModel
from repositories.log_repository import LogRepository


class QuizRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.collection = self.db["quiz"]
        self.log = LogRepository()

    def create_user(self, name, login, email, password):
        try:
            new_user = LoginModel(name, login, email, password)
            response = self.collection.insert_one(new_user.__dict__)
            return response
        except Exception as e:
            self.log.log_error(f"Error creating user: {str(e)}")

    def get_user_with_login(self, login):
        try:
            response = self.collection.find_one({"login": login})
            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving user by login: {str(e)}")

    def get_user_with_email(self, email):
        try:
            response = self.collection.find_one({"email": email})
            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving user by email: {str(e)}")

    def get_user_with_username(self, username):
        try:
            response = self.collection.find_one({"login": username})
            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving user by username: {str(e)}")

    def get_user_informations(self, mail):
        try:
            response = self.collection.find_one({"email": mail}, {"password": 0})
            return response
        except Exception as e:
            self.log.log_error(f"Error retrieving user information: {str(e)}")

    def check_login(self, mail, login):
        try:
            response = self.collection.find_one({"login": login, "email": {"$ne": mail}})
            return response
        except Exception as e:
            self.log.log_error(f"Error checking login: {str(e)}")

    def update_user(self, mail, login, name):
        try:
            user = {"mail": mail}
            update = {
                "$set": {
                    "login": login,
                    "name": name
                }
            }
            response = self.collection.update_one(user, update)
            return response
        except Exception as e:
            self.log.log_error(f"Error updating user: {str(e)}")

    def delete_user(self, mail):
        try:
            delete = {"email": mail}
            response = self.collection.delete_one(delete)
            return response
        except Exception as e:
            self.log.log_error(f"Error deleting user: {str(e)}")
