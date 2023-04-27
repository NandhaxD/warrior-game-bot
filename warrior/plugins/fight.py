from pyrogram import filters
from warrior import bot, prefix 

from warrior.plugins.main import ask_to_dm_first
from warrior.database.main import get_users_list
from warrior.database.bucks import get_bucks_from_users
from warrior.database.fight import fight

@bot.on_message(filters.command("fight", prefix))
async def fighting(_, message):
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
         return await ask_to_dm_first(message)
    if not message.reply_to_message:
        
          return await message.reply("Reply to the User")
    replied_user_id = message.reply_to_message.from_user.id
    bucks = await get_bucks_from_users(user_id)

    if bucks < 1000:
         return await message.reply("you atleast hand 1000 bucks to fight!")

    bucks = await get_bucks_from_users(replied_user_id)
    if bucks < 1000:
         return await message.reply("you atleast hand 1000 bucks to fight!")

    from_user_id = user_id
    x = await message.reply("Let's Begin The Fight UwU")
    await fight(
         message=x,
         symbol="⚇⚇⚇⚇⚇⚇⚇⚇",
         from_user_id=from_user_id, 
         replied_user_id=replied_user_id
)
         
     
