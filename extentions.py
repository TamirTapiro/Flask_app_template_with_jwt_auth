from flask_jwt_extended import JWTManager
from pymongo import MongoClient
import config
import ssl

jwt = JWTManager()
mongo_uri = config.DB_URI
client = MongoClient(mongo_uri, ssl_cert_reqs=ssl.CERT_NONE)

mydb = client[config.CURRENT_DB]
users_collection = mydb[config.USERS_COLLECTION]