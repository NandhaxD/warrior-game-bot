
import uuid
from warrior import DATABASE

db = DATABASE["LOTTERY"]



async def add_lottery_to_db(bucks: int): 
    code = str(uuid.uuid4().hex)
    string = {"code": code, "bucks": bucks}
    db.insert_one(string)
    return code

async def remove_lottery_to_db(code: str):
      string = {"code": code}
      find = db.find_one(string)
      if find:
          db.delete_one(find)
          return True 
      else: 
         return False


async def get_lottery_code():
      code = [x for x in db.find()]
      return code
    
async def get_lotery_bucks(code):
      string = {"code": code}
      xxx = db.find(string)
      if xxx:
          return int(xxx["bucks"])
      else:
          return False
