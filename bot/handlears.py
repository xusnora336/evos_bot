import os

from aiogram import Dispatcher, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from keyboards import filliallar_btn_ru, toshkent_sh_btn_ru, geolokatsiya_btn_ru
from keyboards import btn_ru, uz_ru_btn
from keyboards import toshkent_sh_btn
from keyboards import geolokatsiya_btn
from keyboards import filliallar_btn
from keyboards import btn

router = Router()


@router.message(F.text=="Kompaniya haqida")
async def kompaniya_haqida(message: Message):

    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "evos.png"))
    txt=("EVOS tez xizmat ko'rsatish restoranlari tarmog'i bir\n"
        "joyda turmaydi, siz uchun va siz bilan doimo o'sib\n"
        "boradi va rivojlanadi! biz geografiyamizni\n"
        "kengaytiramiz va geyarli har oyda yangi filliallarni\n"
        "ochamiz.\n"
        "Endi bizning tarmog'imizning O'zbekistoz bo'ylab 50\n"
        "dan ortiq filliali mavjud. Biz doimo jamoamizning bir\n"
        "qismi bo'lishni xohlaydigan va EVOS da o'z\n"
        "faoliyatini boshlashga tayyor bo'lgan dinamik va faol\n"
        "odamlarni qidiramiz.")
    await message.answer_photo(photo=img,caption=txt,reply_markup=btn)

@router.message(F.text=="Filliallar")
async def filliallar(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "evos.png"))
    txt=("EVOS-O'zbekistondagi eng yirik fastfud kompaniyasi.\n"
         "Ayni payitda 49 ta chakana savdo shoxobchasi va\n"
         "zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.")
    await message.answer_photo(photo=img,caption=txt, reply_markup=filliallar_btn)

@router.message(F.text=="Bosh o'fis")
async def bosh_ofis(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "ofis.png"))
    text=("Manzil: Furqat ko'chasi 175, 1-kirish, 4-qavat\n"
          "Mo'ljal: MAKRO THE TOWER")
    await message.answer_photo(photo=img,caption=text,reply_markup=filliallar_btn)

@router.message(F.text=="Toshkent sh")
async def toshkent_sh(message: Message):
    await message.answer("Toshkent sh",reply_markup=toshkent_sh_btn)

@router.message(F.text=="Samarqand darvoza")
async def samarqand_darvoza(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "samarqand_darvoza.png"))
    text=("Filial: Samarqand darvoza\n"
          "Manzil: Qoratosh, 5A")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn)

@router.message(F.text=="Oloy bozor")
async def oloy_bozor(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "oloy_bozori.png"))
    text=("Filial: Oloy bozor\n"
          "Manzil: Amir Temur prospekti, 42\n"
          "Kontakt: +998 712031212")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn)

@router.message(F.text=="Malika")
async def malika(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "malika.png"))
    text=("Filial: Malika\n"
          "Manzil: Bog'iravon, 29\n"
          "Kontakt: +998 712031212")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn)

@router.message(F.text=="Yahyo G'ulomov, 94")
async def yahyo_g(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "yahyo_g.png"))
    text=("Filial: Yahyo G'ulomov, 94\n"
          "Manzil: Yahyo G'ulom kochasi, 94\n")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn)

@router.message(F.text=="Orqaga3")
async def orqaga3(message: Message):
    await message.answer("Siz orqaga qayittingiz",reply_markup=filliallar_btn)


@router.message(F.text=="Orqaga")
async def Orqagaaa(message: Message):
    await message.answer("Siz orqaga qayittingiz", reply_markup=btn)



@router.message(F.text=="Yaqin filliallarni korsatish")
async def yaqin_filliallarni_korsatish(message: Message):
    await message.answer("eng yaqin filialni topish uchun"
                         "joylashuvingizni yuboring",reply_markup=geolokatsiya_btn)




@router.message(F.text=="orqaga")
async def orqagaaa(message: Message):
    await message.answer("orqaga qayittingiz", reply_markup=filliallar_btn)


@router.message(F.text=="Menyu")
async def menyu(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "menu.png"))
    text="EVOS sayitiga o'tish"
    await message.answer_photo(photo=img,caption=text,reply_markup=btn)

@router.message(F.text=="Yangiliklar")
async def yangiliklar(message: Message):
    await message.answer("Kompaniya yangiliklari:\n"
                         "Aksiya\n"
                         "Yangi filiallar\n"
                         "Yangi tortlar va hk.",reply_markup=btn)

@router.message(F.text=="Kontakt/Manzil")
async def kontakt_manzil(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "evos.png"))
    text=("Manzil: Furqat ko'chasi 175, kirish 1,\n"
          "2-qavat.\n"
          "Mo'ljal: MAKRO THE TOWER\n"
          "\n"
          "Kontakt: +998 712031212")
    await message.answer_photo(photo=img,caption=text,reply_markup=btn)



#######################################################
@router.message(F.text=="uz/ru til")
async def uz_ru_til(message: Message):
    await message.answer("Tilni tanlang: ", reply_markup=uz_ru_btn)

@router.message(F.text=="uz")
async def uz(message: Message):
    await message.answer("Siz o'zbekchani tanladingiz", reply_markup=btn)

@router.message(F.text=="ru")
async def ru(message: Message):
    await message.answer("Siz ruschani tanladingiz", reply_markup=btn_ru)


@router.message(F.text=="🏢 О компании")
async def kompanii(message: Message):

    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "evos.png"))
    txt=("Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте,\n"
         "а постоянно растет и развивается вместе с вами и для вас! Мы расширяем свою географию и открываем новые филиалы практически каждый месяц. \n"
        "Сейчас в нашей сети насчитывается более 70 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и активных людей,\n"
         " которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®.\n"
        "EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного роста.\n"
        "kengaytiramiz va geyarli har oyda yangi filliallarni\n"
        "ochamiz.\n"
        "Начни свою карьеру в EVOS® уже сейчас\n"
        )
    await message.answer_photo(photo=img,caption=txt,reply_markup=btn_ru)


@router.message(F.text=="📍 Филиалы")
async def filliali(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "evos.png"))
    txt=("EVOS - крупнейшая фастфуд-компания в Узбекистане.\n"
         "На данный момент открыто более 70 торговых точек и\n"
         " современное многопрофильное производство\n"
         "Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день\n"
         "Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч.\n"
         " Стань частью нашей команды, добро пожаловать в семью EVOS")
    await message.answer_photo(photo=img,caption=txt, reply_markup=filliallar_btn_ru)

@router.message(F.text=="🏢 Головной офис")
async def golovnoy_ofis(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "ofis.png"))
    text=("Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.\n"
          "Ориентир: MAKRO THE TOWER")
    await message.answer_photo(photo=img,caption=text,reply_markup=filliallar_btn_ru)

@router.message(F.text=="г. Ташкент")
async def g_toshkent(message: Message):
    await message.answer("г. Ташкент",reply_markup=toshkent_sh_btn_ru)

@router.message(F.text=="📍 Samarqand Darvoza")
async def Samarqand_darvoza(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "samarqand_darvoza.png"))
    text=("Филиал: Самарканд дарвоза\n"
          "Адрес: ул. Коратош, 5А")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn_ru)

@router.message(F.text=="📍 Алайский базар")
async def alayskiy_bazar(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "oloy_bozori.png"))
    text=("Филиал: Алайский базар\n"
          "Адрес: просп. Амира Темура, 42\n"
          "Контакты: +998 71 203 12 12")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn_ru)

@router.message(F.text=="📍 Малика")
async def Malika(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "malika.png"))
    text=("Филиал: Малика\n"
          "Адрес: ул. Богиравон, 29\n"
          "Контакты: +998 71 203 12 12")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn_ru)

@router.message(F.text=="📍 Яхъё Гулямова, 94")
async def yahyo_g(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "yahyo_g.png"))
    text=("Филиал: улица Яхъё Гулямова, 94\n"
          "Адрес: улица Яхъё Гулямова, 94\n")
    await message.answer_photo(photo=img,caption=text,reply_markup=toshkent_sh_btn_ru)

@router.message(F.text=="Назад")
async def nazad(message: Message):
    await message.answer("Назад",reply_markup=filliallar_btn_ru)


@router.message(F.text=="⬅️ Назад")
async def oorqaga(message: Message):
    await message.answer("⬅️ Назад", reply_markup=btn)



@router.message(F.text=="☕️ Показать ближайший филиал")
async def blijayushiy_fillial(message: Message):
    await message.answer("Отправьте свое местоположение для определения ближайшего филиала",reply_markup=geolokatsiya_btn_ru)

@router.message(F.text=="отправить геолокацию")
async def otpravit(message: Message):
    await message.answer("",reply_markup=geolokatsiya_btn_ru)



@router.message(F.text=="Назад ↩️")
async def orqagaa(message: Message):
    await message.answer("Назад ↩️", reply_markup=btn_ru)


@router.message(F.text=="📱 Меню")
async def menu(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "menu.png"))
    text=("Перейти на сайт Evos (https://evos.uz/)\n"
          "Instagram (https://www.instagram.com/evosuzbekistan/)\n"
          "|Telegram (https://t.me/evosdeliverybot)|\n"
          "Facebook (https://www.facebook.com/evosuzbekistan/)")
    await message.answer_photo(photo=img,caption=text,reply_markup=btn_ru)

@router.message(F.text=="🗣 Новости")
async def novosti(message: Message):
    await message.answer("Новости компании:\n"
                         "Акции\n"
                         "Новые ветки\n"
                         "Свежие торты и т. д.",reply_markup=btn_ru)


@router.message(F.text=="📞 Контакты/Адрес")
async def kontakt_manzil(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "image", "evos.png"))
    text=("📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.\n"
          "📌Ориентир: MAKRO THE TOWER\n"
          "📲 Контакты: +998 71 203 12 12\n")
    await message.answer_photo(photo=img,caption=text,reply_markup=btn_ru)

@router.message(F.text=="🇺🇿/🇷🇺 Язык")
async def rru(message: Message):
    await message.answer("Смена языка",reply_markup=uz_ru_btn)

@router.message(F.text=="uz")
async def uzz(message: Message):
    await message.answer("Танланди: 🇺🇿 O'zbekcha", reply_markup=btn)

@router.message(F.text=="ru")
async def ruu(message: Message):
    await message.answer("Выбрано: 🇷🇺 Русский", reply_markup=btn_ru)


