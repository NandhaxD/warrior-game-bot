from json import JSONDecodeError
from telegraph import upload_file

async def telegraph(message, path):
     try:
       telegraph = upload_file(path)
     except JSONDecodeError:
             return await message.reply_text("Failed To Upload Profile In Telegraph. 🚫")
     for file_id in telegraph:
          url = "https://graph.org/" + file_id
     return url
