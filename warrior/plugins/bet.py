
import random

from warrior import bot, prefix 
from warrior.plugins.main import ask_to_dm_first
from warrior.database.main import get_users_list
from warrior.database.bucks import add_bucks_to_db, get_bucks_from_users
from pyrogram import filters


@bot.on_message(filters.command("bet", prefix))
async def bet(_, message):
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
        return await ask_to_dm_first(message)
    try:
       spend = int(message.text.split(None,1)[1])
    except:
         return await message.reply_text("It Must Be Integer.\nExample: /Bet 1000")
    if message.text.split(None,1)[1][0] == "-":
        return await message.reply_text("You Cannot Do This! 🚫")
    hand = await get_bucks_from_users(user_id)
    if hand > spend:
         bucks = random.randrange(3*-spend, 4*spend)
         await add_bucks_to_db(user_id=user_id,
            bucks=bucks)
         kk = await get_bucks_from_users(user_id)
         if str(bucks)[0] == "-":
             return await message.reply_text(f"You lose 🚫: **{bucks}**\nTotal Bucks 💰: **{kk}**")
         else:
             return await message.reply_text(f"You won ✅: **{bucks}**\nTotal Bucks 💰: **{kk}**")
    else:
       return await message.reply_text("You Don't Have That Much Bucks! 💰")
