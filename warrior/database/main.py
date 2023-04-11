from warrior import database

db = database["main"]

async def add_users_to_db(user_id: int):
     string = {"user_id": user_id, "coins": 500}
     db.insert_one(string)

async def get_users_list():
     list = [x["user_id"] for x in usersdb.find()]
     return list

