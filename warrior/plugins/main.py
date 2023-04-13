
import asyncio

from warrior import bot, prefix 
from warrior.database.main import add_users_to_db, get_users_list
from warrior.database.bucks import get_bucks_from_users, add_bucks_to_db
from warrior.database.profile import add_profile_to_users, get_profile_from_users
from pyrogram import filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


EDIT_PFP = []

async def ask_to_dm_first(message):
     username = (await bot.get_me()).username
     return await message.reply_text(
          "Start Me!", reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Click here!", url=f"t.me/{username}"),]]),)


@bot.on_message(filters.command("start", prefix))
async def start(_, message):
      user_id = int(message.from_user.id)
      if message.chat.type == enums.ChatType.PRIVATE:
             try:     
                if message.text.split(None,1)[1] == "help":                    
                    return await message.reply_text("*help message*")
             except: 
                  pass
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
    if user_id not in (await get_users_list()):
          return await ask_to_dm_first(message=message)
    else:
        profile = await get_profile_from_users(user_id)
        bucks = await get_bucks_from_users(user_id)
        string = f"📛 <b>Name</b>: {message.from_user.mention}\n"
        string += f"💰 <b>Bucks</b>: {bucks}\n"
        return await message.reply_photo(
            photo=profile, caption=string, parse_mode=enums.ParseMode.HTML, 
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Settings ⚙️", callback_data=f"settings:{user_id}"),]]),)


@bot.on_callback_query(filters.regex("settings"))
async def settings(_, query):
     user_id = query.from_user.id
     mm = int(query.data.split(":")[1])
     if user_id != mm:
           return await query.answer("No, You Can Edit's Others!") 
     else:
         await query.message.edit_text("Settings ⚙️",reply_markup=InlineKeyboardMarkup(
         [[InlineKeyboardButton("🧑‍🏫 Edit Profile", callback_data=f"edit_pfp:{user_id}"),]]),)


@bot.on_callback_query(filters.regex("edit_pfp"))
async def edit_pfp(_, query):   
       user_id = query.from_user.id
       chat_id = query.message.chat.id
       mm = int(query.data.split(":")[1])
       if user_id != mm:
           return await query.answer("No, cannot do this!")
       bucks = await get_bucks_from_users(user_id)
       if bucks < 1000:
             return await query.answer("🚫 You Need 1000 Bucks To Change Your Profile!", show_alert=True)
       else:
           await query.message.delete()
           EDIT_PFP.append(user_id)           
           yy = await query.message.reply("Reply With Photo:\n To Save Profile! ")
           await asyncio.sleep(30)
           if user_id in EDIT_PFP:
                 await yy.edit_text("Timeout Try Again. 🚫")
                 try:
                    EDIT_PFP.remove(user_id)
                 except: 
                     pass
                 return 
           else:
              return 

@bot.on_message(filters.photo & filters.reply)
async def set_pfp(_, message):
     user_id = message.from_user.id
     if user_id in EDIT_PFP:
            profile= await message.download()   
            await add_profile_to_users(message, user_id, profile)
            await add_bucks_to_db(user_id, -1000)
            await message.reply_to_message.delete()
            bucks = await get_bucks_from_users(user_id)
            await message.reply_text(f"Successfully Profile Saved! ✅\n  💰 Your Current Bucks: {bucks}")  
            EDIT_PFP.remove(user_id)
     else:
         return 

