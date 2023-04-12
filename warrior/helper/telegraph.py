
from telegraph import upload_file

async def telegraph(path):
     telegraph = await upload_file(path)
     for file_id in telegraph:
          url = "https://graph.org/" + file_id
     return url
