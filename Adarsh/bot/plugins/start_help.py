# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

@StreamBot.on_message((filters.command("start")) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\n [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__Sorry, you are banned. Contact My Owner [Rushidhar](https://telegram.me/rushidhar1999/)__",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://te.legra.ph/file/95db9bf6f91bd96d7a9f1.jpg",
                caption="<i>Join Channel To Use Me🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Now 🔓", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>Something went wrong</i> <b> <a href='https://telegram.me/rushidhar1999'>CLICK HERE FOR SUPPORT </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://te.legra.ph/file/95db9bf6f91bd96d7a9f1.jpg",
        caption =f'Hi {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻 Owner", url="https://telegram.me/rushidhar1999")]
            ]
        )
    )



@StreamBot.on_message((filters.command("help")) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\n [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="__Sorry, you are banned. Contact My Owner [Rushidhar](https://telegram.me/rushidhar1999/)__",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Join Channel To Use Me🔐__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Now 🔓", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Something Went Wrong. Contact__ [Rushidhar](https://telegram.me/rushidhar1999/).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>Send me any file or video i will give you streamable link and download link.</b>\n\n<b>I also support Channels, add me to you Channel and send any media files and see miracle also send /list to know all commands""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ DEV", url="https://t.me/rushidhar1999/")]
               
            ]
        )
    )
