from pyrogram import *
from warrior import *
from warrior.database.bucks import add_bucks_to_db

@bot.on_message(filters.command("meonly"))
async def meonly(_, message):
#    if update.from_user.id in 5951162757:
    chat_id = message.chat.id
             bucks = random.randint(3*-spend, 4*spend)
         await add_bucks_to_db(user_id=user_id,
            bucks=bucks)
    await bot.send_message(chat_id, "Sucessfully Added !")
#    else:
#        await bot.send_message(chat_id, "You Can't Use !")
    
