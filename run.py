import asyncio
import logging
from aiogram import Dispatcher
from config_reader import bot
from app.handlers_start import router


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
