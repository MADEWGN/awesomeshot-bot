import os
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from dotenv import load_dotenv

load_dotenv()

app = Client(
    "tesbot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    plugins=dict(root="plugins")
)

print('Bot Started!')
app.run()
