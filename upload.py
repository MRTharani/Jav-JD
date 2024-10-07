import logging
from tools import split_video, generate_thumbnail, print_progress_bar
from config import *
from swibots import BotApp
import asyncio
import os,time
import subprocess



# Setup logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


bot = BotApp(TOKEN)







async def upload_progress_handler(progress, total):
    print_progress_bar("Uploading..",progress.current+progress.readed, total)


async def upload_thumb(file_path):
    if not os.path.isfile(file_path):
        raise Exception("File path not found")
    try:
        res = await bot.send_media(
            message=f"{os.path.basename(file_path)}",
            community_id=COMMUNITY_ID,
            group_id=GROUP_ID,
            document=file_path,
            )
        return res
    except Exception as e:
        raise Exception(e)


async def switch_upload(file_path,thumb):
    if not os.path.isfile(file_path):
        raise Exception("File path not found")
    try:
        res = await bot.send_media(
            message=f"{os.path.basename(file_path)}",
            community_id=COMMUNITY_ID,
            group_id=GROUP_ID,
            document=file_path,
            thumb=thumb,
            description=os.path.basename(file_path),
            part_size=512*1024*1024,
            task_count=20,
            progress=upload_progress_handler,
            progress_args=(os.path.getsize(file_path),)
            )
        return res
    except Exception as e:
        raise Exception(e)
