from warrior import bot, GROUP_ID


if __name__ == "__main__":
     bot.run()
     with bot:
        bot.send_message(chat_id=GROUP_ID,
           text="Warrior Has Been Successfully Awakened!")
