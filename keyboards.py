from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from messages import messages


def start_buttons(lang):
    buttons = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['about_company']}"),
         KeyboardButton(text=f"{messages[lang]['branches']}")],
        [KeyboardButton(text=f"{messages[lang]['job_positions']}")],
        [KeyboardButton(text=f"{messages[lang]['menu']}",
                        web_app=WebAppInfo(url="https://bunyodnaimov.github.io/p2-evos-test-bot/")),
         KeyboardButton(text=f"{messages[lang]['news']}")],
        [
            KeyboardButton(text=f"{messages[lang]['contacts']}"),
            KeyboardButton(text=f"{messages[lang]['language']}")
        ],
        [KeyboardButton(text=f"{messages[lang]['send_location']}", request_location=True), ]

    ],

        resize_keyboard=True)

    return buttons


def select_language():
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿", callback_data="uz"),
         InlineKeyboardButton(text="🇷🇺", callback_data="ru"),
         ]

    ], resize_keyboard=True)
    return buttons