import asyncio
import random

from warrior import DATABASE
db = DATABASE["FIGHT"]

from warrior.database.bucks import get_bucks_from_users, add_bucks_to_db


is_fighting = []


async def fight(message, symbol, from_user_id, replied_user_id):
    if from_user_id in is_fighting:
         await message.edit("You've fighting to someone please wait for next fight")
         return 
    elif replied_user_id in is_fighting:
         await message.edit("The user is fighting please wait while it is finished!")
         return 
    is_fighting.append(from_user_id) 
    is_fighting.append(replied_user_id)
    length = len(symbol)
    list = [from_user_id, replied_user_id]   
    won_user_id, lose_user_id = random.sample(list, 2)
    await add_bucks_to_db(user_id=won_user_id, bucks=1000)
    kk = await get_bucks_from_users(lose_user_id)
    bucks = int(kk)-1000
    await add_bucks_to_db(user_id=lose_user_id, bucks=bucks)
    info = await app.get_users([won_user_id, lose_user_id])
    name1 = info[0].first_name
    name2 = info[1].first_name
    string = f"""\u0020
⚔️ The fight was so interesting but the winner is {name1}, he defeated {name2} ⚔️

{name1} won: 1000
{name2} lose: 1000
"""
    
    for i in range(length):
           new_symbol = "⚉" * (length - i - 1) + symbol[i] + "⚉" * i
           await message.edit(new_symbol)
           await asyncio.sleep(3)
    await message.edit(string)
    is_fighting.remove(from_user_id) 
    is_fighting.remove(replied_user_id)
    



      

