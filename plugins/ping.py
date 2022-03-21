from datetime import datetime
import requests
import time
from requests import HTTPError
import io
import sys
import traceback
from pyrogram import Client
from pyrogram import filters

import asyncio




#@Client.on_message(filters.command("start") & filters.private & filters.incoming)
#async def start(_, message):
    #    pesan = await message.reply_text("halo")

@Client.on_message(filters.command("ping") & filters.private & filters.incoming)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"**Pong!**\n`{time_taken_s:.3f} ms`")
