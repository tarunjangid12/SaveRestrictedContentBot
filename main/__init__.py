#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23696595
API_HASH = "a5b4f74cd5b550622c4eee4fea7285b0"
BOT_TOKEN = "6743200249:AAFegGMnnYHaHZ_zqH8lYk9sMx1CVLm1SD4"
SESSION = "AQFplNMAe9dQ-mut2Ma2Mtw9S8sUzs-oFu_HVSmyhu3j94lO7Kl3b8SijG9Ywe59TwHObzIuyPEfkh9tB4VOljZmrzXD-8CmELVJPRZt3JUL9OqLYuQyaSLCD-Es1luVhs-Z_pbGo6k-2VAFvvpQ_u3QOfRd8I10x9oFKSk1ETH7kT8x58LfB2R_JEGunOcprJjlsSSxoKuIObOwRK7K7YdUJe6H57jQLI6uWNUk3UMHapXemW88yRQ6UbZoLAm5MamiAwwklw_c5fx5YE2jji8_5ELwSXVaJHI1reFuRzMqEotHhV6lJC2O95dGR-sqm3Lq7A1EmBGZDWFv0UuV-yK42sBaHQAAAAFI7DftAA"
FORCESUB = "restrictedcontentt"
AUTH = 5518407661
auth_str = config("AUTH", default="")
AUTHORIZED_USERS = [int(user_id.strip()) for user_id in auth_str.split(",") if user_id.strip()]

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
