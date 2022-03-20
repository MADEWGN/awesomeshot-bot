import os
from telegraph import upload_file
import glob
import io
import sys
import traceback
from pyrogram import Client
from pyrogram import filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message

DOWNLOAD_LOCATION = "dl/"


@Client.on_message(filters.private & filters.media)
async def getmedia(client, message):
    chat_id = int(message.chat.id)
    medianame = DOWNLOAD_LOCATION + str(message.from_user.id)

    pesan = await message.reply_text("`Processing...`")
    await message.download(file_name=medianame)
     

    a = "awesomeshot -m "
    c = f'{a}{medianame}'
    os.system(c)

    list_of_files = glob.glob('dl/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)



    
    response = upload_file(latest_file)


    text=f"**Link :-** `https://telegra.ph{response[0]}`\n\n**Dev :-** @madewgn"
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
            ],
            [
                InlineKeyboardButton(text="Repo", url="https://telegram.me/FayasNoushad")
            ]
        ]
    )
    
   # await message.reply_message(
        #text=text,
        #disable_web_page_preview=True,
        #reply_markup=reply_markup
    #)

    await pesan.edit("`Uploading...`")
    await client.send_photo(
        chat_id=chat_id,
        photo=latest_file,
        caption=text,
        reply_markup=reply_markup
        
    )
    os.remove(latest_file)

    print("sukses")
