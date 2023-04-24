from pyrogram import filters
from warrior import app, prefix 

from warrior.main import ask_dm_to_first
from warrior.database.main import get_users_list
from warrior.database.fight import fight

@app.on_message(filters.command("fight", prefix))
async def fight(_, message):
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
         return await ask_dm_to_first(message)
    if (not message.reply_to_message or 
            message.reply_to_message.from_user.is_bot == True):
        
          return await message.reply("Reply to the User")
    replied_user_id = message.reply_to_message.from_user.id
    from_user_id = user_id
    return await fight(
         message=message,
         symbol="⚇⚇⚇⚇⚇⚇⚇⚇",
         from_user_id=from_user_id, 
         replied_user_id=replied_user_id)
         
     
