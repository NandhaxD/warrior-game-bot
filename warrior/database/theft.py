from warrior import DATABASE
db = DATABASE["THEFT"]


async def add_user_has_theft_to_user(user_id: int, theft_user_id: int):
        ff = db.find_one({"user_id": user_id})
        if ff:
           yy = db.find_one({"user_id": user_id})
           theft_user_ids = ff["theft_user_id"]
           theft_user_ids.append(user_id)
           filter = {"user_id": user_id}
           update = {"$set": {"theft_user_id": theft_user_ids}}
           db.update_one(filter, update)        
        else:
            string = {"user_id": user_id, "theft_user_id": [theft_user_id]}
            db.insert_one(string)
            
      

