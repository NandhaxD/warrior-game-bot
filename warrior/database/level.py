from warrior import DATABASE

db = DATABASE["MAIN"]

async def level_system(bet_count: int):
    list = [0, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for lvl , list in enumerate(list):
       if bet_count > list:
             level = lvl
    return level 

async def add_level_to_db(user_id: int, level: int):
      mm = db.find_one({"user_id": user_id})
      try:
          mm["level"]
      except KeyError:
          filter = {"user_id": user_id}
          update = {"$set": {"level": 0}}
          db.update_one(filter, update)        
      mm = db.find_one({"user_id": user_id})
      lvl = int(mm["level"])+level
      filter = {"user_id": user_id}
      update = {"$set": {"level": lvl}}
      db.update_one(filter, update)

async def get_users_level(user_id: int):
      mm = db.find_one({"user_id": user_id})
      try:
          mm["level"]
      except KeyError:
          filter = {"user_id": user_id}
          update = {"$set": {"level": 0}}
          db.update_one(filter, update)
      mm = db.find_one({"user_id": user_id})
      level = mm["level"]
      return level


       

