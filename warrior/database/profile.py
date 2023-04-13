from warrior import DATABASE
from warrior.helper.telegraph import telegraph 

db = DATABASE["MAIN"]

async def add_profile_to_users(message, user_id: int, profile):
     filter = {"user_id": user_id}
     link = await telegraph(profile)
     update = {"$set": {"profile": link}}
     db.update_one(filter, update)

async def get_profile_from_users(user_id: int):
      string = {"user_id": user_id}
      mm = db.find_one(string)
      try:
         return mm["profile"]
      except KeyError:
          return "https://graph.org//file/6b06c18453ebb6e6005da.jpg"
          
#k
