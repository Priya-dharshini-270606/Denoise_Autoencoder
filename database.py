from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["dncnn_db"]
collection = db["denoised_images"]
