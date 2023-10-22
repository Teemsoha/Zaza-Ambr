from telethon import Button

from ambro import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/02f87cca391f9b9d627d5.jpg",
                caption="**🥷ѕᴏʀᴄᴇ ᴀᴍʙʀᴏ🥷 Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @ProjectJoni ",
                buttons=[(Button.url("السورس", "https://t.me/Mlze1bot"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
