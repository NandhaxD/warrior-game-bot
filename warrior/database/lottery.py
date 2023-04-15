from warrior import DATABASE
from warrior.helper.code_generate import generate_random_string 

db = DATABASE["LOTTERY"]



async def add_lottery_to_db(bucks: int): 
    code = generate_random_string()   
    string = {"code": code, "bucks": bucks}
    db.insert_one(string)


async def remove_lottery_to_db(code: str):
      string = {"code": code}
      find = db.find_one(string)
      if find:
          db.delete_one(find)
          return True 
      else: 
         return False


async def get_lottery_code():
      code = [x["code"] for x in db.find()]
      return code
    
