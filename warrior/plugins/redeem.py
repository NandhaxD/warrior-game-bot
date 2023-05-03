

from warrior import bot, prefix 
from warrior.database.redeem import add_redeem_to_db, remove_redeem_to_db, get_redeem_code
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

DEV_ID = [5696053228, 5951162757]

@bot.on_message(filters.command("generate", prefix) & filters.user(DEV_ID))
async def generate_redeem(_, message):
      username = (await bot.get_me()).username
      try:
          bucks = int(message.text.split(None,1)[1])
      except:
          return await message.reply_text("Example: /generate 1000.\n `This case you are creating a redeem token which has 1000 bucks`")
      code = await add_redeem_to_db(bucks)
      return await message.reply_text(f"🎊 New Redeem Token Arrived! 🎊\n💰 Bucks: `{bucks}`",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text=f"💰 {bucks} ⬅️", url=f"t.me/{username}/?start={code}")]]),quote=True)

@bot.on_message(filters.command("clear", prefix) & filters.user(DEV_ID))
async def clear_redeem(_, message):
       try:
          code = message.text.split(None,1)[1]
       except:
          return await message.reply_text("Example: /clear code.\n`Thid case your are deleting that redeem code.`")
       kk = await remove_redeem_to_db(code)
       if kk:
           return await message.reply_text("Successfully redeem token Removed! 🧑‍🏫", quote=True)
       else:
           return await message.reply_text(f"🚫 No Redeem Tokens Has: `{code}`", quote=True)


@bot.on_message(filters.command("redeems", prefix) & filters.user(DEV_ID))
async def get_redeems(_, message):
       code = await get_redeem_code()
       string = ""
       for user in code:
            string += "💰 {bucks}: `{token}`\n".format(bucks=user["bucks"], token=user["code"])
       string += "\nCurrentl Available Tokens ✅"
       return await message.reply_text(string)
