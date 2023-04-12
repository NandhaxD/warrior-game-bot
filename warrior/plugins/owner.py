from pyrogram import *
from warrior import *
from warrior.database.bucks import add_bucks_to_db

@bot.on_message(filters.command("meonly"))
async def meonly(_, message):
    chat_id = message.chat.id    
    bucks = 100000000
    await add_bucks_to_db(user_id=user_id,
            bucks=bucks)
    await bot.send_message(chat_id, "Sucessfully Added !")
