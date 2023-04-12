from pyrogram import *
from warrior import *
from warrior.database.bucks import add_bucks_to_db

@bot.on_message(filters.command("only", prefix))
async def meonly(_, message):
    chat_id = message.chat.id    
    bucks = 100000000
    await add_bucks_to_db(user_id=user_id,
            bucks=bucks)
    kk = await get_bucks_from_users(user_id)
         if str(bucks)[0] == "-":
             return await message.reply_text(f"You Win ✅: **{bucks}**\nTotal Bucks 💰: **{kk}**")
         else:
             return await message.reply_text(f"You Win ✅: **{bucks}**\nTotal Bucks 💰: **{kk}**")
