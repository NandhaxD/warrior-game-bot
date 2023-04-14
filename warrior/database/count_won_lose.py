
from warrior import DATABASE

db = DATABASE["MAIN"]

async def add_won_count(user_id: int, won_count: +1):
      x = db.find_one({"user_id": user_id})
      try:
         yy = x["won_count"]
      except:
         filter = {"user_id": user_id}
         update = {"$set": {"won_count": 1}}
         db.update_one(filter, update)
      won_count = int(yy)+1
      filter = {"user_id": user_id}
      update = {"$set": {"won_count": won_count}}
      db.update_one(filter, update)


async def add_lose_count(user_id: int, lose_count: +1):
      x = db.find_one({"user_id": user_id})
      try:
         yy = x["lose_count"]
      except:
         filter = {"user_id": user_id}
         update = {"$set": {"lose_count": 1}}
         db.update_one(filter, update)
      lose_count = int(yy)+1
      filter = {"user_id": user_id}
      update = {"$set": {"lose_count": lose_count}}
      db.update_one(filter, update)


async def get_won_count(user_id: int):
       string = {"user_id": user_id}
       x = db.find_one(string)
       counts = int(x["won_count"])
       return counts
