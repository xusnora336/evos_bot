import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from commands import router as commands_router
from handlears import router as handlears_router
from dotenv import load_dotenv
from menu import bot_commands
# from aiogram.client.session.aiohttp import AiohttpSession
load_dotenv()



TOKEN = getenv("BOT_TOKEN")

# session = AiohttpSession(proxy="http://proxy.server:3128")

dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(handlears_router)



async def main() -> None:
    bot = Bot(token=TOKEN)
    # bot = Bot(token=TOKEN, session=session)
    await bot.set_my_commands(bot_commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())