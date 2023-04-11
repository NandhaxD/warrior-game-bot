from warrior import bot, prefix
from warrior.database.bucks import add_bucks_to_users, get_bucks_from_users
from pyrogram import filters, enums



dice_users = []
@bot.on_message(filters.command("dice", prefix))
async def dice(_, message):
    user_id = message.from_user.id
    if user_id in dice_users:
        return await message.reply_text("Sorry Try Later You Already Played!")
    dice_users.append(user_id)
    xx = await message.reply_text("🎲")
    value = int(xx.value)
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
    await add_bucks_to_users(
        user_id=user_id,
        bucks=bucks)
    kk = await get_users_bucks(
            user_id=user_id)
    return await message.reply_text(
        f"You won: **{bucks}**\nTotal bucks: **{kk}**")
    
