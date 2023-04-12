

from warrior import bot, prefix 
from warrior.database.main import add_users_to_db, get_users_list
from warrior.database.bucks import get_bucks_from_users
from pyrogram import filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

async def ask_to_dm_first(message):
     username = (await bot.get_me()).username
     return await message.reply_text(
          "Start Me!", reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Click here!", url=f"t.me/{username}"),]]),)


@bot.on_message(filters.command("start", prefix))
async def start(_, message):
      user_id = int(message.from_user.id)
      if message.chat.type == enums.ChatType.PRIVATE:
             if message.text.split(None,1)[1] == "help":                    
                    return message.reply_text("*help message*")
             if not user_id in (await get_users_list()):
                    await add_users_to_db(user_id)
                    return await message.reply_text("You Have Been Added To My Database. That Case You Got 500 Bucks.") 
             else:
                 return await message.reply_text("*you start message text here*")
      else:
          return await message.reply_text("*your start message text here*")


@bot.on_message(filters.command("record", prefix))
async def record(_, message):
    user_id = message.from_user.id
    default_pfp = "https://graph.org//file/6b06c18453ebb6e6005da.jpg"
    if user_id not in (await get_users_list()):
          return await ask_to_dm_first(message=message)
    else:
        bucks = await get_bucks_from_users(user_id)
        string = f"📛 **Name**: {message.from_user.mention}\n"
        string += f"💰 **bucks**: {bucks}\n"
        await message.reply_photo(
            photo=default_pfp, caption=string, parse_mode=enums.ParseMode.MARKDOWN, 
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Settings ⚙️", callback_data=f"settings"),]]),)




      
