
import asyncio

from warrior import bot, prefix 
from warrior.database.main import add_users_to_db, get_users_list
from warrior.database.bucks import get_bucks_from_users, add_bucks_to_db
from warrior.database.profile import add_profile_to_users, get_profile_from_users
from warrior.database.count_won_lose import get_won_count
from warrior.database.level import get_users_level
from warrior.database.lottery import get_lottery_code, get_lottery_bucks
from pyrogram import filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


EDIT_PFP = []

START_IMAGE = "https://i.imgur.com/muInEKC.jpeg"
START_TEXT = "<b>{name}</b>, Am I Warrior Game Bot I've Many Games In My Sides. Let's Start Playing? Tap /help"

async def ask_to_dm_first(message):
     username = (await bot.get_me()).username
     return await message.reply_text(
          "Start Me ⬅️", reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Click here!", url=f"t.me/{username}"),]]),)


@bot.on_message(filters.command("start", prefix))
async def start(_, message):
      user_id = int(message.from_user.id)
      mention = message.from_user.mention
      if message.chat.type == enums.ChatType.PRIVATE:
             token = await get_lottery_code()
             TOKEN_LIST = [x["code"] for x in token]
             try:
                 if bool(message.text.split(None,1)[1] in TOKEN_LIST):
                       bucks = await get_lottery_bucks(code=message.text.split(None,1)[1], user_id=user_id)
                       if bucks != False:
                            await add_bucks_to_db(user_id=user_id, bucks=bucks)
                            return await message.reply_text(f"🎊 Congratulations 🎊\nYou've Recived {bucks} 💰", quote=True)    
                       else: return await message.reply_text("⚔️ You've Already Recived This Lottery!")          
                 elif message.text.split(None,1)[1] == "help":                    
                      return await message.reply_text("*help message*")
             except:
                  pass
                  
                  
             if not user_id in (await get_users_list()):
                    await add_users_to_db(user_id)
                    return await message.reply_text("You Has Been Added To My Database, That Case You Got 500 Bucks 💰.") 
             else:
                 return await message.reply_photo(photo=START_IMAGE, 
                      caption=START_TEXT.format(name=mention))

      else:          
          return await message.reply_photo(photo=START_IMAGE, 
               caption=START_TEXT.format(name=mention))


@bot.on_message(filters.command("profile", prefix))
async def profile(_, message):
    user_id = message.from_user.id
    if user_id not in (await get_users_list()):
          return await ask_to_dm_first(message=message)
    else:
        msg = await message.reply_text("Analysing...")
        profile = await get_profile_from_users(user_id)
        bucks = await get_bucks_from_users(user_id)
        won_count = await get_won_count(user_id)
        level = await get_users_level(user_id)
        string = f"📛 <b>Name</b>: {message.from_user.mention}\n"
        string += f"✨ <b>Won count</b>: {won_count}\n"
        string += f"⚔️ <b>Level</b>: {level}\n"
        string += f"💰 <b>Bucks</b>: {bucks}\n"
        await message.reply_photo(
            photo=profile, caption=string, parse_mode=enums.ParseMode.HTML, 
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Settings ⚙️", callback_data=f"settings:{user_id}"),]]),)
        return await msg.delete()

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

