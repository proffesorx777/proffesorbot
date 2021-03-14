import asyncio
import os
from datetime import datetime
from pathlib import Path

from userbot import ALIVE_NAME, bot
from userbot.utils import admin_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5
thumb_image_path = "./resources/541200.png"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ɓ乛ℓα૮ µรε૨ɓσƭ"


@borg.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await pro.edit(
            f"**==> Plugin name:** `{input_str}`\n**==> Uploaded in {time_taken_in_ms} seconds only.**\n**==> Uploaded by:ɓ乛ℓα૮ µรε૨ɓσƭ 's** [{DEFAULTUSER}](tg://user?id={hmm})\n"
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await edit_or_reply(event, "**404**: __File Not Found__")


@borg.on(admin_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "B-Lac  successfully installed this plguin\n @BLACUSERBOT `{}`".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "**Error!**\nPlugin cannot be installed!\n Or may have been pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded {shortname}")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(shortname, str(e))
        )


@borg.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully uninstall {shortname}")
    except Exception as e:
        await event.edit(
            "Successfully uninstall {shortname}\n{}".format(shortname, str(e))
        )


@borg.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )
