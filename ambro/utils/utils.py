# Credits: @mrismanaziz
# FROM Man-ambro <https://github.com/mrismanaziz/Man-ambro>
# t.me/Sharingambro & t.me/Lunatic0de
# Ported By @IDnyaKosong

import asyncio
import importlib
import logging
import sys
from pathlib import Path
from random import randint

import heroku3
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditPhotoRequest,
    EditAdminRequest
)
from telethon.tl.types import (
    ChatAdminRights,
)
from ambro import (
    BOT_TOKEN,
    BOTLOG_CHATID,
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    LOGS,
    bot,
)

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def autobot():
    if BOT_TOKEN:
        return
    await bot.start()
    await bot.send_message(
        BOTLOG_CHATID, "**يتم حاليًا إنشاء روبوت Telegram لك على @BotFather**"
    )
    who = await bot.get_me()
    name = who.first_name + " Assistant Bot"
    if who.username:
        username = who.username + "_Ubot"
    else:
        username = "Joo" + (str(who.id))[5:] + "Ubot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "الرجاء إنشاء روبوت من @BotFather وإضافة الرمز المميز في BOT_TOKEN var"
        )
        sys.exit(1)
    await bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
            )
            sys.exit(1)
    await bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "Joo" + (str(who.id))[6:] + str(ran) + "Ubot"
        await bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, "Search")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_file(bf, "resources/joo.png")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"ببوت مساعد🥂 By {who.first_name}")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(
                bf, f"✪ ᴏᴡɴᴇʀ ~ {who.first_name} ✪\n\n✪ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ~ @ProjectJoni ✪"
            )
            await bot.send_message(
                BOTLOG_CHATID,
                f"**BERHASIL MEMBUAT BOT TELEGRAM DENGAN USERNAME @{username}**",
            )
            await bot.send_message(
                BOTLOG_CHATID,
                "**Tunggu Sebentar, Sedang MeRestart Heroku untuk Menerapkan Perubahan.**",
            )
            rights = ChatAdminRights(
                             add_admins=False,
                             invite_users=True,
                             change_info=True,
                             ban_users=True,
                             delete_messages=True,
                             pin_messages=True,
                             anonymous=False,
                             manage_call=True,
                         )
            await bot(EditAdminRequest(int(BOTLOG_CHATID), f"@{username}", rights, "ᴀssɪsᴛᴀɴᴛ ᴊσσ"))
            memek = "resources/joologs.png"
            await bot(EditPhotoRequest(BOTLOG_CHATID, await bot.upload_file(memek)))
            heroku_var["BOT_TOKEN"] = token
            heroku_var["BOT_USERNAME"] = f"@{username}"
        else:
            LOGS.info(
                "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
            )
            sys.exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "Search")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setuserpic")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_file(bf, "resources/joo.png")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"مساعد  🥂 » {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"✪ المطور ~ {who.first_name} ✪\n\n✨ السورس ʙʏ ~ @Mlze1bot ✨"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"**تم بنجاح إنشاء روبوت Telegram باسم المستخدم @{username}**",
        )
        await bot.send_message(
            BOTLOG_CHATID,
            "**Tunggu Sebentar, Sedang MeRestart Heroku untuk Menerapkan Perubahan.**",
        )
        rights = ChatAdminRights(
                 add_admins=False,
                 invite_users=True,
                 change_info=True,
                 ban_users=True,
                 delete_messages=True,
                 pin_messages=True,
                 anonymous=False,
                 manage_call=True,
             )
        await bot(EditAdminRequest(int(BOTLOG_CHATID), f"@{username}", rights, "ᴀssɪsᴛᴀɴᴛ ᴊσσ"))
        memek = "resources/joologs.png"
        await bot(EditPhotoRequest(BOTLOG_CHATID, await bot.upload_file(memek)))
        heroku_var["BOT_TOKEN"] = token
        heroku_var["BOT_USERNAME"] = f"@{username}"
    else:
        LOGS.info(
            "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
        )
        sys.exit(1)


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"ambro/modules/{shortname}.py")
        name = "ambro.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:

        path = Path(f"ambro/modules/{shortname}.py")
        name = "ambro.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.CMD_HELP = CMD_HELP
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["ambro.modules." + shortname] = mod
        LOGS.info("Successfully imported " + shortname)


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"ambro/modules/assistant/{shortname}.py")
        name = "ambro.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Starting Your Assistant Bot.")
        LOGS.info("Assistant Sucessfully imported " + shortname)
    else:
        path = Path(f"ambro/modules/assistant/{shortname}.py")
        name = "ambro.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["ambro.modules.assistant" + shortname] = mod
        LOGS.info("Assistant Successfully imported" + shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in CMD_HELP[shortname]:
                bot.remove_event_handler(i)
            del CMD_HELP[shortname]

        except BaseException:
            name = f"ambro.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


# bye Ice-ambro

async def create_supergroup(group_name, client, botusername, descript):
    try:
        result = await client(
            functions.channels.CreateChannelRequest(
                title=group_name,
                about=descript,
                megagroup=True,
            )
        )
        created_chat_id = result.chats[0].id
        result = await client(
            functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            )
        )
        await client(
            functions.channels.InviteToChannelRequest(
                channel=created_chat_id,
                users=[botusername],
            )
        )
    except Exception as e:
        return "error", str(e)
    if not str(created_chat_id).startswith("-100"):
        created_chat_id = int("-100" + str(created_chat_id))
    return result, created_chat_id


async def autopilot():
    if BOTLOG_CHATID and str(BOTLOG_CHATID).startswith("-100"):
        return
    k = []  # To Refresh private ids
    async for x in bot.iter_dialogs():
        k.append(x.id)
    if BOTLOG_CHATID:
        try:
            await bot.get_entity(int("BOTLOG_CHATID"))
            return
        except BaseException:
            del heroku_var["BOTLOG_CHATID"]
    try:
        r = await bot(
            CreateChannelRequest(
                title="「ѕᴏʀᴄᴇ ᴀᴍʙʀᴏ」𝙇𝙊𝙂𝙎",
                about="𝙂𝙧𝙤𝙪𝙥 𝙇𝙤𝙜𝙨 🥷 ѕᴏʀᴄᴇ ᴀᴍʙʀᴏ 🥷\n\n 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 @Mlze1bot",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "Terlalu banyak channel dan grup, hapus salah satu dan restart lagi"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "Terjadi kesalahan, Buat sebuah grup lalu isi id nya di config var BOTLOG_CHATID."
        )
        exit(1)
    chat_id = r.chats[0].id
    if not str(chat_id).startswith("-100"):
        heroku_var["BOTLOG_CHATID"] = "-100" + str(chat_id)
    else:
        heroku_var["BOTLOG_CHATID"] = str(chat_id)
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )