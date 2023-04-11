

from warrior import bot, prefix 
from warrior.database.main import add_users_to_db, get_users_list
from pyrogram import filters, enums 

async def ask_to_dm_first(message):
     username = (await bot.get_me()).username
     return await message.reply_text(
          "First Dm Me", reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Click here!", url=f"t.me/{username}"),]]),)


@bot.on_message(filters.command("start", prefix))
async def start(_, message):
      user_id = int(message.from_user.id)
      if message.chat.type == enums.ChatType.PRIVATE:
             if not user_id in (await get_users_list()):
                    await add_users_to_db(user_id)
                    return await message.reply_text("You Have Been Added To My Database. That Case You Got 500 Bucks.") 
             else:
                 return await message.reply_text("*you start message text here*")
      else:
          return await message.reply_text("*your start message text here*")

