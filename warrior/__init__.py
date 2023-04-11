import os
import logging


from pyrogram import Client 
from pymongo import MongoClient



#mongo database 
mongodb_url = "mongodb+srv://Kora:Kora@2008@kora.zbev3wd.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(mongodb_url)
database = mongo.warrior



FORMAT = "[Warrior]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")



bot = Client(
       name="warrior"
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=TOKEN,
       plugins=dict(root="warrior"),)


