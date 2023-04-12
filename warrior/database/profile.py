from warrior import DATABASE
from warrior.helper.telegraph import telegraph 

db = DATABASE["MAIN"]

async def add_profile_to_users(user_id: int, profile):
     filter = {"user_id": user_id}
     link = await telegraph(profile)
     update = {"$set": {"profile": link}}
     db.update_one(filter, update)
