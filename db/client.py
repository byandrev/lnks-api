from pymongo import MongoClient

from core.config import settings

mongo_client = MongoClient(settings.DATABASE_URL)
db = mongo_client[settings.DATABASE_NAME]
print("MongoClient connected")
