import asyncio 

from warrior import bot, prefix
from warrior.database.bucks import add_bucks_to_db, get_bucks_from_users
from warrior.database.main import get_users_list
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


async def ask_to_dm_first(message):
     username = (await bot.get_me()).username
     return await message.reply_text(
          "First Dm Me", reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Click here!", url=f"t.me/{username}"),]]),)


dice_users = []
@bot.on_message(filters.command("dice", prefix))
async def dice(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id in (await get_users_list()):
         return await ask_to_dm_first(message=message)
    if user_id in dice_users:
        return await message.reply_text("Sorry Try Later You Already Played!")
    dice_users.append(user_id)    
    xx = await bot.send_dice(chat_id=chat_id)
    value = int(xx.dice.value)
    if value == 1:
         bucks = 10000
    elif value == 2:
         bucks = 2000
    elif value == 3:
         bucks = 3000
    elif value == 4:
          bucks = 4000
    elif value == 5:
         bucks = 5000
    elif value == 6:
         bucks = 6000
    await add_bucks_to_db(
        user_id=user_id,
        bucks=bucks)
    kk = await get_bucks_from_users(
            user_id=user_id)
    await message.reply_text(
        f"You won: **{bucks}**\nTotal bucks: **{kk}**")
    await asyncio.sleep(10*60)
    dice_users.remove(user_id)
    return 
