import asyncio
import os,time
import logging
from pyrogram import Client
from config import *
from database import connect_to_mongodb
from tools import split_video, generate_thumbnail, print_progress_bar
import subprocess
from myjd import (
    connect_to_jd,
    add_links,
    clear_downloads,
    process_and_move_links,
    check_for_new_links,
    check_downloads
)
from upload import progress
from scraper import fetch_page

# Setup logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Connect to MongoDB
db = connect_to_mongodb(MONGODB_URI, "Spidydb")
collection_name = COLLECTION_NAME

if db is not None:
    logging.info("Connected to MongoDB")

# Initialize the Telegram client
app = Client(
    name="JAVDLX-bot",
    api_hash=API_HASH,
    api_id=API_ID,
    bot_token=BOT_TOKEN,
    workers=30
)

async def start_download():
    async with app:
        try:
            # Connect to JD device
            jd = connect_to_jd(JD_APP_KEY, JD_EMAIL, JD_PASSWORD)
            device = jd.get_device(JD_DEVICENAME)
            logging.info('Connected to JD device')
            clear_downloads(device)

            url = "https://missav.com/dm559/en/uncensored-leak"
            suffix = "-uncensored-leak"
            jav_links = await fetch_page(url, suffix)
            jav_links = list(set(jav_links))
            logging.info(f"Total links found: {len(jav_links)}")
            linkgrabber = device.linkgrabber
            if jav_links:
                for url in jav_links[:3]:
                        response = add_links(device, url, "JAV")
                        check_for_new_links(device, linkgrabber)
                        process_and_move_links(device)
                        fies = check_downloads(device)
                        for i in fies:
                             for j in ["downloads/"+file for file in os.listdir("downloads")]:
                                  if i == j:
                                       print(i)
                        while True:                  
                            for file_path in ["downloads/"+file for file in os.listdir("downloads")]:
                                    logging.info(f"{file_path} is downloaded")
                                    if os.path.exists(file_path):
                                            try:
                                                logging.info(f"{file_path} is downloaded")
                                                logging.info(f"{file_path} is Spliting...")
                                                split_files = split_video(file_path)
                                                thumbnail_name = f"{os.path.basename(file_path)}_thumb.png"
                                                for file in split_files:
                                                    try:
                                                        
                                                        logging.info("Generating Thumbnail")
                                                        generate_thumbnail(file, thumbnail_name)
                                                        logging.info("Thumbnail generated")
                                                        
                                                        logging.info(f'Video File Size is {os.path.getsize(file)} bytes')
                                                        await app.send_photo(DUMP_ID,photo=thumbnail_name, progress=progress)
                                                        await app.send_video(DUMP_ID, file, thumb=thumbnail_name, progress=progress)
                                                    except Exception as e:
                                                    
                                                        logging.error(f"Error sending video {file}: {e}")
                                                    
                                                    finally:
                                                        if os.path.exists(file):
                                                            os.remove(file)
                                                if os.path.exists(file_path):
                                                    os.remove(file_path)
                                                if os.path.exists(thumbnail_name):
                                                    os.remove(thumbnail_name)
                                            except Exception as e:
                                                logging.error(f"Error processing upload for {file_path}: {e}")
        except Exception as e:
            logging.error(f"Error in start_download: {e}")

if __name__ == "__main__":
    app.run(start_download())
