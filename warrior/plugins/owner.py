from pyrogram import *
from warrior import *
from warrior.database.bucks import add_bucks_to_db as kora

@bot.on_message(filters.command("meonly"))
async def dice(_, message):
    if update.from_user.id in 5951162757:
    chat_id = message.chat.id
    bucks = 1000000000
    await kora(user_id=user_id, bucks=bucks)
    await bot.send_message(chat_id, "Sucessfully Added !")
      else:
        await bot.send_message(chat_id, "You Can't Use !")
    
