import asyncio
import logging
from aiogram import Dispatcher
from config_reader import bot
from app.handlers_start import router
from app.handlers_internet import r_int
from app.handlers_iptv import r_iptv
from app.handlers_ktv import r_ktv


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(r_int)
    dp.include_router(r_iptv)
    dp.include_router(r_ktv)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
