from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=7774029, cast=int)
API_HASH = config("API_HASH", default=531dbf42d387514dc43da07db9f2dc8f)
BOT_TOKEN = config("BOT_TOKEN", default=5347144880:AAFE8KTe2DCsNtJ8JFcR683j79GJ5C3rijE)
BOT_UN = config("BOT_UN", default=kapilcompress13bot)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
