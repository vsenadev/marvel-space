from run import create_mongo_client

class LoginRepository:
    def __init__(self):
        self.db = create_mongo_client()
        collection = self.db["login"]

    def createUser(self, name, login, email, password):
        parameters = {
            "login": login,
            "password": password,
            "name": name,
            "email": email
        }
