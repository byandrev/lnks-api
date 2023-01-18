from pymongo import MongoClient

from core.config import settings


try:
    mongo_client = MongoClient(settings.DATABASE_URL)
    db = mongo_client[settings.DATABASE_NAME]
    print("MongoClient connected")
except:
    print("error to connect the MongoClient")
