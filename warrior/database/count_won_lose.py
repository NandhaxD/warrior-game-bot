
from warrior import DATABASE

db = DATABASE["MAIN"]

async def add_won_count(user_id: int, won_count: int):
      x = db.find_one({"user_id": user_id})
      try:
         yy = x["won_count"]
      except KeyError:
          filter = {"user_id": user_id}
          update = {"$set": {"won_count": 0}}
          db.update_one(filter, update)

      x = db.find_one({"user_id": user_id})
      yy = x["won_count"]
      won_count = int(yy)+1
      filter = {"user_id": user_id}
      update = {"$set": {"won_count": won_count}}
      db.update_one(filter, update)


async def add_lose_count(user_id: int, lose_count: int):
      x = db.find_one({"user_id": user_id})
      try:
         yy = x["lose_count"]
      except KeyError:
           filter = {"user_id": user_id}
           update = {"$set": {"lose_count": +0}}
           db.update_one(filter, update)

      x = db.find_one({"user_id": user_id})
      yy = x["lose_count"]
      lose_count = int(yy)+1
      filter = {"user_id": user_id}
      update = {"$set": {"lose_count": lose_count}}
      db.update_one(filter, update)


async def get_won_count(user_id: int):
       string = {"user_id": user_id}
       x = db.find_one(string)
       try:
          counts = int(x["won_count"])
       except KeyError:
            await add_won_count(user_id, +0)
            string = {"user_id": user_id}
            x = db.find_one(string)
            counts = int(x["won_count"])
            return counts
       string = {"user_id": user_id}
       x = db.find_one(string)
       counts = int(x["won_count"])
       return counts

async def get_lose_count(user_id: int):
       string = {"user_id": user_id}
       x = db.find_one(string)
       try:
          counts = int(x["lose_count"])
       except KeyError:
            await add_lose_count(user_id, +0)
            string = {"user_id": user_id}
            x = db.find_one(string)
            counts = int(x["lose_count"])
            return counts
       string = {"user_id": user_id}
       x = db.find_one(string)
       counts = int(x["lose_count"])
       return counts


async def get_bet_count(user_id: int):
       won_count = await get_won_count(user_id)
       lose_count = await get_lose_count(user_id)
       bet_count = int(won_count)+int(lose_count)
       return bet_count


