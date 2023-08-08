from pymongo import MongoClient
import os
from dotenv import load_dotenv

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
database_url = os.environ.get('DATABASE_URL')

connection_string = 'mongodb+srv://{0}:{1}@{2}/?retryWrites=true&w=majority'.format(username, password, database_url)


def create_mongo_client():
    client = MongoClient(connection_string)
    database_name = "marvel"
    db = client[database_name]
    print('connect')
    return db
