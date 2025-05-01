from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup


btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompaniya haqida"),
         KeyboardButton(text="Filliallar"),],
        [KeyboardButton(text="Bo'sh ish o'rinlari"),],
        [KeyboardButton(text="Menyu"),
         KeyboardButton(text="Yangiliklar")],
        [KeyboardButton(text="Kontakt/Manzil"),
         KeyboardButton(text="uz/ru til")],
    ],resize_keyboard=True,)


filliallar_btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yaqin filliallarni korsatish"),],
        [KeyboardButton(text="Bosh o'fis"),
         KeyboardButton(text="Toshkent sh")],
        [KeyboardButton(text="Orqaga")]],resize_keyboard=True,
)
geolokatsiya_btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Geolokatsiyani yuborish"),],
        [KeyboardButton(text="orqaga"),],
    ],resize_keyboard=True,
)

toshkent_sh_btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Samarqand darvoza"),
         KeyboardButton(text="Oloy bozor"),],
        [KeyboardButton(text="Malika"),
         KeyboardButton(text="Yahyo G'ulomov, 94")],
        [KeyboardButton(text="Orqaga3"),]
    ]
)
