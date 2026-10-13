import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"http://telegra.ph/file/de61130f75f47984f0530.jpg",
        caption=f"""**
『It's a Music bot without lag and struck .
  ❌ Fully Stable ❌ workflows Deployment 
  ❌ 3 HRS nonstop playing 
Nb : Bot and Userbot are locked by owner ,
     who wish to add this bot to your group,
     then , contact @kk_heaven_hater』
**""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝗖𝗛𝗔𝗡𝗡𝗘𝗟』", url=f"https://t.me/KK_LINKS"),
                    InlineKeyboardButton(
                        "『𝗜𝗡𝗦𝗧𝗔🎭𝗚𝗥𝗔𝗠』", url=f"https://www.instagram.com/kani_mangalamkovilakam/"),
                 ],[
                    InlineKeyboardButton(
                        "『𝗙𝗔𝗖𝗘🌎𝗕𝗢𝗢𝗞』", url=f"https://www.facebook.com/profile.php?id=100085628503716"),
                    InlineKeyboardButton(
                        "『𝗚𝗥𝗢𝗨𝗣』", url=f"https://t.me/kanimangalamkovilakam") 
                ]
            ]
        ),
     )
    
    
@Client.on_message(commandpro(["/start", "/alive", "blackcat"]) & filters.group)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"http://telegra.ph/file/de61130f75f47984f0530.jpg",
        caption=f"""**𝙾𝙵𝙵𝙸𝙲𝙸𝙰𝙻 𝐌𝐔𝐒𝐈𝐂 Bot of 𓄂𝐊𝐊࿐ཽ༵✰**,
        ❌ Fully Stable ❌ workflows Deployment 
  ❌ 3 HRS nonstop playing 
Nb : Bot and Userbot are locked by owner ,
     who wish to add this bot to your group,
     then , contact @kk_heaven_hater』
        NB:- 24HRS ASSISTANCE OF bot
             for anytime help:- [✞𖤍◣‌⃟⃟⃟⃟⃟࿅‌❰❰⃘꯭꯭Ꭰᴀʀᴋ†💢꛱‌꯭꯭꯭†❰❰꯭꯭꯭ ⃘Ꭰ꯭ᴇᴠᴉɭ✇࿅‌𖤍✞](https://t.me/FULLY_CRUAL_MIND), 
                                  [༂𝄇𖤓࿈കൃഷ്ണതുളസ᭄🌙⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ࿈𖤓𝄆༂](https://t.me/KRISHNA_THULSI)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "▲𝐅𝐀𝐌𝐈𝐋𝐘▼", url=f"https://t.me/KK_LINKS"),
                    InlineKeyboardButton(
                        "『𝐈𝐧𝐬𝐭𝐚🎭𝐆𝐫𝐚𝐦』", url=f"https://www.instagram.com/kani_mangalamkovilakam/"),
                    InlineKeyboardButton(
                        "『𝐅𝐀𝐂𝐄🌎𝐁𝐎𝐎𝐊』", url=f"https://www.facebook.com/profile.php?id=100085628503716"),
                    InlineKeyboardButton(
                        "『𝗚𝗥𝗢𝗨𝗣』", url=f"https://t.me/kanimangalamkovilakam")
                ]
            ]
        ),
    )

