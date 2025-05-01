import os

from aiogram import Dispatcher, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

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
async def Orqaga(message: Message):
    await message.answer("Siz orqaga qayittingiz", reply_markup=btn)



@router.message(F.text=="Yaqin filliallarni korsatish")
async def yaqin_filliallarni_korsatish(message: Message):
    await message.answer("eng yaqin filialni topish uchun"
                         "joylashuvingizni yuboring",reply_markup=geolokatsiya_btn)




@router.message(F.text=="orqaga")
async def orqaga(message: Message):
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