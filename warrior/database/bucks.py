from warrior import database


db = database["main"]


async def get_bucks_from_users(user_id: int):
     string = {"user_id": user_id}
     xx = db.find_one(string)
     mm = int(xx["bucks"])
     return mm

async def add_bucks_to_db(user_id: int, bucks: int):
        xx = await get_bucks_from_users(user_id)
        total_bucks = xx+bucks
        string = {"user_id": user_id}, {"$set":{"bucks": total _bucks}}
        db.update_one(string)
