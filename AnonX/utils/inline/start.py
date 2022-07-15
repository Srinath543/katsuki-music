from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from MAJA EXPRESS import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="😈 𝐒𝐀𝐌𝐁𝐔 𝐌𝐀𝐕𝐀𝐍𝐄 𝐀𝐃𝐃 𝐏𝐀𝐍𝐍𝐔𝐃𝐀 𝐆𝐑𝐎𝐔𝐏 𝐋𝐀 😈",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐔𝐓𝐇𝐀𝐕𝐈",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="😈 𝐆𝐔𝐑𝐔 𝐍𝐀𝐓𝐇𝐀𝐑 😈", user_id=OWNER),
            InlineKeyboardButton(
                text="🏰 𝐀𝐑𝐀𝐍𝐌𝐀𝐍𝐀𝐈 🏰", url=f"https://t.me/Tamil_chat_junctions"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="😈 𝐒𝐀𝐌𝐁𝐔 𝐌𝐀𝐕𝐀𝐍𝐄 𝐀𝐃𝐃 𝐏𝐀𝐍𝐍𝐔𝐃𝐀 𝐆𝐑𝐎𝐔𝐏 𝐋𝐀 😈",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐔𝐓𝐇𝐀𝐕𝐈", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="😈 𝐆𝐔𝐑𝐔 𝐍𝐀𝐓𝐇𝐀𝐑 😈", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/Tamil_chat_junctions"
                )
        ],
     ]
    return buttons
