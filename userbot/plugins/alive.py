# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# modified by Pawan jatt
# Kang with credits else gay...
import asyncio
import os
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME
from userbot.thunderconfig import Config
from userbot.utils import admin_cmd, sudo_cmd

# ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else " Bä¹LAC UÊÒ½É¾áÏÆ"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
Blacversion = "1.5"
ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Jatt = bot.uid
# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/74cd131c1cc3aa962f9a9.mp4"

""" =======================CONSTANTS====================== """
pm_caption = "**ð¹ðð¸â ððð¼âð¹ðð ðð ðâððâð¼**\n\n"

pm_caption += f"ðð¹ðð¸â ððð¼âð¹ððð       : __**{Blacversion}**__\n"

pm_caption += "ð¡ï¸ðð¼ðð¼ðâðâð¡ï¸ : `1.19.0` \n"

pm_caption += f"âï¸ððð»ðâï¸            : `{sudou}`\n"

pm_caption += "â ï¸ââð¸ââð¼ðâ ï¸   : [ðððâ](https://t.me/BLAC_USERBOT)\n"

pm_caption += "ð¥ââð¼ð¸ððâð¥    : [âððð¹ âð¼âð¼](https://t.me/ERROR_404_USER_NOT_FOUNDED)\n\n"

pm_caption += "ð¥ð¹ðð¸â ð¾ð¸âð¾ ððâð¼âð¥    : [ðð¸ððð¸ ðð¸ðð](https://t.me/JATTGAMINGYT11)\n\n"

pm_caption += "    [â¨âð¼âðâ¨](https://github.com/B-Lac/B-Lac-Userbot) ð¹ [ðððâð¼âðð¼ð](https://github.com/B-Lac/B-Lac-Userbot/blob/master/LICENSE)\n"

pm_caption += f"â¾ **ðð ðð¸ððð¼â** â [{DEFAULTUSER}](tg://user?id={ghanti})\n"

pm_caption += "[ââââ¦âââââ¦ââââââ¦ââ¦âââ\nâââââââââââââââââ âââ\nââââââ£â â£âââââââââââ\nââââ©ââ©âââ©ââââââ©ââââ](https://t.me/BLAC_USERBOT)"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "** Bä¹LAC UÊÒ½É¾áÏÆ ð¸ð ð¾ï¸ð½ð»ð¸ð½ð´**\n"
        pm_caption += f"**ððª ð¹ð ð¤ð¤**            : {DEFAULTUSER}\n"
        pm_caption += "ðð´ð»ð´ðð·ð¾ð½ ðð´ððð¸ð¾ð½        : 1.17.5\n"
        pm_caption += "ð¿ððð·ð¾ð½ ðð´ððð¸ð¾ð½          : 3.9.0\n"
        pm_caption += "ððð¿ð¿ð¾ðð ð²ð·ð°ð½ð½ð´ð»         : [á´á´ÉªÉ´](https://t.me/BLAC_USERBOT)\n"
        pm_caption += (
            "ððð¿ð¿ð¾ðð ð¶ðð¾ðð¿           : [á´á´ÉªÉ´](https://t.me/BLAC_USERBOT_GROUP)\n"
        )
        pm_caption += "ððððððð                  : [AGPL-3.0  ÊÉªá´á´É´ê±á´](https://github.com/B-Lac/B-Lac-Userbot/blob/master/License)\n"
        pm_caption += (
            "ð¾ðððððððð ð½ð            : [  Bä¹LAC UÊÒ½É¾áÏÆ ](https://t.me/BLAC_USERBOT)\n"
        )
        pm_caption += "[âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ \n âââââââââ«ââââââââââ \n âââââââââââââââââââ](https://t.me/BLAC_USERBOT)"
        await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            alive.chat_id, ALIVE_PHOTTO, caption=pm_caption, link_preview=False
        )
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/74cd131c1cc3aa962f9a9.mp4")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(
            alive.chat_id,
            "** Bä¹LAC UÊÒ½É¾áÏÆ ð¸ð ð¾ï¸ð½ð»ð¸ð½ð´**\n"
            f"**ððª ð¹ð ð¤ð¤**            : {DEFAULTUSER}\n"
            "ðð´ð»ð´ðð·ð¾ð½ ðð´ððð¸ð¾ð½        : 1.17.5\n"
            "ð¿ððð·ð¾ð½ ðð´ððð¸ð¾ð½          : 3.9.0\n"
            "ððð¿ð¿ð¾ðð ð²ð·ð°ð½ð½ð´ð»         : [á´á´ÉªÉ´](https://t.me/BLAC_USERBOT)\n"
            "ððð¿ð¿ð¾ðð ð¶ðð¾ðð¿           : [á´á´ÉªÉ´](https://t.me/BLAC_USERBOT_GROUP)\n"
            "ððððððð                  : [AGPL-3.0  ÊÉªá´á´É´ê±á´](https://github.com/B-Lac/B-Lac-Userbot/blob/master/License)\n"
            "ð¾ðððððððð ð½ð            : [  Bä¹LAC UÊÒ½É¾áÏÆ ](https://t.me/BLAC_USERBOT)\n"
            "[ âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ \n âââââââââ«ââââââââââ \n âââââââââââââââââââ](https://t.me/BLAC_USERBOT)",
            link_preview=False,
        )
        await alive.delete()
