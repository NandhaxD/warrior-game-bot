

from warrior import bot, prefix 
from warrior.database.lottery import add_lottery_to_db, remove_lottery_to_db, get_lottery_code
from pyrogram import filters


@bot.on_message(filters.command("generate", prefix) & filters.user(5696053228))
async def generate_lottery(_, message):
      try:
          bucks = int(message.text.split(None,1)[1])
      except:
          return await message.reply_text("Example: /generate 1000.\n `This case you are creating a lottery token which has 1000 bucks`")
      code = await add_lottery_to_db(bucks)
      return await message.reply_text("🎊 Successfully lottery generated! 🎊\n👨‍💻 Code: `{code}`", quote=True)

@bot.on_message(filters.command("clear", prefix) & filters.user(5696053228))
async def clear_lottery(_, message):
       try:
          code = int(message.text.split(None,1)[1])
       except:
          return await message.reply_text("Example: /clear code.\n`This case are deleting the lottery token in db.`")
       kk = await remove_lottery_to_db(code)
       if kk:
           return await message.reply_text("Successfully lottery token Removed! 🧑‍🏫", quote=True)
       else:
           return await message.reply_text("🚫 No Token Active Has: `{code}`", quote=True)


@bot.on_message(filters.command("get_lotterys", prefix) & filters.user(5696053228))
async def get_lotterys(_, message):
       code = await get_lottery_code()
       return await message.reply_text(code)
