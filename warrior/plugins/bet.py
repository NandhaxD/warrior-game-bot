
import random

from warrior import bot, prefix 
from warrior.plugins.main import ask_to_dm_first
from warrior.database.main import get_users_list
from warrior.database.bucks import add_bucks_to_db, get_bucks_from_users
from pyrogram import filters


won_users = []

async def winners_bucks(user_id: int, bucks_spend: int):
      count = won_users.count(user_id)
      bucks = bucks_spend*int(count)+2
      return bucks

@bot.on_message(filters.command("bet", prefix))
async def bet(_, message): 
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
          return await ask_to_dm_first(message)
    try:
          bucks_spend = int(message.text.split(None,1)[1])
    except:
          return await message.reply_text("🥸 Example: /bet 100", quote=True)
    if message.text.split(None,1)[1][0] == "-":
        return await message.reply_text("No!", quote=True)
    bucks_balance = await get_bucks_from_users(user_id)
    if bucks_balance > bucks_spend or bucks_balance == bucks_spend:
        mm = ["lose","lose","won", "pro"]
        key = random.choice(mm)
        if key.casefold() == "lose":
              await add_bucks_to_db(user_id, -bucks_spend)
              bucks = await get_bucks_from_users(user_id)
              await message.reply_text(f"🚫 You Lose {bucks_spend}. Your Current Bucks Balance `{bucks}`.")
              x = [m for m in won_users if m!= user_id]
              won_users.clear()
              cc = won_users + x
              return 
        elif key.casefold() == "pro":
               won_bucks = bucks_spend*10
               await add_bucks_to_db(user_id=user_id, bucks=won_bucks)
               bucks = await get_bucks_from_users(user_id)
               return await message.reply_text(f"🎊 Pro Bet UwU 🎊. ✨ You Won {won_bucks}, Your Current Bucks Balance `{bucks}`.", quote=True)
        elif key.casefold() == "won":
              won_users.append(user_id)
              won_bucks = await winners_bucks(user_id=user_id, bucks_spend=bucks_spend)
              await add_bucks_to_db(user_id=user_id, bucks=won_bucks)
              bucks = await get_bucks_from_users(user_id)
              return await message.reply_text(f"🎊 You Won: {won_bucks}, ✨ Your Current Balance Bucks {bucks}.", quote=True)
    else:
        return await message.reply_text("You Don't Have That Much Bucks! To Know Your Bucks Balance Click /record.")










