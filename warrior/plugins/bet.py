from warrior import bot, prefix 
from warrior.plugins.main import ask_to_dm_first
from warrior.database.main import get_users_list
from warrior.database.bucks import add_bucks_to_db
from pyrogram import filters


@bot.on_message(filters.command("bet", prefix))
async def bet(_, message):
    user_id = message.from_user.id
    try:
       spend_bucks = int(message.text.split(None,1)[1])
    except:
         return await message.reply_text("Read help!")
