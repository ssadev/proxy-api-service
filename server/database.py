from pymongo import MongoClient
import settings

db_connection = MongoClient(settings.mongodb_uri)
db = db_connection[settings.db_name]
collection_ep = db["endpoints"]
