import os
import logging


from pyrogram import Client 
from pymongo import MongoClient


#prefix for commands
prefix = [".","!","?","*","$","#","/"]


#mongo database 
MONGODB_URL = "mongodb+srv://nandhaxd:rw5T7YJRjsE3fmk3@cluster0.80igexg.mongodb.net/?retryWrites=true&w=majority"
MONGO = MongoClient(MONGODB_URL)
DATABASE = MONGO.WARRIOR



FORMAT = "[Warrior]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")
GROUP_ID = os.getenv("GROUP_ID")



bot = Client(
       name="warrior",
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=TOKEN,
       plugins=dict(root="warrior"),)


